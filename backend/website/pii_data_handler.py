"""
Fernet uses the AES (Advanced Encryption Standard) algorithm in CBC (Cipher Block Chaining)
mode with a 128-bit key for encryption and decryption. It also uses HMAC (Hash-based Message Authentication Code)
for message authentication.

The keys used by Fernet are derived from a base64-encoded 32-byte key, which is generated randomly and securely.
"""

import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

this_directory = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(this_directory, "../.env"))

key = os.environ.get("ENCRYPTION_KEY")
cipher_suite = Fernet(key)


def encrypt_data(unencrypted_data: str) -> str:
    data_bytes = unencrypted_data.encode("utf-8")

    return cipher_suite.encrypt(data_bytes)


def decrypt_data(encrypted_data: str) -> str:

    return cipher_suite.decrypt(encrypted_data).decode("utf-8")
