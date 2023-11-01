from sys import argv


# Function to check if the position is safe for a queen
def is_safe(board, row, col):
    # Check left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


# Function to solve N Queens problem
def solve_nqueens(N):
    # Initialize the chessboard
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    return solutions


# Utility function to solve N Queens problem using backtracking
def solve_nqueens_util(board, col, solutions):
    # If all queens are placed, add the solution
    if col == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, solutions) or res
            board[i][col] = 0

    return res


if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)

if not argv[1].isdigit():
    print('N must be a number')
    exit(1)

N = int(argv[1])

if N < 4:
    print('N must be at least 4')
    exit(1)

solutions = solve_nqueens(N)
for sol in solutions:
    print(sol)
