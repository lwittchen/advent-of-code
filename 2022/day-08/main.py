from itertools import product


def plot_grid(grid: dict, rows: int, cols: int) -> list:
    grid_out = [[None for i in range(cols)] for _ in range(rows)]
    for (row, col), val in grid.items():
        grid_out[row][col] = val
    return grid_out


def get_grid_p1(array: list, n_rows: int, n_cols: int) -> dict:
    grid = dict()
    for row, col in product(range(n_rows), range(n_cols)):
        if (row == 0) or (col == 0) or (row == (n_rows - 1)) or (col == (n_cols - 1)):
            grid[(row, col)] = 1
            continue

        val = array[row][col]
        left_col = val > max(array[row][:col])
        right_col = val > max(array[row][col + 1 :])
        top_row = val > max([array[i][col] for i in range(row)])
        down_row = val > max([array[i][col] for i in range(row + 1, n_rows)])
        if left_col or right_col or top_row or down_row:
            grid[(row, col)] = 1
        else:
            grid[(row, col)] = 0
    return grid


def num_to_blocker(val: int, list_: list) -> int:
    if not list_:
        return 0

    num = 0
    for i in list_:
        num += 1
        if i >= val:
            return num
    return num


def get_grid_p2(array: list, n_rows: int, n_cols: int) -> dict:
    grid = dict()
    for row, col in product(range(n_rows), range(n_cols)):
        val = array[row][col]
        left_col = num_to_blocker(val, reversed(array[row][:col]))
        right_col = num_to_blocker(val, array[row][col + 1 :])
        top_row = num_to_blocker(val, reversed([array[i][col] for i in range(row)]))
        down_row = num_to_blocker(val, [array[i][col] for i in range(row + 1, n_rows)])
        grid[(row, col)] = left_col * right_col * top_row * down_row
    return grid


if __name__ == "__main__":
    filename = "input.txt"
    lines = [line.strip() for line in open(filename) if line.strip()]
    array = [list(map(int, line)) for line in lines]

    n_rows = len(array)
    n_cols = len(array[0])

    grid_p1 = get_grid_p1(array, n_rows, n_cols)
    grid_out = plot_grid(grid_p1, n_rows, n_cols)  # just for debugging
    final_sum_p1 = sum(grid_p1.values())

    grid_p2 = get_grid_p2(array, n_rows, n_cols)
    final_score_p2 = max(grid_p2.values())

    print("--- results ---")
    print(f"{final_sum_p1=}")
    print(f"{final_score_p2=}")
