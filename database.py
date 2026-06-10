import sqlite3
from datetime import datetime


def init_db():

    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pengirim TEXT,
            penerima TEXT,
            pesan TEXT,
            ciphertext TEXT,
            hash_value TEXT,
            signature TEXT,
            waktu TEXT
        )
    ''')

    conn.commit()
    conn.close()


def save_data(
    pengirim,
    penerima,
    pesan,
    ciphertext,
    hash_value,
    signature
):

    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()

    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute('''
        INSERT INTO history(
            pengirim,
            penerima,
            pesan,
            ciphertext,
            hash_value,
            signature,
            waktu
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        pengirim,
        penerima,
        pesan,
        ciphertext,
        hash_value,
        signature,
        waktu
    ))

    conn.commit()
    conn.close()


def get_history():

    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM history ORDER BY id DESC")

    data = cursor.fetchall()

    conn.close()

    return data