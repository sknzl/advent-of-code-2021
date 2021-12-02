from aocd import get_data


def return_data():
    data_str_array = get_data(day=2).split("\n")
    return [(item.split()[0], int(item.split()[1])) for item in data_str_array]


def part_a():
    position = {"horizontal": 0, "vertical": 0}
    for direction, value in return_data():
        if direction == "forward":
            position["horizontal"] += value
        elif direction == "down":
            position["vertical"] += value
        elif direction == "up":
            position["vertical"] -= value

    return position["horizontal"] * position["vertical"]


def part_b():
    position = {"horizontal": 0, "vertical": 0, "aim": 0}
    for direction, value in return_data():
        if direction == "forward":
            position["horizontal"] += value
            position["vertical"] += value * position["aim"]
        elif direction == "down":
            position["aim"] += value
        elif direction == "up":
            position["aim"] -= value

    return position["horizontal"] * position["vertical"]


if __name__ == "__main__":
    print(part_a())
    print(part_b())
