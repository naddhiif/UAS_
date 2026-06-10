from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# kunci AES 32 byte = AES-256
KEY = b'12345678901234567890123456789012'


def pad(data):
    while len(data) % 16 != 0:
        data += ' '
    return data


def encrypt_message(message):
    cipher = AES.new(KEY, AES.MODE_ECB)
    padded_message = pad(message)
    encrypted_bytes = cipher.encrypt(padded_message.encode())
    return base64.b64encode(encrypted_bytes).decode()


def decrypt_message(ciphertext):
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted_bytes = base64.b64decode(ciphertext)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    return decrypted_bytes.decode().rstrip()