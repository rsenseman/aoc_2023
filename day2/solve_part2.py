from collections import defaultdict, namedtuple
import re

Handful = namedtuple("Handful", ["reds", "greens", "blues"])
GAME_MATCH = re.compile(r"Game ([0-9]+)")
RED_MATCH = re.compile(r"([0-9]+) red")
GREEN_MATCH = re.compile(r"([0-9]+) green")
BLUE_MATCH = re.compile(r"([0-9]+) blue")

def get_input(input_file="input.txt"):
    with open(input_file) as f:
        contents = f.readlines()
    return contents

def parse_handful_string(handful_string):
    reds = int(RED_MATCH.search(handful_string).group(1)) if RED_MATCH.search(handful_string) else 0
    greens = int(GREEN_MATCH.search(handful_string).group(1)) if GREEN_MATCH.search(handful_string) else 0
    blues = int(BLUE_MATCH.search(handful_string).group(1)) if BLUE_MATCH.search(handful_string) else 0
    return Handful(reds, greens, blues)

def parse_lines(lines):
    games = {}

    for line in lines:
        game_identifier, handfuls = line.split(":")

        game_id = int(GAME_MATCH.search(game_identifier).group(1))
        handfuls = [
            parse_handful_string(handful)
            for handful
            in handfuls.split(";")
        ]
        games[game_id] = handfuls

    return games

def make_min_set(handfuls):
    rgb_sets = [rgb for rgb in zip(*handfuls)]
    rgb_mins = Handful(*[max(rgb_set) for rgb_set in rgb_sets])
    return rgb_mins

def get_game_power(min_set):
    return min_set.reds * min_set.greens * min_set.blues

def solve():
    lines = get_input()
    games_dict = parse_lines(lines)

    min_sets = [make_min_set(handfuls) for game, handfuls in games_dict.items()]
    game_power = [get_game_power(min_set) for min_set in min_sets]

    sum_game_power = sum(game_power)
    return sum_game_power


if __name__ == '__main__':
    solution = solve()
    print(solution)