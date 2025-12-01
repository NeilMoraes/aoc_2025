from utils import import_data


data = import_data("data/day1.txt")


def turn_dial():

    return


# Part 1
def part1():
    value = 50
    counter = 0

    for line in data:
        direction, rotation = line[0], int(line[1:])

        # Added handling for rotations larger than 100
        value += rotation % 100 if direction == "R" else -rotation % 100

        if value < 0:
            value += 100

        if value > 99:
            value -= 100

        if value == 0:
            counter += 1

    print(f"Part 1: {counter}")


if __name__ == "__main__":

    # Part 1 - 1177
    part1()
