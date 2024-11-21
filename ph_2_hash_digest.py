# 5 create folder hash_plant_house_logs_400

import os
import hashlib
import time

def hash_file(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(65536)  # Read in 64k chunks
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def hash_files_in_directory(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    hashes = {}
    for filename in os.listdir(input_directory):
        file_path = os.path.join(input_directory, filename)
        if os.path.isfile(file_path):
            file_hash = hash_file(file_path)
            hashes[filename] = file_hash
            output_file_path = os.path.join(output_directory, f"{filename}.hash")
            with open(output_file_path, 'w') as f:
                f.write(file_hash)
    return hashes
start_time = time.time()
input_directory = "plant_house_logs_400_9"
output_directory = "hash_plant_house_logs_400_9"
file_hashes = hash_files_in_directory(input_directory, output_directory)

for filename, file_hash in file_hashes.items():
    print(f"Hash of {filename}: {file_hash}")

end_time = time.time()
execution_time = end_time - start_time

print("Execution time:", execution_time, "seconds")
