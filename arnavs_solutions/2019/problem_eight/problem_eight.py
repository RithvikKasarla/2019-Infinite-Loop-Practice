test_cases = int(input())

for _ in range(test_cases):
    row, column = map(int, input().split())

    rows = []
    for i in range(20):
        current_row = []
        for j in range(20):
            if i == row and j == column:
                current_row.append("100")
            elif row - 1 <= i <= row + 1 and column - 1 <= j <= column + 1:
                current_row.append("50")
            elif row - 2 <= i <= row + 2 and column - 2 <= j <= column + 2:
                current_row.append("25")
            else:
                current_row.append("10")
        rows.append(" ".join(current_row))

    print("\n".join(rows))

