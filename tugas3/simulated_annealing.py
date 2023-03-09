
import math
import random

MAX_ITERATION = 1000

def in_conflict(column, row, other_column, other_row):
    if column == other_column:
        return True  
    if row == other_row:
        return True  
    if abs(column - other_column) == abs(row - other_row):
        return True  

    return False

def count_conflicts(board):
    cnt = 0

    for queen in range(0, len(board)):
        for other_queen in range(queen + 1, len(board)):
            if in_conflict(queen, board[queen], other_queen, board[other_queen]):
                cnt += 1

    return cnt


def evaluate_state(board):
    return (len(board) - 1) * len(board) / 2 - count_conflicts(board)


def print_board(board):
    for row in range(len(board)):
        line = ''
        for column in range(len(board)):
            if board[column] == row:
                line += 'Q'
            else:
                line += '-'
        print(line)
    print("")


def init_board(nqueens):
    board = []
    for column in range(nqueens):
        board.append(random.randint(0, nqueens - 1))

    return board

def Simulated_Annealing(board, initialboard):
    i = 0
    temp = 1000
    optimum = (len(board) - 1) * len(board) / 2
    evaluation = [evaluate_state(board)]

    while evaluate_state(board) < optimum:
        i += 1

        if i == MAX_ITERATION:  
            break

        rand_col = random.randint(0, len(board) - 1)
        rand_row = random.randint(0, len(board) - 1)
        new_board = board.copy()
        new_board[rand_col] = rand_row

        board_score = evaluate_state(board)
        new_board_score = evaluate_state(new_board)

        if new_board_score >= board_score:
            board = new_board

        else:
            score_change = new_board_score - board_score
            probability = math.exp(score_change / temp)
            if random.random() < probability:
                board = new_board

        temp *= 0.95
        print(f"Iteration {i}: Evaluation = {evaluate_state(board)}")
        print_board(board)

    if evaluate_state(board) == optimum:
        print(f"\nPuzzle solved using simulated annealing with {i} iteration")

    else:
        print('\nSimulated Annealing can not solve this problem with given maximum iteration')
    
    print('\nInitial State:')
    print_board(initialboard)

    print('\nFinal State:')
    print_board(board)



n_queens = 8
board = init_board(n_queens)
print('\nInitial Board:')
print_board(board)
Simulated_Annealing(board, board)
