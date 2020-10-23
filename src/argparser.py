import argparse

# --folder : The folder that will be used for encryption
# --type: gets to values of “sym” and “asym” for symmetric and asymmetric algorithm selection
# --secrets: an n-tuple input used for secrets such as keys, and other important parameters needed for the crypto scheme, e.g. algorithm itself. Feel free to define sub-parameters if needed.
# --action: decrypt or encrypt

def run_argparser():
    parser = argparse.ArgumentParser(description='Project help page.')
    parser.add_argument("--directory", required=True, help="The folder or file directory to encrypt.")
    parser.add_argument("--type", required=True, help="Type of encryption. Available: XOR, AES, RC4, Blowfish.")
    parser.add_argument("--secrets", required=True, help="The secret key to encrypt or decrypt.")
    parser.add_argument("--action", required=True, help="encrypt or decrypt.")
    return parser
    #args = parser.parse_args()

# parser.add_argument('integers', metavar='N', type=int, nargs='+', 
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,

#                     help='sum the integers (default: find the max)')