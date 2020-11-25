import os

# from Crypto.PublicKey import ECC
import rsa

import parameter

from ecies.utils import generate_eth_key, generate_key
from ecies import encrypt, decrypt

private_key_file = "private.pem"
public_key_file = "public.pem"

ecc_folder = "ecc/"
rsa_folder = "rsa/"

curr_dir = "."

key_format = "PEM"
rsa_length = 2048
ecc_curve_type = "P-256"

def remove_keys(name:str = ""):
    folder_dir = os.path.join(curr_dir, name)
    os.system(f"rm -rf {folder_dir}")
    
def generate_key(name: str):
    
    name_folder = os.path.join(curr_dir, f"{name}/")
    
    name_ecc_folder = os.path.join(name_folder, ecc_folder)
    os.makedirs(name_ecc_folder, exist_ok=True)
    
    name_ecc_private_file = os.path.join(name_ecc_folder, private_key_file)
    name_ecc_public_file = os.path.join(name_ecc_folder, public_key_file)
    with open(name_ecc_private_file, "w") as prkf, open(name_ecc_public_file, "w") as pkf:
        key = generate_eth_key()
        # private key
        prkf.write(key.to_hex())
        
        # public key
        pkf.write(key.public_key.to_hex())
        
    name_rsa_folder = os.path.join(name_folder, rsa_folder)
    os.makedirs(name_rsa_folder, exist_ok=True)
    
    name_rsa_private_file = os.path.join(name_rsa_folder, private_key_file)
    name_rsa_public_file = os.path.join(name_rsa_folder, public_key_file)
    with open(name_rsa_private_file, "w") as prkf, open(name_rsa_public_file, "w") as pkf:
        pubkey, privkey = rsa.newkeys(rsa_length)
        # private key
        prkf.write(privkey.save_pkcs1(format=key_format).decode())
        
        # public key
        pkf.write(pubkey.save_pkcs1(format=key_format).decode())

if __name__ == "__main__":
    remove_keys("bob")
    remove_keys("alice")
    
    generate_key("bob")
    generate_key("alice")