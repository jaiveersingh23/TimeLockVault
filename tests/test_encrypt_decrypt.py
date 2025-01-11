import os
from encryption import encrypt_file, decrypt_file

def test_encryption_and_decryption():
    input_file = "test_input.txt"
    encrypted_file = "test_encrypted.enc"
    decrypted_file = "test_decrypted.txt"
    password = "securepassword"

    # Create a test input file
    with open(input_file, "w") as f:
        f.write("This is a test file for encryption and decryption.")

    try:
        # Encrypt the file
        encrypt_file(input_file, encrypted_file, password)

        # Ensure the encrypted file exists and is not empty
        assert os.path.exists(encrypted_file)
        assert os.path.getsize(encrypted_file) > 0

        # Decrypt the file
        decrypt_file(encrypted_file, decrypted_file, password)

        # Ensure the decrypted file exists and matches the original content
        with open(decrypted_file, "r") as f:
            decrypted_content = f.read()

        with open(input_file, "r") as f:
            original_content = f.read()

        assert decrypted_content == original_content

        print("Encryption and decryption test passed.")
    finally:
        # Clean up test files
        for file in [input_file, encrypted_file, decrypted_file]:
            if os.path.exists(file):
                os.remove(file)
