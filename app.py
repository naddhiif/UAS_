from flask import Flask, render_template, request, send_file
from crypto.aes_crypto import encrypt_message, decrypt_message
from crypto.hashing import generate_hash
from crypto.rsa_signature import (
    generate_keys,
    sign_message,
    verify_signature
)
from crypto.pdf_generator import create_pdf
from database import init_db, save_data, get_history
from crypto.qr_generator import generate_qr

app = Flask(__name__)

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':

      pengirim = request.form['pengirim']
      penerima = request.form['penerima']
      pesan = request.form['pesan']

      ciphertext = encrypt_message(pesan)
      plaintext = decrypt_message(ciphertext)

      hash_value = generate_hash(pesan)
      generate_keys()
      signature = sign_message(pesan)
      status = verify_signature(pesan, signature)
      qr_file = generate_qr(ciphertext, signature)

      save_data(
         pengirim,
         penerima,
         pesan,
         ciphertext,
         hash_value,
         signature
      )

      create_pdf(
         pengirim,
         penerima,
         pesan,
         ciphertext,
         plaintext,
         hash_value,
         signature,
         qr_file
      )

      return render_template(
         'response.html', 
         pengirim=pengirim, 
         penerima=penerima, 
         pesan=pesan, 
         ciphertext=ciphertext, 
         plaintext=plaintext,
         hash_value=hash_value,
         signature=signature,
         status=status,
         qr_file=qr_file
      )
   return render_template('form.html')

@app.route('/history')
def history():

    data = get_history()

    return render_template(
        'history.html',
        data=data
    )

@app.route('/download-pdf')
def download_pdf():

    return send_file(
        "hasil_enkripsi.pdf",
        as_attachment=True
    )

if __name__ == '__main__':
   app.run(debug=True)
