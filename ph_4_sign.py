import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives import padding  # Import padding module
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

    # Apply PKCS7 padding to plaintext
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    return ciphertext

def sign_md(private_key, md):
    signature = private_key.sign(
        md,
        ec.ECDSA(hashes.SHA256())
    )
    return signature

def encrypt_to_sign_from_hash_and_sign():
    hash_folder = "hash_plant_house_logs_400"
    d_sign_logs_folder = "enc_d_sign_logs"
    moac_key_folder = "keygen_moac_logs"
    ph_key_folder = "keygen_planthouse_logs"
    #signature_folder = "signature_log"

    if not os.path.exists(d_sign_logs_folder):
        os.makedirs(d_sign_logs_folder)

    for filename in os.listdir(hash_folder):
        
        plant_house = filename[:-9]  # Extracting the plant house name
        print("PlantHouse: ", plant_house)
        public_key_file = os.path.join(moac_key_folder, "moac_1_public_key.pem")

        if not os.path.exists(public_key_file):
            print(f"Public key file not found for {plant_house}. Skipping encryption for this plant house.")
            continue

        hash_file = os.path.join(hash_folder, f"{plant_house}.log.hash")
        with open(hash_file, 'rb') as f:
            message_digest = f.read()

        with open(public_key_file, 'rb') as f:
            public_key_data = f.read()
        moac_public_key = serialization.load_pem_public_key(public_key_data, backend=default_backend())

        if plant_house.startswith("plant_house_10"):
            private_key_file = os.path.join(ph_key_folder, f"{plant_house[:-30]}_privat_key.pem")
            print(f"{plant_house[:-30]}_privat_key.pem\n")
        else:
            if (len(plant_house[:-20]) == 13):
                private_key_file = os.path.join(ph_key_folder, f"{plant_house[:-29]}_privat_key.pem")
                print(f"{plant_house[:-29]}_privat_key.pem\n")
            elif (len(plant_house[:-20]) == 14):
                private_key_file = os.path.join(ph_key_folder, f"{plant_house[:-29]}privat_key.pem")
                print(f"{plant_house[:-29]}privat_key.pem\n")

        with open(private_key_file, 'rb') as f:
            private_key_data = f.read()
        ph_private_key = serialization.load_pem_private_key(private_key_data, password=None, backend=default_backend())

        # Sign the message digest using the sender's private key
        signature = sign_md(ph_private_key, message_digest)

        # signature_file = os.path.join(signature_folder, filename + ".sig")
        # with open(signature_file, 'wb') as f:
        #     f.write(signature)
        
        shared_secret = derive_shared_secret(ph_private_key, moac_public_key)
        
        # Encrypt the signature using the shared secret
        enc_sig = encrypt_data_with_shared_secret(shared_secret, signature)

        enc_sig_file = os.path.join(d_sign_logs_folder, filename + ".sig")
        with open(enc_sig_file, 'wb') as f:
            f.write(enc_sig)

        print(f"Digital Signature encrypted for {plant_house}")
start_time = time.time()

encrypt_to_sign_from_hash_and_sign()

end_time = time.time()
execution_time = end_time - start_time

print("Execution time:", execution_time, "seconds")
