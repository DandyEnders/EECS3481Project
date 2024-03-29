from Crypto.Cipher import Blowfish
from Crypto import Random
from struct import pack
from arc4 import ARC4
from itertools import cycle

import hashlib
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

import Crypto
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import ECC

from abc import ABC, abstractmethod

import rsa
# from ecies import encrypt, decrypt
import ecies

class CipherMethod(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def encrypt(self, plain_byte: bytes) -> bytes:
        pass

    @abstractmethod
    def decrypt(self, encrypted_byte: bytes) -> bytes:
        pass


class XORCipher(CipherMethod):
    def __init__(self, key):
        self.key = key
        self.key = key.encode('utf-8')

    def encrypt(self, plain_byte: bytes) -> bytes:
        return bytes([_a ^ _b for _a, _b in zip(plain_byte, cycle(self.key))])

    def decrypt(self, encrypted_byte: bytes) -> bytes:
        return bytes([_a ^ _b for _a, _b in zip(encrypted_byte, cycle(self.key))])

class AESCipher(CipherMethod):
    def __init__(self, key):
        self.key = key
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
        self.key = key

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
        self.key = key
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
    
class ECCCipher(CipherMethod):
    def __init__(self, sender_private_key, receiver_public_key):
        self.aes_key = b'D\xfb+Q\x16\xae\xc0\xaa\x11&\xed\xc0`\xd2\xcb\x14'
        self.sender_private_key = sender_private_key
        self.receiver_public_key = receiver_public_key
        
    def encrypt(self, plain_byte: bytes) -> bytes:
        encrypted_aes_key = ecies.encrypt(self.receiver_public_key, self.aes_key)
        symmetric_encrypt_cipher = NoEncodeAESCipher(self.aes_key)
        
        encrypted_byte = symmetric_encrypt_cipher.encrypt(plain_byte)
        return encrypted_byte, encrypted_aes_key

    def decrypt(self, encrypted_byte: bytes, encrypted_aes_key: bytes) -> bytes:
        decrypted_aes_key = ecies.decrypt(self.sender_private_key, encrypted_aes_key)
        
        symmetric_decrypt_cipher = NoEncodeAESCipher(decrypted_aes_key)
        
        plain_byte = symmetric_decrypt_cipher.decrypt(encrypted_byte)
        return plain_byte

class RSACipher:
    def __init__(self, sender_private_key, receiver_public_key):
        self.aes_key = b'D\xfb+Q\x16\xae\xc0\xaa\x11&\xed\xc0`\xd2\xcb\x14'
        self.sender_private_key = rsa.PrivateKey.load_pkcs1(sender_private_key.encode())
        self.receiver_public_key = rsa.PublicKey.load_pkcs1(receiver_public_key.encode())

    def encrypt(self, plain_byte: bytes) -> bytes:
        encrypted_aes_key = rsa.encrypt(self.aes_key, self.receiver_public_key)
        symmetric_encrypt_cipher = NoEncodeAESCipher(self.aes_key)
        
        encrypted_byte = symmetric_encrypt_cipher.encrypt(plain_byte)
        return encrypted_byte, encrypted_aes_key

    def decrypt(self, encrypted_byte: bytes, encrypted_aes_key: bytes) -> bytes:
        decrypted_aes_key = rsa.decrypt(encrypted_aes_key, self.sender_private_key)
        
        symmetric_decrypt_cipher = NoEncodeAESCipher(decrypted_aes_key)
        
        plain_byte = symmetric_decrypt_cipher.decrypt(encrypted_byte)
        return plain_byte
    
class NoEncodeAESCipher(CipherMethod):
    def __init__(self, byteKey):
        self.byteKey = byteKey
        self.block_size = AES.block_size
        self.byte_key = hashlib.sha256(byteKey).digest()
        self.iv = (" " * self.block_size).encode()

    def encrypt(self, plain_byte: bytes) -> bytes:
        encrypter = AES.new(self.byte_key, AES.MODE_CBC, iv=self.iv)
        encrypted_byte = encrypter.encrypt(pad(plain_byte, self.block_size))
        return encrypted_byte

    def decrypt(self, encrypted_byte: bytes) -> bytes:
        decrypter = AES.new(self.byte_key, AES.MODE_CBC, iv=self.iv)
        plain_byte = unpad(decrypter.decrypt(encrypted_byte), self.block_size)
        return plain_byte

