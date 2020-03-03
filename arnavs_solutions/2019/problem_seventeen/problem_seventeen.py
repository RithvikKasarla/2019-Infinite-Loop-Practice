from typing import List, NamedTuple


def num_surrounding_cells(grid: List[List[int]], row: int, column: int) -> int:
    amount = 0
    candidates = [  # All 8 surrounding locations for a cell
        lambda i, j: (i - 1, j - 1),
        lambda i, j: (i - 1, j),
        lambda i, j: (i - 1, j + 1),
        lambda i, j: (i, j - 1),
        lambda i, j: (i, j + 1),
        lambda i, j: (i + 1, j - 1),
        lambda i, j: (i + 1, j),
        lambda i, j: (i + 1, j + 1),
    ]

    for candidate in candidates:
        i, j = candidate(row, column)
        if i < 0 or j < 0:  # Negative indices valid in Python
            continue
        try:  # Handle invalid locations for edge cells by ignoring index erros
            if grid[i][j] == 1:
                amount += 1
        except IndexError:
            continue

    return amount


def main():
    test_cases = int(input())

    for _ in range(test_cases):
        generations = int(input())

        grid = []
        for _ in range(10):
            grid.append(list(map(int, list(input()))))

        for _ in range(generations):
            mark_for_toggle = []  # Toggle all locations in this list each generation
            for row in range(len(grid)):
                for column in range(len(grid[row])):
                    if (  # Any live cell adjacent to one or zero live cells dies (from loneliness).
                        grid[row][column] == 1
                        and num_surrounding_cells(grid, row, column) <= 1
                    ):
                        mark_for_toggle.append((row, column))
                    elif (  # Any live cell adjacent to four or more live cells dies (from overcrowding).
                        grid[row][column] == 1
                        and num_surrounding_cells(grid, row, column) >= 4
                    ):
                        mark_for_toggle.append((row, column))
                    elif (  # Any live cell adjacent to four or more live cells dies (from overcrowding).
                        grid[row][column] == 0
                        and num_surrounding_cells(grid, row, column) == 3
                    ):
                        mark_for_toggle.append((row, column))

            for toggle_location in mark_for_toggle:
                if grid[toggle_location[0]][toggle_location[1]] == 0:
                    grid[toggle_location[0]][toggle_location[1]] = 1
                else:
                    grid[toggle_location[0]][toggle_location[1]] = 0

        print("\n".join("".join(map(str, row)) for row in grid))


if __name__ == "__main__":
    main()
