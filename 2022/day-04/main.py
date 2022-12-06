def is_subset(range_x, range_y):
    set_x = set(range_x)
    set_y = set(range_y)

    return set_x.issubset(set_y) or set_y.issubset(set_x)


def is_overlap(range_x, range_y):
    set_x = set(range_x)
    set_y = set(range_y)

    return not set_x.isdisjoint(set_y) or not set_y.isdisjoint(set_x)


if __name__ == "__main__":
    filename = "input.txt"
    lines = [l.strip() for l in open(filename).readlines()]

    count = 0
    overlaps = 0
    for line in lines:
        start_x, end_x = map(int, line.split(",")[0].split("-"))
        start_y, end_y = map(int, line.split(",")[1].split("-"))

        count += is_subset(range(start_x, end_x + 1), range(start_y, end_y + 1))
        overlaps += is_overlap(range(start_x, end_x + 1), range(start_y, end_y + 1))

    print("--- result ---")
    print(f"{count=}")
    print(f"{overlaps=}")
