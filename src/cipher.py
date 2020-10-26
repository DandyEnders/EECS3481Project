from Crypto.Cipher import Blowfish
from Crypto import Random
from struct import pack
from itertools import cycle

import hashlib
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

import sys


class CipherMethod:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plain_byte: bytes) -> bytes:
        pass

    def decrypt(self, encrypted_byte: bytes) -> bytes:
        pass


class XORCipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)
        self.key = key.encode('utf-8')  # key string to bytes

    def encrypt(self, plain_byte: bytes) -> bytes:
        print("encrypting")
        # plain_int = int.from_bytes(plain_byte, byteorder="big")
        # key_int = int.from_bytes(self.key, byteorder="big")
        # result_int = plain_int ^ key_int
        # result_string = str(result_int)
        # encrypted_byte = result_string.encode('utf-8')
        # return encrypted_byte
        return bytes([_a ^ _b for _a, _b in zip(plain_byte, self.key)])

    def decrypt(self, encrypted_byte: bytes) -> bytes:
        print("decrypting")
        # encrypted_int = int.from_bytes(encrypted_byte, byteorder="big")
        # key_int = int.from_bytes(self.key, byteorder="big")
        # result_int = encrypted_int ^ key_int
        # result_string = str(result_int)
        # plain_byte = result_string.encode('utf-8')
        # return plain_byte
        return bytes([_a ^ _b for _a, _b in zip(encrypted_byte, self.key)])


class AESCipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)
        # TODO

    def encrypt(self, plain_byte: bytes) -> bytes:
        # print("encrypting")
        encrypted_byte = plain_byte  # TODO, encrypt plain_byte
        return encrypted_byte

    def decrypt(self, encrypted_byte: bytes) -> bytes:
        # print("decrypting")
        plain_byte = encrypted_byte  # TODO, decrypt plain_byte
        return plain_byte


class RC4Cipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)
        # TODO

    def encrypt(self, plain_byte: bytes) -> bytes:
        # print("encrypting")
        encrypted_byte = plain_byte  # TODO, encrypt plain_byte
        return encrypted_byte

    def decrypt(self, encrypted_byte: bytes) -> bytes:
        # print("decrypting")
        plain_byte = encrypted_byte  # TODO, decrypt plain_byte
        return plain_byte


class BlowFishCipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)
        self.block_size = Blowfish.block_size
        self.iv = Random.new().read(self.block_size)
        byte_key = str.encode(key)
        byte_key = hashlib.sha256(key.encode()).digest()
        self.cipher = Blowfish.new(byte_key,
                                   Blowfish.MODE_CBC,
                                   self.iv)

    def encrypt(self, plain_byte: bytes) -> bytes:
        # print("encrypting")
        plen = self.block_size - divmod(len(plain_byte), self.block_size)[1]
        padding = [plen]*plen
        padding = pack('b'*plen, *padding)
        encrypted_byte = self.iv + self.cipher.encrypt(plain_byte + padding)
        return encrypted_byte

    def decrypt(self, encrypted_byte: bytes) -> bytes:
        # print("decrypting")
        ciphertext = encrypted_byte
        ciphertext = ciphertext[self.block_size:]
        plain_byte = self.cipher.decrypt(ciphertext)
        last_byte = plain_byte[-1]
        plain_byte = plain_byte[:- (last_byte if type(last_byte)
                                    is int else ord(last_byte))]
        return plain_byte
