import argparse

def run_argparser():
    parser = argparse.ArgumentParser(description='Project help page.')
    parser.add_argument("--directory", required=True, help="The folder or file directory to encrypt.")
    parser.add_argument("--type", required=True, help="Type of encryption. Available: XOR, AES, RC4, Blowfish, RSA, ECC.")
    parser.add_argument("--secrets", required=False, help="(XOR, AES, RC4, Blowfish only)The secret key to encrypt or decrypt.", default="")
    parser.add_argument("--privateKey", required=False, help="(RSA, ECC only)The private key used for signature.", default="")
    parser.add_argument("--publicKey", required=False, help="(RSA, ECC only)The public key used for encryption / decryption.", default="")
    parser.add_argument("--action", required=True, help="encrypt or decrypt.")
    return parser
