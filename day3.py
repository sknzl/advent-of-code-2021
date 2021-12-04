from aocd import get_data


def return_data():
    data_str_array = get_data(day=3).split("\n")
    return [list(map(int, x)) for x in data_str_array]


def part_a():
    data = return_data()
    sum_vector = [sum(i) for i in zip(*data)]
    gamma = epsilon = ""
    for element in sum_vector:
        if element > len(data) / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    # Not covered if equal amount ouf 1s and 0s

    return int(gamma, 2) * int(epsilon, 2)


if __name__ == "__main__":
    print(part_a())
