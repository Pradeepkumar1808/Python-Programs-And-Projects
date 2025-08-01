from cryptography.fernet import Fernet
class Fakestr(str):
    def __str__(self):
        return '****'
    def __repr__(self):
        return '******'
def load_key():
    return open("Secret.key","rb").read()
def encrypted_password(password):
    key=load_key()
    f=Fernet(key)
    return f.encrypt(password.encode())

def decrypted_password():
    key = load_key()
    f = Fernet(key)
    decrypted=f.decrypt(encrypted_password()).decode()
    return Fakestr(decrypted)

def get_decrypt_password():
    encrypted_password=b'gAAAAABoY8UDY3VZf0WeCwEHvqzwx5RcpVuLrl2HFfC7kr5cCkwv6_YwG0mJK2nbVjhHPy49bHVx1ug_6e_WamtIaAtxEnnkew=='
    return decrypted_password(encrypted_password)