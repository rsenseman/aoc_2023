from collections import namedtuple
import sys
import re

CubeRound = namedtuple('CubeRound', ['game_id', 'reds', 'greens', 'blues'])
class ExtendedRound(CubeRound):
    def get_power(self):
        return self.reds * self.greens * self.blues

class MinRoundContainer:
    def __init__(self):
        self.min_reds = 0
        self.min_greens = 0
        self.min_blues = 0
    
    def add_round(self, round:CubeRound):
        self.min_reds = self.min_reds if round.reds < self.min_reds else round.reds
        self.min_greens = self.min_greens if round.greens < self.min_greens else round.greens
        self.min_blues = self.min_blues if round.blues < self.min_blues else round.blues



def get_structured_round_spec(game_id, round_string):
    num_reds_match = re.search(r"(\d+) red", round_string)
    num_greens_match = re.search(r"(\d+) green", round_string)
    num_blues_match = re.search(r"(\d+) blue", round_string)

    num_reds = int(num_reds_match.group(1)) if num_reds_match else 0
    num_greens = int(num_greens_match.group(1)) if num_greens_match else 0
    num_blues = int(num_blues_match.group(1)) if num_blues_match else 0

    return CubeRound(game_id, num_reds, num_greens, num_blues)

def get_input(filename=sys.argv[1]):
    with open(filename) as f:
        for l in f.readlines():
            yield l.strip()

def clean_input(input_line):
    id_string, rounds_strings = input_line.split(": ")

    game_id = int(id_string.split(" ")[1])
    round_strings = rounds_strings.split(";")

    rounds = [
        get_structured_round_spec(game_id, round_string)
        for round_string
        in round_strings
    ]

    return rounds

def solve_part1():
    file_lines = get_input()
    rounds = []
    for line in file_lines:
        rounds.extend(clean_input(line))

    max_reds = 12
    max_greens = 13
    max_blues = 14

    all_games = set(round.game_id for round in rounds)
    invalid_games = set(
        round.game_id 
        for round 
        in rounds 
        if (round.reds > max_reds) or (round.greens > max_greens) or (round.blues > max_blues)
    )

    valid_games = all_games - invalid_games
    result = sum(valid_games)

    print(result)

def get_power_of_minset(rounds):
    min_round_tracker = MinRoundContainer()

    for round in rounds:
        min_round_tracker.add_round(round)

    min_round = ExtendedRound(0, min_round_tracker.min_reds, min_round_tracker.min_greens, min_round_tracker.min_blues)
    min_round_power = min_round.get_power()

    return min_round_power

def solve_part2():
    file_lines = get_input()

    power_sum = 0

    for line in file_lines:
        game_rounds = clean_input(line)
        power_sum += get_power_of_minset(game_rounds)

    print(power_sum)

if __name__ == "__main__":
    # solve_part1()
    solve_part2()