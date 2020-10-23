class CipherMethod:
    def __init__(self, key):
        self.key = key
    
    def encrypt(self, plain_byte):
        pass
    
    def decrypt(self, encrypted_byte):
        pass

class XORCipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)
        # TODO
    
    def encrypt(self, plain_byte):
        print("encrypting", plain_byte) # TODO
    
    def decrypt(self, encrypted_byte):
        print("decrypting", encrypted_byte) # TODO
        

class AESCipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)
        # TODO
    
    def encrypt(self, plain_byte):
        print("encrypting", plain_byte) # TODO
    
    def decrypt(self, encrypted_byte):
        print("decrypting", encrypted_byte) # TODO
        
class RC4Cipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)
        # TODO
    
    def encrypt(self, plain_byte):
        print("encrypting", plain_byte) # TODO
    
    def decrypt(self, encrypted_byte):
        print("decrypting", encrypted_byte) # TODO
        
class BlowFishCipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)
        # TODO
    
    def encrypt(self, plain_byte):
        print("encrypting", plain_byte) # TODO
    
    def decrypt(self, encrypted_byte):
        print("decrypting", encrypted_byte) # TODO