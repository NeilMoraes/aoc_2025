from utils import import_data


def part1(data: list[str]):

    # Variables
    counter = 0
    total = 0

    Y = len(data)
    X = len(data[0])

    for y in range(Y):
        for x in range(X):
            current = data[y][x]

            if current != "@":
                continue

            neighbours = [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ]

            for n in neighbours:

                ny = y + n[0]
                nx = x + n[1]

                if ny in range(Y) and nx in range(X):
                    if data[ny][nx] == "@":
                        total += 1

            if total < 4:
                counter += 1
            total = 0

    print(f"Part 1: {counter}")


def part2(data: list[str]):

    # Variables
    counter = 0
    total = 0
    remove = []
    is_removed = True

    Y = len(data)
    X = len(data[0])

    while is_removed:
        is_removed = False
        for y in range(Y):
            for x in range(X):
                current = data[y][x]

                if current != "@":
                    continue

                neighbours = [
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                    (0, -1),
                    (0, 1),
                    (1, -1),
                    (1, 0),
                    (1, 1),
                ]

                for n in neighbours:

                    ny = y + n[0]
                    nx = x + n[1]

                    if ny in range(Y) and nx in range(X):
                        if data[ny][nx] == "@":
                            total += 1

                if total < 4:
                    is_removed = True
                    remove.append((y, x))
                total = 0
        if not is_removed:
            break

        for ry, rx in remove:
            data[ry] = data[ry][:rx] + "." + data[ry][rx + 1 :]

    print(f"Part 2: {len(remove)}")


if __name__ == "__main__":
    sample = import_data("data/day4_sample.txt")
    data = import_data("data/day4.txt")

    # Part 1 - Sample
    part1(sample)

    # Part 1
    part1(data)

    # Part 2 - Sample
    part2(sample)

    # Part 2
    part2(data)
