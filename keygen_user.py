# 3 create folder keygen_user_logs

import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
import time

def generate_and_save_ecc_key_pair(user):
    ecc_key_folder = "keygen_user_logs"

    if not os.path.exists(ecc_key_folder):
        os.makedirs(ecc_key_folder)

    for node in user:
        private_key = ec.generate_private_key(ec.SECP256R1(), backend=default_backend())
        public_key = private_key.public_key()

        private_key_file = os.path.join(ecc_key_folder, f"{node}_private_key.pem")
        with open(private_key_file, 'wb') as f:
            private_key_pem = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
            f.write(private_key_pem)

        public_key_file = os.path.join(ecc_key_folder, f"{node}_public_key.pem")
        with open(public_key_file, 'wb') as f:
            public_key_pem = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
            f.write(public_key_pem)

        print(f"ECC key pair generated and saved for {node}")

start_time = time.time()

user = ["user_1"]

generate_and_save_ecc_key_pair(user)

end_time = time.time()
execution_time = end_time - start_time

print("Execution time:", execution_time, "seconds")
