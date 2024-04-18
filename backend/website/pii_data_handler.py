"""
Fernet uses the AES (Advanced Encryption Standard) algorithm in CBC (Cipher Block Chaining)
mode with a 128-bit key for encryption and decryption. It also uses HMAC (Hash-based Message Authentication Code)
for message authentication.

The keys used by Fernet are derived from a base64-encoded 32-byte key, which is generated randomly and securely.
"""

import base64
import os

from cryptography.fernet import Fernet
from dotenv import load_dotenv

this_directory = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(this_directory, "../.env"))

key = os.environ.get("ENCRYPTION_KEY")
cipher = Fernet(key)


def encrypt_data(unencrypted_data: str) -> str:
    # Encrypt the provided data
    encrypted_data = cipher.encrypt(unencrypted_data.encode("utf-8"))

    # Convert encrypted data to a string
    encrypted_string = base64.b64encode(encrypted_data).decode("utf-8")

    return encrypted_string


def decrypt_data(encrypted_string: str) -> str:

    # Decode the Base64 string
    encrypted_data = base64.b64decode(encrypted_string)

    # Decrypt the data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Convert decrypted bytes to string (assuming it was originally a string)
    plaintext = decrypted_data.decode("utf-8")

    return plaintext


if __name__ == "__main__":
    string_to_encrypt = "encrypt me"

    encrypted_data = encrypt_data(string_to_encrypt)

    print(encrypted_data)
    print(type(encrypted_data))

    decrypted_data = decrypt_data(encrypted_data)

    print(decrypted_data)

    string_to_encrypt = "encrypt me"

    encrypted_data = encrypt_data(string_to_encrypt)

    print(encrypted_data)
    print(type(encrypted_data))

    decrypted_data = decrypt_data(encrypted_data)

    print(decrypted_data)
