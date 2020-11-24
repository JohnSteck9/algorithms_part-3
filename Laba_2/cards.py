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
    max_sequence = []
    sequence = []
    jok = joker_num
    boo = False
    array_end = False

    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return 1
    else:   # * якщо є тільки джокери
        try:
            sequence = [array[joker_num]]
        except IndexError:
            return joker_num

    for i in range(joker_num, len(array)):
        # 0 0 0 [3 - 5 6 - 8 9 - - - 13 - - 16 17 18 ... 30 31 - -33 34 35 36 37]

        # пропускаємо якщо вставити 1 елемент в список або минуле значення послідовне
        if i - joker_num > 0:
            # * щоб не вийти за межі array
            if array[i] == array[-1]:
                if array[i] == sequence[-1] + 1:
                    sequence.append(array[i])
                array_end = True
                break

        if boo is True:
            sequence.append(array[i])
            boo = False

        j = i + 1
        while True:
            # * щоб не вийти з циклу
            if array[j] == array[-1]:
                if array[j] == sequence[-1] + 1:
                    sequence.append(array[j])
                array_end = True
                break

            # -- якщо наступна карта на 1 більша ніж попередня в sequence[]
            if array[j] == sequence[-1] + 1:
                sequence.append(array[j])
                j += 1
                continue

            # -- use jokers
            else:
                # -- використовуємо джокери поки не закінчаться або не натрапимо на послідовну карту
                while array[j] > sequence[-1] + 1 and jok > 0:
                    sequence.append(int(sequence[-1]) + 1)
                    jok -= 1

                # -- якщо натрпаили на послідовну карту -> add
                if int(sequence[-1]) + 1 == array[j]:
                    sequence.append(array[j])
                    j += 1
                    continue
                    # -- якщо джокери закінчилися і нема послідовності
                    # * порівнюємо sequence[] з max_sequence[] -> break
                elif jok == 0:
                    if len(max_sequence) < len(sequence):
                        max_sequence = sequence[:]
                        boo = True
                        sequence = []
                        jok = joker_num
                        break

                    else:
                        boo = True
                        sequence = []
                        # sequence = [array[i + 1]]
                        jok = joker_num
                        break

                elif array[j] == array[-1]:
                    print("GG")
                    break
                else:
                    print("@@@")
                    break
        if array_end is True:
            break
        print("OK")

    while jok > 0:
        if sequence[-1] < 1000000:  # * блокуємо вихід через верхню межу
            sequence.append(int(sequence[-1] + 1))
        else:
            sequence.insert(0, int(sequence[0] - 1))
        jok -= 1

    if len(max_sequence) < len(sequence):
        max_sequence = sequence[:]
        print("Max: ", max_sequence)
        return len(max_sequence)
    else:
        print("Max: ", max_sequence)
        print(max_sequence)
        return len(max_sequence)


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
