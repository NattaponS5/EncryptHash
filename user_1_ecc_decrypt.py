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

def decrypt_data_with_shared_secret(shared_secret, ciphertext):
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'ECC shared secret encryption key',
        backend=default_backend()
    ).derive(shared_secret)

    iv = b'\x00' * 16
    cipher = Cipher(algorithms.AES(derived_key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext

# def extract_date_from_directory(directory):
#     # Get the list of directories in the parent directory
#     subdirectories = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
    
#     # Iterate over the subdirectories
#     for subdir in subdirectories:
#         if subdir.startswith("enc_aes_key_2024"):
#             # Extract the date and time from the directory name
#             date = subdir[len("enc_aes_key_"):].replace("_", "_")
#             #print("Date:", date)
#             break
#     return date

def decrypt_aes_keys_with_ecc_private_keys(directory):
    # date = extract_date_from_directory(directory)
    enc_aes_keys_folder = f"enc_aes_key_logs_9"
    dec_aes_keys_folder = f"dec_aes_key_logs_9"
    user_key_folder = "keygen_user_logs"
    ph_key_folder = "keygen_planthouse_logs"

    if not os.path.exists(dec_aes_keys_folder):
        os.makedirs(dec_aes_keys_folder)

    for filename in os.listdir(enc_aes_keys_folder):
        enc_aes_key_file = os.path.join(enc_aes_keys_folder, filename)
        with open(enc_aes_key_file, 'rb') as f:
            enc_aes_key = f.read()

        plant_house = filename[:-8]  # Extracting the plant house from the filename
        private_key_file = os.path.join(user_key_folder, "user_1_private_key.pem")

        if not os.path.exists(private_key_file):
            print(f"Private key file not found for {plant_house}. Skipping decryption for this plant house.")
            continue

        with open(private_key_file, 'rb') as f:
            private_key_data = f.read()
        private_key = serialization.load_pem_private_key(private_key_data, password=None, backend=default_backend())

        public_key_file = os.path.join(ph_key_folder, f"{plant_house}_public_key.pem")

        if not os.path.exists(public_key_file):
            print(f"Public key file not found for {plant_house}. Skipping encryption for this plant house.")
            continue

        with open(public_key_file, 'rb') as f:
            public_key_data = f.read()
        public_key = serialization.load_pem_public_key(public_key_data, backend=default_backend())
        shared_secret = derive_shared_secret(private_key, public_key)

        aes_key = decrypt_data_with_shared_secret(shared_secret, enc_aes_key)

        dec_aes_key_file = os.path.join(dec_aes_keys_folder, filename[:-4])
        with open(dec_aes_key_file, 'wb') as f:
            f.write(aes_key)

        print(f"AES key decrypted for {plant_house}")

start_time = time.time()
# please change to your project directory
decrypt_aes_keys_with_ecc_private_keys("/home/nattapons5/vscode/EncryptHash")

end_time = time.time()
execution_time = end_time - start_time

print("Execution time:", execution_time, "seconds")