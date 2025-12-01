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

        if direction == "R":
            counter += delta // 100
        elif (direction == "L") & (delta < 0) & (prev_value > 0):
            counter += -delta // 100 + 1
        elif (value == 0) & (direction == "L"):
            counter += -delta // 100 if rotation > 100 else 1
        elif value == 0:
            counter += 1
        print(prev_value, line, delta, value, counter)
    print(f"Part 2: {counter}")


if __name__ == "__main__":

    # Part 1 - 1177
    # part1()

    # Part 2 - Not implemented yet - 6180
    part2()
