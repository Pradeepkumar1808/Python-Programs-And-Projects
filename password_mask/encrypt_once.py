from password_utils import encrypted_password
from cryptography.fernet import Fernet

def generate_key():
    key=Fernet.generate_key()
    with open("Secret.key",'wb') as f:
        f.write(key)
    print("Key has been generated to Secret.key")
if __name__ == "__main__":
   ## generate_key()

    encrypted=encrypted_password("root")
    print("Copy this to password_utils")
    print(encrypted)



