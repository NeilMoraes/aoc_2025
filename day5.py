from utils import import_data

test = ["3-5", "10-14", "16-20", "12-18", ""]


def part1(data: list[str]):

    # Variables
    counter = []

    fresh_ranges, ids = data[: data.index("")], data[data.index("") + 1 :]

    for id in ids:
        for rng in fresh_ranges:
            x, y = rng.split("-")
            if int(id) in range(int(x), int(y) + 1):
                counter.append(id)

    print(f"Part 1: {len(set(counter))}")


def has_no_overlap(rng1, rng2):
    """True if rng2 has no overlap with rng1"""

    x1, y1 = rng1
    x2, y2 = rng2

    if x2 > y1:
        return True
    return False


def adj_rng(rng1, rng2):
    """Extends rng1 to include rng2 if there is an overlap"""

    x1, y1 = rng1
    x2, y2 = rng2

    if (x2 >= x1) & (x2 <= y1) & (y2 > y1):
        return (x1, y2)
    else:
        return (x1, y1)


def part2(data: list[str]):

    # Variables
    counter = 0
    final = []  # Store non overlapping ranges

    fresh_ranges = sorted(
        [
            (int(rng.split("-")[0]), int(rng.split("-")[1]))
            for rng in data[: data.index("")]
        ]
    )

    L = len(fresh_ranges)
    # print(fresh_ranges)

    i = 0
    while i < L:
        x1, y1 = fresh_ranges[i]

        print("Start rng1:", x1, y1)

        # Adjust range1
        while True:
            i += 1

            if i == L:
                break

            x2, y2 = fresh_ranges[i]

            if has_no_overlap((x1, y1), (x2, y2)):
                break

            x1, y1 = adj_rng((x1, y1), (x2, y2))

            print("  rng2", x2, y2, "Adj rng1", x1, y1)

        final.append((x1, y1))

    # count all non overlapping ranges
    counter = sum([rng[1] - rng[0] + 1 for rng in final])

    print(f"Part 2: {counter}")


if __name__ == "__main__":
    sample = import_data("data/day5_sample.txt")
    data = import_data("data/day5.txt")

    # Part 1 - Sample
    part1(sample)

    # Part 1
    part1(data)

    # Part 2 - Sample
    part2(test)

    # Part 2
    part2(data)
