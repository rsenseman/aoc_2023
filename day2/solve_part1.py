from collections import defaultdict, namedtuple
import re

RGB_MAX = (12, 13, 14)
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

def is_handful_valid(handful):
    for num, max in zip(handful, RGB_MAX):
        if num > max:
            return False
    return True

def is_game_valid(handfuls):
    for handful in handfuls:
        if not is_handful_valid(handful):
            return False
    return True

def solve():
    lines = get_input()
    games_dict = parse_lines(lines)

    valid_game_ids = [game_id for game_id, handfuls in games_dict.items() if is_game_valid(handfuls)]
    game_id_sum = sum(valid_game_ids)

    return game_id_sum

if __name__ == '__main__':
    part1_solution = solve()
    print(part1_solution)