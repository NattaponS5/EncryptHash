# EncryptHash

This repository contains a comprehensive setup for preparing and storing data in a blockchain, including key generation, encryption, hashing, and decryption processes. Follow the steps below to prepare your data for storage.

## Prerequisites

### Install Required Python Packages
Ensure you have the necessary Python packages installed:
```sh
pip install -r requirements.txt
```

## Data Preparation Steps

### Step 0: Navigate to the Project Directory
```sh
cd EncryptHash
```

### Phase 1: MOAC Verify Every Individual Key Pair

#### 1. Generate Key Pairs for Each Plant House
```sh
python keygen_planthouse.py
```
- **Output**: Generates public and private key pairs for each plant house (10 plant houses).
- **Saved To**: `keygen_planthouse_logs_{set}` folder.

#### 2. Generate Key Pair for the User
```sh
python keygen_user.py
```
- **Output**: Generates public and private key pairs for the user.
- **Saved To**: `keygen_user_logs_{set}` folder.

#### 3. Generate Key Pair for the MOAC
```sh
python keygen_moac.py
```
- **Output**: Generates public and private key pairs for the MOAC (Master of All Cluster).
- **Saved To**: `keygen_moac_logs_{set}` folder.

### Phase 2: Encryption of Sensors Inside the Plant House

#### 1. Generate and Encrypt Session Keys
```sh
python ph_1_aes_encrypt.py
```
- **Output**: Generates a random 16-bit session key using PRNG for each plant house (10 different PRNG keys).
- **Saved To**: `aes_keys_logs_{set}` folder.
- **Encrypted Data**: Encrypts each plant house plaintext using the generated session key.
- **Saved To**: `ciphertext_logs_{set}` folder.
- **Note**: Fix the input folder in line 31:
  ```python
  input_folder = "plant_house_logs_{no of sensor}"
  ```

#### 2. Generate Hash Digests
```sh
python ph_2_hash_digest.py
```
- **Output**: Hashes the plaintext to message digests.
- **Saved To**: `hash_plant_house_logs_400_{set}` folder.

#### 3. Encrypt PRNG Keys Using ECC
```sh
python ph_3_ecc_enckey.py
```
- **Output**: Encrypts each house PRNG keys using ECC.
- **Saved To**: `enc_aes_key_logs_{set}` folder.

#### 4. Generate Digital Signatures
```sh
python ph_4_sign.py
```
- **Output**: Signs the hash key using the public key of the MOAC to generate digital signatures for each plant house hash.
- **Saved To**: `enc_d_sign_logs_{set}` folder.

### Phase 3: User Data Retrieval

#### 1. Decrypt PRNG Keys
```sh
python user_1_ecc_decrypt.py
```
- **Output**: Decrypts the PRNG key to the default aes_key.
- **Saved To**: `dec_aes_key_logs_{set}` folder.

#### 2. Decrypt Ciphertext to Plaintext
```sh
python user_2_aes_decrypt.py
```
- **Output**: Decrypts the PRNG Key with the same PRNG key accessed earlier in the first phase.
- **Retrieved Plaintext**: The user gets the same plaintext back.
- **Saved To**: `Retrieved_PT_{date}` folder.

## Conclusion
This setup allows you to prepare your data for storage in a blockchain by generating key pairs, encrypting data, hashing plaintext, and decrypting data for retrieval. Follow the steps above to ensure your data is securely prepared and stored.