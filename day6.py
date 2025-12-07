from functools import reduce


def import_data(filepath: str) -> list[str]:
    with open(filepath, "r") as f:
        data = [line for line in f.readlines()]
    return data


test = ["123 328  51 64 ", " 45 64  387 23 ", "  6 98  215 314", "*   +   *   +  "]


def part1(data: list[str]):

    # Variables
    counter = 0

    info = [row.split() for row in data]

    for i in range(len(info[0])):

        if info[-1][i] == "+":
            counter += reduce(lambda x, y: x + y, [int(row[i]) for row in info[:-1]])
        else:
            counter += reduce(lambda x, y: x * y, [int(row[i]) for row in info[:-1]])

    print(f"Part 1: {counter}")


def part2(data: list[str]):

    # Variables
    counter = 0

    info = [row for row in data]

    # print(info)

    # Read columns backwards
    calc = []
    for i in range(len(info[0]) - 1):
        calc_str = ""
        for j in range(len(info) - 1):
            calc_str += info[j][i]

        calc.append(calc_str.strip())

    operators = info[len(info) - 1][: len(info[0])].split()

    l = []
    i = 0
    for j, val in enumerate(calc):
        try:
            l.append(int(val.strip()))
            if j == len(calc) - 1:
                raise
        except:
            print("l", l, "op", operators[i])
            if operators[i] == "+":
                counter += reduce(lambda x, y: x + y, l)
            else:
                counter += reduce(lambda x, y: x * y, l)
            i += 1
            l = []

    print(f"Part 2: {counter}")


if __name__ == "__main__":

    data = import_data("data/day6.txt")

    # Part 1 - Sample
    part1(test)

    # Part 1
    part1(data)

    # Part 2 - Sample
    # part2(test)

    # Part 2
    part2(data)
