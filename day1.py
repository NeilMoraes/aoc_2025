from utils import import_data


# Part 1
def part1(data: list[str]):

    # Variables
    value = 50
    counter = 0

    for line in data:
        direction, rotation = line[0], int(line[1:])

        # Perform a rotation
        value = (
            (value + rotation) % 100 if direction == "R" else (value - rotation) % 100
        )

        # Increment counter
        if value == 0:
            counter += 1

    print(f"Part 1: {counter}")


# Part 2
def part2(data: list[str]):

    # Variables
    value = 50
    counter = 0

    for line in data:
        direction, rotation = line[0], int(line[1:])

        # Perform a rotation
        prev_value = value
        overflow = (value + rotation) if direction == "R" else (value - rotation)
        value = overflow % 100

        # Increment counter based on overflows
        if (direction == "R") & (overflow > 99):
            counter += overflow // 100
        elif (direction == "L") & (overflow < 1):
            counter += 1 + (abs(overflow) // 100) - (1 if prev_value == 0 else 0)

    print(f"Part 2: {counter}")


if __name__ == "__main__":
    sample = import_data("data/day1_sample.txt")
    data = import_data("data/day1.txt")

    # Part 1 - Sample
    part1(sample)

    # Part 1 - 1177
    part1(data)

    # Part 2 - Sample
    part2(sample)

    # Part 2 - 6768
    part2(data)
