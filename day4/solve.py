import sys
from typing import Iterable, List


def get_input(filename=sys.argv[1]):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]

class ScratchCard:
    def __init__(self, winning_numbers: Iterable, present_numbers: Iterable):
        self.winning_numbers = set(winning_numbers)
        self.present_numbers = set(present_numbers)
        self.num_downstream_copies_awarded = len(self.winning_numbers.intersection(self.present_numbers))

    def calcuate_card_score(self):
        num_matches = len(self.winning_numbers.intersection(self.present_numbers))
        if num_matches > 0:
            return 2**(num_matches-1)
        else:
            return 0


def clean_data(input_lines):
    for line in input_lines:
        all_the_numbers = line.split(": ")[1]
        all_the_winning_numbers, all_the_present_numbers = all_the_numbers.split(" | ")

        winning_numbers_list = [int(num) for num in all_the_winning_numbers.strip().split(" ") if num]
        present_numbers_list = [int(num) for num in all_the_present_numbers.strip().split(" ") if num]

        yield ScratchCard(winning_numbers_list, present_numbers_list)


def solve_part1():
    input_lines = get_input()
    cards: Iterable[ScratchCard] = clean_data(input_lines)
    cumulative_score = sum(card.calcuate_card_score() for card in cards)
    print(cumulative_score)

def solve_part2():
    input_lines = get_input()
    cards: Iterable[ScratchCard] = list(clean_data(input_lines))
    copy_awards = [card.num_downstream_copies_awarded for card in cards]

    card_instances = [1]*len(cards)

    max_pointer = len(cards)-1
    for i, copy_award in enumerate(copy_awards):
        if i >= max_pointer:
            break

        for j in range(i+1, min(i+copy_award+1, max_pointer+1)):
            card_instances[j] += card_instances[i]
            
    print(sum(card_instances))


if __name__ == "__main__":
    # solve_part1()
    solve_part2()