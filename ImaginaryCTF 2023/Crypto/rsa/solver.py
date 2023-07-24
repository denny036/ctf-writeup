from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from base64 import b64decode

def decrypt_flag():
    # Load the private key from the private.pem file
    with open("private.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    # Read the base64-encoded ciphertext from flag.enc
    with open("flag.enc", "r") as flag_file:
        encoded_ciphertext = flag_file.read()

    # Decode the base64-encoded ciphertext to bytes
    encrypted_flag = b64decode(encoded_ciphertext)

    # Decrypt the flag using the private key
    decrypted_flag = private_key.decrypt(
        encrypted_flag,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    print("Decrypted Flag:", decrypted_flag.decode())

if __name__ == "__main__":
    decrypt_flag()
