#############################################
#               Long poker                  #
#############################################

from random import randint
from typing import List
from sorting_algo import Sort


class DeckGeneration:

    def __init__(self, length=None, min_v=None, max_v=None):
        self.deck_length = length
        self.min_value = min_v
        self.max_value = max_v

    def user_inputs(self):
        cards_deck = []

        if self.deck_length <= 0 \
                or self.min_value <= 0 \
                or self.min_value > self.max_value \
                or self.max_value > 1000000:
            print("Incorrect input!"), exit()
        elif self.deck_length == "exit" or self.min_value == "exit" or self.max_value == "exit":
            exit()

        while self.deck_length > 0:
            self.deck_length -= 1
            cards_deck.append(randint(min_value, max_value))
        # print(cards_deck)
        return cards_deck

    @staticmethod
    def read_file(file_name: str) -> List[int]:
        try:
            with open(file_name) as f:
                return list(map(int, (f.readline().split())))
        except FileNotFoundError as error:
            print("!", error), exit()
        except ValueError as error:
            print(f"Value Error in file: {file_name}\n", error, end=""), exit()


def joker(array: list, min_v: int, max_v: int) -> List[int]:
    if min_v < 1 or max_v < 1:
        raise ValueError("Invalid max or min input")
    for i in range(len(array)):
        if array[i] == 0:
            array[i] = randint(min_v, max_v)
        else:
            return array


def output(line):
    with open("lngpok.out", "w+") as file:
        file.write(str(line))


def max_sequence(array: list) -> int:
    sequence = []
    comp_sequence = []
    boo = True
    if len(array) == 0:
        return 0

    for i in range(len(array) - 1):
        if boo is True:
            comp_sequence.append(array[i])
            boo = False
        if array[i] == (array[i + 1]):
            # print("same: ", deck[i], deck[i + 1])
            continue
        elif array[i] + 1 == (array[i + 1]):
            comp_sequence.append(array[i + 1])
            # print("comp_sequence: ", comp_sequence)
        else:
            boo = True
            comp_sequence = []
        if len(comp_sequence) >= len(sequence):
            sequence = comp_sequence[:]

    if len(sequence) == 0:
        return 1

    print("Sequence of cards: ", sequence)
    return len(sequence)

# def circle(r):
#     if type(r) not in [int, float]:
#         raise TypeError("text")


if __name__ == '__main__':
    select_mode = None
    deck_length = None
    min_value = None
    max_value = None
    deck = []

    print("Please select mode:")
    print("1 - random mode")
    print("2 - user mode")

    try:
        select_mode = int(input("Enter mode: "))
    except ValueError as err:
        print(err), exit()

    if select_mode == 1:
        try:
            deck_length = int(input("Enter the length of the deck: "))
            min_value = int(input("Enter min value: "))
            max_value = int(input("Enter max value: "))
        except ValueError as err:
            print(err), exit()

        deck_generation = DeckGeneration(deck_length, min_value, max_value)
        deck = deck_generation.user_inputs()
        print("Random Cards Deck: ", deck)

        Sort.quick_sort(deck, 0, (len(deck) - 1))
        print("Quick Sorted Deck: ", deck)

    elif select_mode == 2:
        deck = DeckGeneration.read_file("lngpok.in")
        print("User Deck: ", deck)
        Sort.quick_sort(deck, 0, (len(deck) - 1))
        print("Quick Sorted Deck: ", deck)

        if deck[0] == 0:
            try:
                min_value = int(input("Enter joker min value: "))
                max_value = int(input("Enter joker max value: "))
            except ValueError as err:
                print(err), exit()

            joker(deck, min_value, max_value)
            print("Deck with jokers:", deck)
            Sort.insertion_sort(deck)
            print("Insertion Sorted Deck: ", deck)
    else:
        print("*mode not found -_-"), exit()

    num = max_sequence(deck)
    print(num)
    output(num)
