import argparse

import os

curr_dir = "./keys/"
key_format = "pem"

def run_argparser():
    parser = argparse.ArgumentParser(description='Project help page.')
    parser.add_argument("--name", required=True, help="Name of person. (ex. alice, bob)")
    parser.add_argument("--kind", required=True, help="kind of key. (ex. ECC, RSA)")
    parser.add_argument("--type", required=True, help="Type of key. (ex. public, private)")
    return parser

def get_keys(p_name: str, p_kind: str, p_type: str):
    l_name = p_name.lower()
    l_kind = p_kind.lower()
    l_type = p_type.lower()
    
    file_dir = os.path.join(curr_dir, f"{l_name}/", f"{l_kind}/", f"{l_type}.{key_format}")
    with open(file_dir, "r") as f:
        result = f.read()
    return result


if __name__ == "__main__":
    argv = run_argparser().parse_args()
    print(get_keys(argv.name, argv.kind, argv.type))