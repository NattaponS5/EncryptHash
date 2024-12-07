
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import time
def derive_shared_secret(private_key, public_key):
    shared_secret = private_key.exchange(ec.ECDH(), public_key)
    return shared_secret

def encrypt_data_with_shared_secret(shared_secret, plaintext):
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'ECC shared secret encryption key',
        backend=default_backend()
    ).derive(shared_secret)

    iv = b'\x00' * 16
    cipher = Cipher(algorithms.AES(derived_key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return ciphertext

def encrypt_aes_keys_with_ecc_keys():
    aes_keys_folder = "aes_keys_logs_9"
    enc_aes_keys_folder = "enc_aes_key_logs_9"
    user_key_folder = "keygen_user_logs"
    ph_key_folder = "keygen_planthouse_logs"


    if not os.path.exists(enc_aes_keys_folder):
        os.makedirs(enc_aes_keys_folder)

    for filename in os.listdir(aes_keys_folder):
        aes_key_file = os.path.join(aes_keys_folder, filename)
        with open(aes_key_file, 'rb') as f:
            aes_key = f.read()

        plant_house = filename[:-4]  # Extracting the plant house from the filename
        public_key_file = os.path.join(user_key_folder, "user_1_public_key.pem")

        if not os.path.exists(public_key_file):
            print(f"Public key file not found for {plant_house}. Skipping encryption for this plant house.")
            continue

        with open(public_key_file, 'rb') as f:
            public_key_data = f.read()
        public_key = serialization.load_pem_public_key(public_key_data, backend=default_backend())

        private_key_file = os.path.join(ph_key_folder, f"{plant_house}_privat_key.pem")
        with open(private_key_file, 'rb') as f:
            private_key_data = f.read()
        private_key = serialization.load_pem_private_key(private_key_data, password=None, backend=default_backend())

        shared_secret = derive_shared_secret(private_key, public_key)
        enc_aes_key = encrypt_data_with_shared_secret(shared_secret, aes_key)

        enc_aes_key_file = os.path.join(enc_aes_keys_folder, filename + ".enc")
        with open(enc_aes_key_file, 'wb') as f:
            f.write(enc_aes_key)

        print(f"AES key encrypted for {plant_house}")
start_time = time.time()
encrypt_aes_keys_with_ecc_keys()

end_time = time.time()
execution_time = end_time - start_time

print("Execution time:", execution_time, "seconds")