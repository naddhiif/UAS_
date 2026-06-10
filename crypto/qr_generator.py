import qrcode
import os
import json


def generate_qr(ciphertext, signature):

    folder = "static/qr"

    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = "cipher_qr.png"

    path = os.path.join(folder, filename)

    qr_data = {
        "ciphertext": ciphertext,
        "signature": signature
    }

    img = qrcode.make(json.dumps(qr_data))

    img.save(path)

    return filename