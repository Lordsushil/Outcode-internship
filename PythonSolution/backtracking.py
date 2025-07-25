import time
from collections import Counter

def exist(board, word):
    rows, cols = len(board), len(board[0])

    # Early pruning using character counts
    board_count = Counter(c for row in board for c in row)
    word_count = Counter(word)
    if any(word_count[c] > board_count.get(c, 0) for c in word_count):
        return False

    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
            return False

        temp = board[r][c]
        board[r][c] = "#"

        found = (dfs(r + 1, c, i + 1) or
                 dfs(r - 1, c, i + 1) or
                 dfs(r, c + 1, i + 1) or
                 dfs(r, c - 1, i + 1))

        board[r][c] = temp
        return found

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0] and dfs(i, j, 0):
                return True

    return False

test_cases = [
    ([
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ], "ABCCEDASF"),

    ([
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ], "SEE"),

    ([
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ], "ABCB"),
]

for idx, (board, word) in enumerate(test_cases, 1):
    start_time = time.time()
    result = exist(board, word)
    end_time = time.time()
    duration = end_time - start_time

    print(f"Test Case {idx}:")
    print(f"Word: {word}")
    print(f"Result: {result}")
    print(f"Time Taken: {duration:.6f} seconds\n")
