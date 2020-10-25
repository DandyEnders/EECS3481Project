import argparse

def run_argparser():
    parser = argparse.ArgumentParser(description='Project help page.')
    parser.add_argument("--directory", required=True, help="The folder or file directory to encrypt.")
    parser.add_argument("--type", required=True, help="Type of encryption. Available: XOR, AES, RC4, Blowfish.")
    parser.add_argument("--secrets", required=True, help="The secret key to encrypt or decrypt.")
    parser.add_argument("--action", required=True, help="encrypt or decrypt.")
    return parser
