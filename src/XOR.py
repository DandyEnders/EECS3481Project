import input_argparser
from input_argparser import run_argparser

#Check that user is in list of symmetric tasks, and that XOR is selected.
# and (action == "SYMMETRIC" or "symmetric")):
if (type == "XOR" or "xor"): 
    def xor_crypt(file, type, secrets, action):
        if action == "encrypt" or "ENCRYPT":
            key = secrets
            with open(file, 'r') as input_file: #reading file and iterating through its lines
                text_line = input_file.readlines()
                for text_line in input_file:
                    input_file = (input_file[:text_line] + chr(ord(input_file[text_line]) ^ ord(key)) + input_file[text_line + 1:])
                    print(input_file[text_line], end = "")
                return input_file
