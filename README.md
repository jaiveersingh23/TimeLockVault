# RSA Time-Lock Encryption

This project implements a secure document sharing system using RSA-based time-lock puzzles.

## Features
- AES encryption for file security.
- RSA-based time-lock puzzles to enforce delayed decryption.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run the application: `python main.py`

## How It Works
1. **Encryption Phase**:
   - The file is encrypted with AES.
   - A time-lock puzzle is generated using modular arithmetic.

2. **Decryption Phase**:
   - The puzzle must be solved to retrieve the decryption key.

## Tests
Coming soon!
