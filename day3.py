from utils import import_data


def part1(data: list[str]):

    # Variables
    counter = 0

    for bank in data:
        max_joltage = 0
        for i, battery1 in enumerate(bank[:-1]):
            for j, battery2 in enumerate(bank[i + 1 :]):
                joltage = int(battery1 + battery2)
                if joltage > max_joltage:
                    max_joltage = joltage

        counter += max_joltage
    print(f"Part 1: {counter}")


def part2(data: list[str]):

    # Variables
    counter = 0

    for bank in data:
        max_joltage = ""
        idx = 0
        for r in range(12, 0, -1):
            m = max(bank[idx : (len(bank) - r + 1)])
            max_idx = bank.index(m, idx, len(bank) - r + 1)
            idx = max_idx + 1
            max_joltage += str(m)
        counter += int(max_joltage)
    print(f"Part 2: {counter}")


if __name__ == "__main__":
    sample = import_data("data/day3_sample.txt")
    data = import_data("data/day3.txt")

    # Part 1 - Sample
    part1(sample)

    # Part 1 - 1177
    part1(data)

    # Part 2 - Sample
    part2(sample)

    # Part 2 - 6768
    part2(data)
