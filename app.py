from flask import Flask, render_template, request
from rc4 import RC4  # Modul untuk implementasi algoritma RC4

app = Flask(__name__)

# Fungsi untuk enkripsi teks menggunakan algoritma RC4
def encrypt_text(key, plaintext):
    cipher = RC4(key)
    return cipher.encrypt(plaintext)

# Fungsi untuk dekripsi teks menggunakan algoritma RC4
def decrypt_text(key, ciphertext):
    cipher = RC4(key)
    return cipher.decrypt(ciphertext)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    key = request.form['key']
    text = request.form['text']
    action = request.form['action']

    if action == 'encrypt':
        result_text = encrypt_text(key, text)
    else:
        result_text = decrypt_text(key, text)

    return render_template('result.html', result=result_text)

if __name__ == '__main__':
    app.run(debug=True)
