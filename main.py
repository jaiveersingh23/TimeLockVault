from encryption.encrypt import encrypt_file
from encryption.decrypt import decrypt_file
from puzzle.puzzle_generator import generate_puzzle
from puzzle.puzzle_solver import solve_puzzle
import os

def main():
    print("Welcome to RSA Time-Lock Encryption!")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

    if mode == "encrypt":
        input_file = input("Enter the path of the file to encrypt: ")
        output_file = input("Enter the output encrypted file path: ")
        password = input("Enter a password: ")

        # Encrypt file
        encrypt_file(input_file, output_file, password)

        # Generate time-lock puzzle
        bits = 512
        iterations = 100000
        N, g, x, puzzle, iterations = generate_puzzle(bits, iterations)
        print(f"Puzzle generated. Puzzle result: {puzzle}, Iterations: {iterations}")
        print(f"RSA Modulus (N): {N}")

    elif mode == "decrypt":
        input_file = input("Enter the path of the encrypted file: ")
        output_file = input("Enter the output decrypted file path: ")
        password = input("Enter a password: ")
        N = int(input("Enter RSA modulus (N): "))
        g = int(input("Enter generator (g): "))
        x = int(input("Enter initial value (x): "))
        iterations = int(input("Enter iterations: "))

        # Solve puzzle
        puzzle_result = solve_puzzle(N, g, x, iterations)
        print(f"Puzzle solved! Result: {puzzle_result}")

        decrypt_file(input_file, output_file, password)
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
