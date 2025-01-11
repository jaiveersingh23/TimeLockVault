def solve_puzzle(N, g, x, iterations):
    result = x
    for _ in range(iterations):
        result = pow(result, 2, N)
    return result
