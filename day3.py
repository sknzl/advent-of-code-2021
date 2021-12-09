from pdb import set_trace
from aocd import get_data
from collections import Counter


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


def part_b():
    data = return_data()
    result_o2 = extract_life_support(data)
    result_co2 = extract_life_support(data, k=1)
    return int("".join([str(elem) for elem in result_o2]), 2) * int(
        "".join([str(elem) for elem in result_co2]), 2
    )


def extract_life_support(data, k=0):
    for index in range(len(data[0])):
        transposed_data = list(map(list, zip(*data)))
        counter = Counter(transposed_data[index])
        if len(data) == 1:
            break
        elif counter[1] > counter[0]:
            remove_list = [
                position
                for position, bit in enumerate(transposed_data[index])
                if bit == 0 ^ k
            ]
            data = [i for j, i in enumerate(data) if j not in remove_list]
        elif counter[0] > counter[1]:
            remove_list = [
                position
                for position, bit in enumerate(transposed_data[index])
                if bit == 1 ^ k
            ]
            data = [i for j, i in enumerate(data) if j not in remove_list]
        elif counter[0] == counter[1]:
            remove_list = [
                position
                for position, bit in enumerate(transposed_data[index])
                if bit == 0 ^ k
            ]
            data = [i for j, i in enumerate(data) if j not in remove_list]

    return data[0]


if __name__ == "__main__":
    print(part_a())
    print(part_b())
