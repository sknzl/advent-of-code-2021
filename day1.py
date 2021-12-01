from aocd import get_data

def part_a():
    data_str_array = get_data(day=1).split("\n")
    data_int_array = [int(item) for item in data_str_array]
    increases = [ next_item - item for item, next_item in zip(data_int_array, data_int_array[1:]) if next_item - item  > 0]
    return len(increases)

if __name__ == '__main__':
    print(part_a())