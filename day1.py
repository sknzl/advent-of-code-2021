from aocd import get_data


def return_data():
    data_str_array = get_data(day=1).split("\n")
    return [int(item) for item in data_str_array]


def part_a():
    data_int_array = return_data()
    increases = [
        next_item - item
        for item, next_item in zip(data_int_array, data_int_array[1:])
        if next_item - item > 0
    ]
    return len(increases)


def part_b():
    data_int_array = return_data()
    moving_window = [
        a + b + c
        for a, b, c in zip(data_int_array, data_int_array[1:], data_int_array[2:])
    ]
    increases = [
        next_item - item
        for item, next_item in zip(moving_window, moving_window[1:])
        if next_item - item > 0
    ]
    return len(increases)


if __name__ == "__main__":
    print(part_a())
    print(part_b())
