from utils import import_data


# Brute force baby :)
def part1(data: list[str]):

    # Variables
    id_ranges = data[0].split(",")
    counter = 0

    for id_range in id_ranges:

        x, y = id_range.split("-")

        for val in range(int(x), int(y) + 1):
            L = len(str(val))
            if L % 2 == 0:
                if str(val)[: L // 2] == str(val)[L // 2 :]:
                    counter += val

    print(f"Part 1: {counter}")


def part2(data: list[str]):

    # Variables
    id_ranges = data[0].split(",")
    counter = 0

    for id_range in id_ranges:

        x, y = id_range.split("-")

        for val in range(int(x), int(y) + 1):
            L = len(str(val))

            # Early exit for single digit numbers
            if L < 2:
                continue

            if str(val) == (L * str(val)[0]):
                counter += val
                continue

            if L % 2 == 0:
                if str(val)[: L // 2] == str(val)[L // 2 :]:
                    counter += val
                else:
                    factors = list(range(2, L // 2, 2))
                    for f in factors:
                        if str(val) == ((L // f) * str(val)[:f]):
                            counter += val
            else:
                factors = list(range(2, L // 2, 1))
                for f in factors:
                    if str(val) == ((L // f) * str(val)[:f]):
                        counter += val

            # print(val)

    print(f"Part 2: {counter}")


if __name__ == "__main__":
    sample = import_data("data/day2_sample.txt")
    data = import_data("data/day2.txt")

    # Part 1 - Sample
    part1(sample)

    # Part 1 - 1177
    part1(data)

    # Part 2 - Sample
    part2(sample)

    # Part 2 - 6768
    part2(data)
