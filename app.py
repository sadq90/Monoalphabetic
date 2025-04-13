from flask import Flask, render_template, request
import os
import random

app = Flask(__name__)

# المفتاح الخاص بالتشفير الأحادي (تقدر تغيّره حسب رغبتك)
original_alphabet = 'abcdefghijklmnopqrstuvwxyz'
substitution_alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'.lower()

def monoalphabetic_encrypt(plaintext):
    encrypted = ''
    for char in plaintext.lower():
        if char in original_alphabet:
            index = original_alphabet.index(char)
            encrypted += substitution_alphabet[index]
        else:
            encrypted += char  # غير الحروف تُترك كما هي
    return encrypted

@app.route('/', methods=['GET', 'POST'])
def index():
    encrypted_text = ''
    if request.method == 'POST':
        plaintext = request.form['plaintext']
        encrypted_text = monoalphabetic_encrypt(plaintext)
    return render_template('index.html', encrypted=encrypted_text)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
