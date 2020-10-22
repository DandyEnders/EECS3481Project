import sys
from src import argparser

# The ransomware agent should be able to encrypt and decrypt file contents using the command line. 
# The command line should receive the following argument options:

# --folder : The folder that will be used for encryption
# --type: gets to values of “sym” and “asym” for symmetric and asymmetric algorithm selection
# --secrets: an n-tuple input used for secrets such as keys, and other important parameters needed for the crypto scheme, e.g. algorithm itself. Feel free to define sub-parameters if needed.
# --action: decrypt or encrypt

def main(filename: str, encrypt_type: str, secrets: str, action: str):
    print(f"{filename}, {encrypt_type}, {secrets}, {action}")
    

if __name__ == "__main__":
    argv = argparser.run_argparser().parse_args()
    main(argv.file, argv.type, argv.secrets, argv.action)
    