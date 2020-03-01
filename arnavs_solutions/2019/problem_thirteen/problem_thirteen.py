test_cases = int(input())

for _ in range(test_cases):
    rows, columns, num_bombs = map(int, input().split())

    bombs = []
    for _ in range(num_bombs):
        bombs.append(tuple(map(int, input().split())))

    grid = []
    for i in range(rows):
        grid.append([0] * columns)

    for bomb in bombs:
        grid[bomb[0]][bomb[1]] = "*"

    # All 8 surrounding locations; edges won't have all of these
    # but errors are ignored in that case
    candidates = [
        lambda i, j: (i - 1, j - 1),
        lambda i, j: (i - 1, j),
        lambda i, j: (i - 1, j + 1),
        lambda i, j: (i, j - 1),
        lambda i, j: (i, j + 1),
        lambda i, j: (i + 1, j - 1),
        lambda i, j: (i + 1, j),
        lambda i, j: (i + 1, j + 1),
    ]

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == "*":
                continue

            current_counter = 0
            for candidate in candidates:
                try:
                    row, column = candidate(i, j)
                    if (
                        row < 0 or column < 0
                    ):  # Python accepts negative indices, invalid in this case
                        continue
                    if grid[row][column] == "*":
                        current_counter += 1
                except IndexError:
                    continue
            grid[i][j] = str(current_counter)

    print("\n".join("".join(row) for row in grid))
