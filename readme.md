pip the requirement via

pip install -r requirements.txt

Extract the "plant_house_logs.rar" into the same directory running on python

Run the program according to the name respectively

Phase 1: MOAC verify every individual key pair.--------

python keygen_planthouse.py
    - This will generate public key and private key for each planthouse (This project is working with 10 planthouses.)
    - The planthouse key pairs will save to "keygen_planthouse_logs" folder

python keygen_user.py
    - This will generate public key and private key of the user (We assume 1 user has the access to the plaintext data)
    - The user key pair will save to "keygen_user_logs" folder

python keygen_moac.py
    - This will generate public key and private key of the MOAC (MOAC = Master of All Cluster)
    - The MOAC key pair will save to "keygen_moac_logs" folder

Phase 2: Encryption of sensors inside the planthouse.------

python ph_1_aes_encrypt.py
    - This will generate the random 16 bit session key using PRNG that belongs to each planthouse. (10 plant houses = 10 different PRNG keys)
    - The PRNG key will save to "aes_keys_logs" folder

    - This will use the generated session key to encrypt each planthouse plaintext.
    - The planthouse ciphertext data will save to "ciphertext_logs" folder

    - Please fix the input of the file in line 31: 
    input_folder = "plant_house_logs_{no of sensor}"

python ph_2_hash_digest.py
    - This will hash the ecc_session key to message digests
    - The hash will save to "hash_plant_house_logs_400" folder

python ph_4_sign.py
    - This will sign the hash key using the public key of the MOAC to generte Digital Signature of each planthouse hash
    - The digital signature will save to "enc_d_sign_logs" folder


Phase 5: User data retrieval.------------

python user_2_aes_decrypt.py
    - The decrypted prng_key will be decrypted with the same prng_key accessed earlier in the first phase
    - The user gets the same plaintext back.
    The retreived plaintext will save to "Retrieved_PT_{date}" folder

THE END...





