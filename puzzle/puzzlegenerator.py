from sympy import randprime
import time

def generate_puzzle(bits=512, iterations=100000):
    p = randprime(2**(bits//2), 2**(bits//2 + 1))
    q = randprime(2**(bits//2), 2**(bits//2 + 1))
    N = p * q
    g = randprime(2, N)
    x = randprime(2, N)
    
    # Compute g^(2^iterations) mod N
    start = time.time()
    result = x
    for _ in range(iterations):
        result = pow(result, 2, N)
    end = time.time()
    print(f"Time-lock puzzle generated in {end - start:.2f} seconds.")

    return N, g, x, result, iterations
