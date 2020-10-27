import argparse
import csv
import time


class Sort:
    insertion_sort_comparison_counter = 0
    insertion_sort_swap_counter = 0
    merge_sort_comparison_counter = 0
    merge_sort_swap_counter = 0

    def __init__(self, array):
        self.array = array

    @staticmethod
    def insertion_sort(array, comparing_function):
        for index in range(1, len(array)):
            key_item = array[index]
            item = index - 1
            while item >= 0 and comparing_function(key_item, array[item]):
                Sort.insertion_sort_comparison_counter += 1
                array[item + 1] = array[item]
                item -= 1
            array[item + 1] = key_item
        return array

    @staticmethod
    def merge_sort(array):
        if len(array) < 2:
            return array

        midpoint = len(array) // 2
        return Sort.merge(
            left=Sort.merge_sort(array[:midpoint]),
            right=Sort.merge_sort(array[midpoint:]),
            comparing_function=lambda x, y: x.engine_power <= y.engine_power)

    @staticmethod
    def merge(left, right, comparing_function):
        if len(left) == 0:
            return right
        if len(right) == 0:
            return left

        result = []
        index_left = index_right = 0
        Sort.merge_sort_comparison_counter += 1
        while len(result) < len(left) + len(right):
            if comparing_function(left[index_left], right[index_right]):
                Sort.merge_sort_swap_counter += 1
                result.append(left[index_left])
                index_left += 1
            else:
                result.append(right[index_right])
                index_right += 1
            if index_right == len(right):
                result += left[index_left:]
                break
            if index_left == len(left):
                result += right[index_right:]
                break
        return result


class File:
    def __init__(self, csv_filename):
        self.csv_filename = csv_filename

    def read_csv(self):
        elevators = []
        try:
            with open(self.csv_filename) as csv_fd:
                reader = csv.reader(csv_fd, delimiter=",")
                n = 0
                for row in reader:
                    n += 1
                    if len(row) != 3:
                        print(f"Warning: Wrong Row[{n}] length")
                    try:
                        float(row[1])
                        float(row[2])
                    except ValueError as err:
                        print("ValueError:", err)
                        continue
                    elevators.append(Elevator(row[0], row[1], row[2]))
                return elevators
        except FileNotFoundError as err:
            print("FileNotFoundError:", err)

    # def write_csv(self, text):
    #     with open(self.csv_filename, "w") as writer:
    #         writer.write(text)


class Elevator:
    def __init__(self, name, load_capacity, engine_power):
        self.name = str(name)
        self.load_capacity = int(load_capacity)
        self.engine_power = int(engine_power)

    def __repr__(self):
        return "Elevator(" + repr(self.name) + ")"


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="filename", required=True)
    parser.add_argument("-t", "--type", dest="sort_type", required=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse()
    filename, sort_type = args.filename, args.sort_type
    print("Loaded File:", filename)
    print("Sorting Algorithm:", sort_type)
    file = File(filename)
    list_of_objects = file.read_csv()

    time_start = time.time()
    if sort_type == "insertion_sort":
        new_list = Sort.insertion_sort(
            list_of_objects, (lambda x, y: x.load_capacity < y.load_capacity))
        print("Compare counter:", Sort.insertion_sort_comparison_counter)
        print("Swap counter:", Sort.insertion_sort_swap_counter)
    elif sort_type == "merge_sort":
        new_list = Sort(list_of_objects).merge_sort(list_of_objects)
        print("Compare counter:", Sort.merge_sort_comparison_counter)
        print("Swap counter:", Sort.merge_sort_swap_counter)
    else:
        print("Algorithm not found")
        exit()

    time_end = time.time() - time_start
    print("Algorithm time:", time_end)

    dict_keys = ["name", "load_capacity", "engine_power"]

    with open(filename, 'w') as f:
        w = csv.writer(f)
        for dict_data in new_list:
            my_dict = dict_data.__dict__
            dict_name = my_dict["name"]
            dict_load_capacity = my_dict["load_capacity"]
            dict_engine_power = my_dict["engine_power"]
            f.write(f"{dict_name},{dict_load_capacity},{dict_engine_power}\n")
