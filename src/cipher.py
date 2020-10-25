from Crypto.Cipher import Blowfish
from Crypto import Random
from struct import pack
from arc4 import ARC4

import hashlib
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

import Crypto
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad

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
        # TODO

    def encrypt(self, plain_byte: bytes) -> bytes:
        encrypted_byte = plain_byte  # TODO, encrypt plain_byte
        return encrypted_byte

    def decrypt(self, encrypted_byte: bytes) -> bytes:
        plain_byte = encrypted_byte  # TODO, decrypt plain_byte
        return plain_byte


class AESCipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)
        self.block_size = AES.block_size
        self.byte_key = hashlib.sha256(key.encode()).digest()
        self.iv = (" " * self.block_size).encode()

    def encrypt(self, plain_byte: bytes) -> bytes:
        encrypter = AES.new(self.byte_key, AES.MODE_CBC, iv=self.iv)
        encrypted_byte = encrypter.encrypt(pad(plain_byte, self.block_size))
        return encrypted_byte

    def decrypt(self, encrypted_byte: bytes) -> bytes:
        decrypter = AES.new(self.byte_key, AES.MODE_CBC, iv=self.iv)
        plain_byte = unpad(decrypter.decrypt(encrypted_byte), self.block_size)
        return plain_byte


class RC4Cipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)

    def encrypt(self, plain_byte: bytes) -> bytes:
        arc4 = ARC4(self.key.encode())
        encrypted_byte = arc4.encrypt(plain_byte) 
        return encrypted_byte

    def decrypt(self, encrypted_byte: bytes) -> bytes:
        arc4 = ARC4(self.key.encode())
        plain_byte = arc4.decrypt(encrypted_byte)
        return plain_byte


class BlowFishCipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)
        self.block_size = Blowfish.block_size
        self.byte_key = hashlib.sha256(key.encode()).digest()
        self.iv = (" " * self.block_size).encode()
        
    def encrypt(self, plain_byte: bytes) -> bytes:
        encrypter = Blowfish.new(self.byte_key, Blowfish.MODE_CBC, iv=self.iv)
        encrypted_byte = encrypter.encrypt(pad(plain_byte, self.block_size))
        return encrypted_byte

    def decrypt(self, encrypted_byte: bytes) -> bytes:
        decrypter = Blowfish.new(self.byte_key, Blowfish.MODE_CBC, iv=self.iv)
        plain_byte = unpad(decrypter.decrypt(encrypted_byte), self.block_size)
        return plain_byte
