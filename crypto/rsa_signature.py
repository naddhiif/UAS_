from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import os


PRIVATE_KEY_PATH = "keys/private.pem"
PUBLIC_KEY_PATH = "keys/public.pem"


def generate_keys():

    if os.path.exists(PRIVATE_KEY_PATH):
        return

    key = RSA.generate(2048)

    with open(PRIVATE_KEY_PATH, "wb") as f:
        f.write(key.export_key())

    with open(PUBLIC_KEY_PATH, "wb") as f:
        f.write(key.publickey().export_key())


def sign_message(message):

    with open(PRIVATE_KEY_PATH, "rb") as f:
        private_key = RSA.import_key(f.read())

    h = SHA256.new(message.encode())

    signature = pkcs1_15.new(private_key).sign(h)

    return signature.hex()


def verify_signature(message, signature_hex):

    with open(PUBLIC_KEY_PATH, "rb") as f:
        public_key = RSA.import_key(f.read())

    h = SHA256.new(message.encode())

    try:
        pkcs1_15.new(public_key).verify(
            h,
            bytes.fromhex(signature_hex)
        )
        return True

    except:
        return False