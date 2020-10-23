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
        print("encrypting")
        encrypted_byte = plain_byte # TODO, encrypt plain_byte
        return encrypted_byte
    
    def decrypt(self, encrypted_byte: bytes) -> bytes:
        print("decrypting")
        plain_byte = encrypted_byte # TODO, decrypt plain_byte
        return plain_byte
        
class AESCipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)
        # TODO
    
    def encrypt(self, plain_byte: bytes) -> bytes:
        print("encrypting", plain_byte)
        encrypted_byte = plain_byte # TODO, encrypt plain_byte
        return encrypted_byte
    
    def decrypt(self, encrypted_byte: bytes) -> bytes:
        print("decrypting")
        plain_byte = encrypted_byte # TODO, decrypt plain_byte
        return plain_byte
        
class RC4Cipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)
        # TODO
    
    def encrypt(self, plain_byte: bytes) -> bytes:
        print("encrypting", plain_byte)
        encrypted_byte = plain_byte # TODO, encrypt plain_byte
        return encrypted_byte
    
    def decrypt(self, encrypted_byte: bytes) -> bytes:
        print("decrypting")
        plain_byte = encrypted_byte # TODO, decrypt plain_byte
        return plain_byte
        
class BlowFishCipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)
        # TODO
    
    def encrypt(self, plain_byte: bytes) -> bytes:
        print("encrypting", plain_byte)
        encrypted_byte = plain_byte # TODO, encrypt plain_byte
        return encrypted_byte
    
    def decrypt(self, encrypted_byte: bytes) -> bytes:
        print("decrypting")
        plain_byte = encrypted_byte # TODO, decrypt plain_byte
        return plain_byte