#############################################
#               Long poker                  #
#############################################

from typing import List
from sorting_algo import Sort


class DeckGeneration:

    @staticmethod
    def read_file(file_name: str) -> List[int]:
        try:
            with open(file_name) as f:
                return list(map(int, (f.readline().split())))
        except FileNotFoundError as error:
            print("!", error), exit()
        except ValueError as error:
            print(f"Value Error in file: {file_name}\n", error, end=""), exit()


def joker(array: list):
    joker_n = 0
    for i in range(len(array)):
        if array[i] == 0:
            joker_n += 1
        else:
            return joker_n
    return joker_n


def output(line):
    with open("lngpok.out", "w+") as file:
        file.write(str(line))


def sequence_exit():
    pass


def max_sequence(array: list, joker_num: int) -> int:
    sequence = []
    comp_sequence = []
    num_sequence = 0
    max = 0
    seq = 0
    jok = joker_num

    if len(array) == 0:
        return num_sequence
    else:
        comp_sequence.append(array[joker_num])  # * ставимо перше значення
        seq += 1

    for i in range(joker_num, len(array) - joker_num):
        j = i + 1
        while True:
        # while len(array[i:]) >= max:
            if array[-1] == array[j - 1]:
                break

            if array[j - 1] == array[j]:  # * скіпаєм повторювальні значення
                j += 1
                continue

            elif int(comp_sequence[-1]) + 1 == array[j]:  # * якщо число послідовне (додаємо до comp_sequence)
                comp_sequence.append(array[j])
                seq += 1
                j += 1
                continue

            else:  # -- використовуємо джокери
                while int(comp_sequence[-1]) + 1 < array[j] and jok > 0:
                    comp_sequence.append(int(comp_sequence[-1]) + 1)
                    seq += 1
                    jok -= 1
                if int(comp_sequence[-1]) + 1 == array[j]:  # -- якщо дійшли до послідовності
                    comp_sequence.append(array[j])
                    seq += 1
                    j += 1
                    continue
                    # -- якщо джокери закінчилися і нема послідовності повістю виходимо з циклу
                    # -- записуємо послідовність і порівнюємо її з максимальною
                elif jok == 0:
                    if max < seq:
                        max = seq
                        sequence = comp_sequence[:]
                        comp_sequence = [array[i+1]]
                        seq = 1
                        jok = joker_num
                    else:
                        comp_sequence = [array[i+1]]
                        seq = 1
                        jok = joker_num
                    # ?continue
                break
            # break
    while jok > 0:
        try:
            if comp_sequence[-1] < 1000000:  # * блокуємо вихід через верхню межу
                comp_sequence.append(int(comp_sequence[-1]+1))
            else:
                comp_sequence.insert(0, int(comp_sequence[0]-1))
        except IndexError:
            return joker_num
        jok -= 1
        seq += 1
    if max < seq:
        max = seq
        # seq = 0
    if len(sequence) < len(comp_sequence):
        sequence = comp_sequence[:]
        # comp_sequence = []
    print("Array: ", sequence, "Max: ", max)
    return max


if __name__ == '__main__':
    select_mode = None
    deck_length = None
    min_value = None
    max_value = None

    deck = DeckGeneration.read_file("lngpok.in")
    print("User Deck: ", deck)
    Sort.quick_sort(deck, 0, (len(deck) - 1))
    print("Quick Sorted Deck: ", deck)

    joker_num = joker(deck)

    # Sort.insertion_sort(deck)
    # print("Insertion Sorted Deck: ", deck)

    num = max_sequence(deck, joker_num)
    print(num)
    output(num)
