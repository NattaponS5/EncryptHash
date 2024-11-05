import os
import hashlib

# Duplication Check: HashSet-Based Duplication Check

# check duplication content at dataPath
data_path = os.path.join(os.path.dirname(__file__), '../../CyberProject/plant_house_logs_400')
# list files in dataPath
# for file in os.listdir(data_path):
#     print(file)

duplicate_files = {}

def calculate_file_hash(file):
    # Calculate the SHA256 hash of the file content
    with open(file, 'rb') as f: 
        # Read the first line and extract the sensor data
        first_line = f.readline()
        key = first_line.decode('utf-8').split(":")[1].strip()
        # Use the key in the PRNG to generate a random encryption key
        encryption_key = hashlib.sha256(key.encode()).hexdigest()
        # Read the remaining content
        content = f.read()
        # Hash the content using SHA256
        file_hash = hashlib.sha256(f'{encryption_key} + {content}'.encode()).hexdigest()
    return file_hash

def find_duplicates(data_path):
    file_hashes = {}
    for root, _, files in os.walk(data_path):
        for file in files:
            full_path = os.path.join(root, file)
            file_hash = calculate_file_hash(full_path)
            if file_hash in file_hashes:
                if file_hash not in duplicate_files:
                    duplicate_files[file_hash] = [file_hashes[file_hash]]
                duplicate_files[file_hash].append(full_path)
            else:
                file_hashes[file_hash] = full_path
    return duplicate_files

duplicates = find_duplicates(data_path)
if duplicates:
    print("Duplicate files found:")
    for file_hash, files in duplicates.items():
        print(f"Files with hash {file_hash}:")
        for file in files:
            print(f"{os.path.basename(file)}")
else:
    print("No duplicate files found.")