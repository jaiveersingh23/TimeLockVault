from puzzle import generate_puzzle, solve_puzzle

def test_puzzle_generation_and_solving():
    bits = 512
    iterations = 1000  # Reduced for testing
    N, g, x, puzzle, iters = generate_puzzle(bits, iterations)

    # Ensure valid values are generated
    assert N > 0
    assert g > 0
    assert x > 0
    assert puzzle > 0
    assert iters == iterations

    # Solve the puzzle
    solved_puzzle = solve_puzzle(N, g, x, iters)

    # Verify the solution matches the expected result
    assert solved_puzzle == puzzle

    print("Puzzle generation and solving test passed.")
