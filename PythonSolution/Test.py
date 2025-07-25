def shortestPathBinaryMatrix(grid):
    n = 3  

    
    if grid[0][0] != 0 or grid[2][2] != 0:
        return -1


    directions = [(-1, -1), (-1, 0), (-1, 1),
                  ( 0, -1),          ( 0, 1),
                  ( 1, -1), ( 1, 0), ( 1, 1)]

    queue = [(0, 0, 1)]  # row, col, path_length
    visited = [[False]*3 for _ in range(3)]
    visited[0][0] = True

    while queue:
        r, c, dist = queue.pop(0)

        if r == 2 and c == 2:
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < 3 and 0 <= nc < 3 and not visited[nr][nc] and grid[nr][nc] == 0:
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))

    return -1


# Example 3x3 grid
grid = [
    [0, 1, 0],
    [1, 1, 0],
    [1, 0, 0]
]

# Print result
print("Shortest Path Length:", shortestPathBinaryMatrix(grid))
