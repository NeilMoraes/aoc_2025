from utils import import_data


data = import_data("data/day1.txt")


# Part 1
def part1():
    value = 50
    counter = 0

    for line in data:
        direction, rotation = line[0], int(line[1:])

        value = (
            (value + rotation) % 100 if direction == "R" else (value - rotation) % 100
        )

        if value == 0:
            counter += 1

    print(f"Part 1: {counter}")


# Part 2
def part2():
    value = 50
    counter = 0

    for line in data:
        direction, rotation = line[0], int(line[1:])
        prev_value = value

        delta = (value + rotation) if direction == "R" else (value - rotation)
        value = delta % 100

        if value == 0:
            counter += 1
        elif (delta < 0) & (prev_value != 0):
            counter += (rotation // 100) + (
                1 if (prev_value - rotation % 100) < 0 else 0
            )
        elif delta > 99:
            counter += (rotation // 100) + (
                1 if (prev_value + rotation % 100) > 100 else 0
            )

        print(prev_value, line, delta, value, counter)
    print(f"Part 2: {counter}")


if __name__ == "__main__":

    # Part 1 - 1177
    # part1()

    # Part 2 - Not implemented yet
    part2()
