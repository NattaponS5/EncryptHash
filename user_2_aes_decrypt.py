from Crypto.Cipher import AES
import os
import time

# Function to decrypt data using AES-CTR
def decrypt_data(ciphertext, key, nonce):
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    decrypted_data = cipher.decrypt(ciphertext)
    return decrypted_data

# Function to save decrypted data to a file with the same name as the original ciphertext file
def save_decrypted_data(decrypted_data, output_file):
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)


def decrypt_ciphertext_with_aes_key(directory):
    # Input and output directories
    input_folder = f"ciphertext_logs_9"
    output_folder = f"Retrieved_PT_9"
    key_folder = f"dec_aes_key_logs_9"

    # Ensure output directory exists for decryption
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List the files in the key folder
    # key_files = os.listdir(key_folder)
    # print("Key files available:", key_files)

    # Default key
    key = b''  # The key must be in bytes

    # Decrypt each file in the input directory
    for filename in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, filename)

        # Check if the file is a ciphertext file
        if filename.endswith(".nonce"):
            continue

        # Read ciphertext and nonce from files
        with open(input_file_path, 'rb') as f:
            ciphertext = f.read()

        # Extract nonce from corresponding nonce file
        nonce_filename = filename + ".nonce"
        nonce_file_path = os.path.join(input_folder, nonce_filename)
        with open(nonce_file_path, 'rb') as f:
            nonce = f.read()

        # Decrypt the data using the appropriate key
        if filename[:14] == "plant_house_1_":
            key_file_path = os.path.join(key_folder, "plant_house_1.key")
            with open(key_file_path, 'rb') as f:
                key = f.read()
        if filename[:14] == "plant_house_2_":
            key_file_path = os.path.join(key_folder, "plant_house_2.key")
            with open(key_file_path, 'rb') as f:
                key = f.read()
        if filename[:14] == "plant_house_3_":
            key_file_path = os.path.join(key_folder, "plant_house_3.key")
            with open(key_file_path, 'rb') as f:
                key = f.read()
        if filename[:14] == "plant_house_4_":
            key_file_path = os.path.join(key_folder, "plant_house_4.key")
            with open(key_file_path, 'rb') as f:
                key = f.read()
        if filename[:14] == "plant_house_5_":
            key_file_path = os.path.join(key_folder, "plant_house_5.key")
            with open(key_file_path, 'rb') as f:
                key = f.read()
        if filename[:14] == "plant_house_6_":
            key_file_path = os.path.join(key_folder, "plant_house_6.key")
            with open(key_file_path, 'rb') as f:
                key = f.read()
        if filename[:14] == "plant_house_7_":
            key_file_path = os.path.join(key_folder, "plant_house_7.key")
            with open(key_file_path, 'rb') as f:
                key = f.read()
        if filename[:14] == "plant_house_8_":
            key_file_path = os.path.join(key_folder, "plant_house_8.key")
            with open(key_file_path, 'rb') as f:
                key = f.read()
        if filename[:14] == "plant_house_9_":
            key_file_path = os.path.join(key_folder, "plant_house_9.key")
            with open(key_file_path, 'rb') as f:
                key = f.read()
        if filename[:14] == "plant_house_10":
            key_file_path = os.path.join(key_folder, "plant_house_10.key")
            with open(key_file_path, 'rb') as f:
                key = f.read()

        # Decrypt the data
        decrypted_data = decrypt_data(ciphertext, key, nonce)


        # Save the decrypted data to the output file
        output_file_path = os.path.join(output_folder, filename)
        save_decrypted_data(decrypted_data, output_file_path)

    print("Decryption completed. Decrypted files saved in", output_folder)

start_time = time.time()

# please change to your project directory
decrypt_ciphertext_with_aes_key(r"D:\SIIT Y4\2024\Cyber Crime\Project\EncryptHash")

end_time = time.time()
execution_time = end_time - start_time

print("Execution time:", execution_time, "seconds")

