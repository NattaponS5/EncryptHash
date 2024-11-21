# 4 create folder aes_keys_logs and ciphertext_logs

from Crypto.Cipher import AES
import os
import secrets
import time

# Function to encrypt data using AES-CTR
def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_CTR)
    ciphertext = cipher.encrypt(data)
    nonce = cipher.nonce
    return ciphertext, nonce

# Function to save ciphertext to a file with the same name as the original log file
def save_ciphertext(ciphertext, output_file):
    with open(output_file, 'wb') as f:
        f.write(ciphertext)

# Function to save nonce to a file with the same name as the original log file
def save_nonce(nonce, output_file):
    with open(output_file, 'wb') as f:
        f.write(nonce)

def generate_aes_key():
    # Generate a 128-bit (16 bytes) random key using a secure PRNG
    aes_key = secrets.token_bytes(16)
    return aes_key

start_time = time.time()

# Input and output directories
input_folder = "plant_house_logs_400_9"
output_folder = "ciphertext_logs_9"

# Ensure output directory exists for encryption
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Create folders for plant house keys
keys_folder = "aes_keys_logs_9"
if not os.path.exists(keys_folder):
    os.makedirs(keys_folder)

# Default key
key = b''  # The key must be in bytes


# Define the number of plant houses
num_plant_houses = 10

# Iterate over each plant house
for i in range(1, num_plant_houses + 1):
    key = generate_aes_key()
    key_filename = f"plant_house_{i}.key"
    key_file_path = os.path.join(keys_folder, key_filename)
    with open(key_file_path, 'wb') as key_file:
        key_file.write(key)
    print(f"AES key for plant_house_{i} stored in {key_filename}.")


# Encrypt each file in the input directory
for filename in os.listdir(input_folder):
    key = b'' 
    input_file_path = os.path.join(input_folder, filename)
    # Read data from file
    with open(input_file_path, 'rb') as f:
        data = f.read()

    # AES key (replace with your own key)
    if filename[:14] == "plant_house_1_":
        key_file_path = os.path.join(keys_folder, "plant_house_1.key")
        with open(key_file_path, 'rb') as f:
            key = f.read()
    elif filename[:14] == "plant_house_2_":
        key_file_path = os.path.join(keys_folder, "plant_house_2.key")
        with open(key_file_path, 'rb') as f:
            key = f.read()
    elif filename[:14] == "plant_house_3_":
        key_file_path = os.path.join(keys_folder, "plant_house_3.key")
        with open(key_file_path, 'rb') as f:
            key = f.read()
    elif filename[:14] == "plant_house_4_":
        key_file_path = os.path.join(keys_folder, "plant_house_4.key")
        with open(key_file_path, 'rb') as f:
            key = f.read()
    elif filename[:14] == "plant_house_5_":
        key_file_path = os.path.join(keys_folder, "plant_house_5.key")
        with open(key_file_path, 'rb') as f:
            key = f.read()
    elif filename[:14] == "plant_house_6_":
        key_file_path = os.path.join(keys_folder, "plant_house_6.key")
        with open(key_file_path, 'rb') as f:
            key = f.read()
    elif filename[:14] == "plant_house_7_":
        key_file_path = os.path.join(keys_folder, "plant_house_7.key")
        with open(key_file_path, 'rb') as f:
            key = f.read()
    elif filename[:14] == "plant_house_8_":
        key_file_path = os.path.join(keys_folder, "plant_house_8.key")
        with open(key_file_path, 'rb') as f:
            key = f.read()
    elif filename[:14] == "plant_house_9_":
        key_file_path = os.path.join(keys_folder, "plant_house_9.key")
        with open(key_file_path, 'rb') as f:
            key = f.read()
    elif filename[:14] == "plant_house_10":
        key_file_path = os.path.join(keys_folder, "plant_house_10.key")
        with open(key_file_path, 'rb') as f:
            key = f.read()

    # Encrypt the data
    ciphertext, nonce = encrypt_data(data, key)

    # Save the ciphertext to the output file with the same name as the original log file
    output_file_path = os.path.join(output_folder, filename)
    save_ciphertext(ciphertext, output_file_path)

    # Save the nonce to a file with the same name as the original log file
    nonce_file_path = os.path.join(output_folder, filename + ".nonce")
    save_nonce(nonce, nonce_file_path)

    # Save the key to the corresponding folder
    key_file_path = os.path.join(keys_folder, key_filename)
    with open(key_file_path, 'wb') as key_file:
        key_file.write(key)


end_time = time.time()
execution_time = end_time - start_time

print("Execution time:", execution_time, "seconds")
