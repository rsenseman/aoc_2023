from collections import namedtuple, defaultdict
from itertools import chain
import re
import sys

PartNumber = namedtuple("PartNumber", ["value", "line_number", "start_x", "end_x"])
Symbol = namedtuple("Symbol", ["value", "line_number", "x"])


def get_input(filename=sys.argv[1]):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]

class Board:
    def __init__(self, lines):
        self.min_x = 0
        self.max_x = len(lines[0])
        self.min_y = 0
        self.max_y = len(lines)

        self.lines = lines
        self.all_numbers = self.get_numbers_from_lines()

        self.all_symbols = self.get_symbols_from_lines()
        self.symbol_map = self.make_symbol_map_from_symbols()

        self.part_numbers = self.get_part_numbers()

        self.stars_map = self.get_stars_map()
        self.gears = self.get_gears()

    @classmethod
    def get_numbers_from_line(cls, line_number, line_contents):
        part_number_matches = re.finditer(r"\d+", line_contents)
        for part_number_match in part_number_matches:
            yield PartNumber(
                int(part_number_match.group(0)),
                line_number,
                int(part_number_match.start()),
                int(part_number_match.end())
            )

    def get_numbers_from_lines(self):
        return list(chain.from_iterable([Board.get_numbers_from_line(i, line) for i, line in enumerate(self.lines)]))
    
    @classmethod
    def get_symbols_from_line(cls, line_number, line_contents):
        symbol_matches = re.finditer(f"[^\d.]", line_contents)
        for symbol_match in symbol_matches:
            yield Symbol(
                symbol_match.group(0),
                line_number,
                int(symbol_match.start())
            )

    def get_symbols_from_lines(self):
        return list(chain.from_iterable([Board.get_symbols_from_line(i, line) for i, line in enumerate(self.lines)]))

    def make_symbol_map_from_symbols(self):
        return {
            (symbol.line_number, symbol.x): symbol.value
            for symbol
            in self.all_symbols
        }

    def is_symbol(self, line_number, x):
        return (line_number, x) in self.symbol_map

    def is_number_adjacent_to_symbol(self, number: PartNumber):
        coordinates_above = [(number.line_number-1, x) for x in range(number.start_x-1, number.end_x+1)]
        coordinates_beside = [(number.line_number, number.start_x-1), (number.line_number, number.end_x)]
        coordinates_below = [(number.line_number+1, x) for x in range(number.start_x-1, number.end_x+1)]

        return any(self.is_symbol(*coordinate) for coordinate in chain.from_iterable([coordinates_above, coordinates_beside, coordinates_below]))

    def get_part_numbers(self):
        return [number for number in self.all_numbers if self.is_number_adjacent_to_symbol(number)]

    def get_adjacent_stars(self, number: PartNumber):
        coordinates_above = [(number.line_number-1, x) for x in range(number.start_x-1, number.end_x+1)]
        coordinates_beside = [(number.line_number, number.start_x-1), (number.line_number, number.end_x)]
        coordinates_below = [(number.line_number+1, x) for x in range(number.start_x-1, number.end_x+1)]

        return [
            coordinate
            for coordinate 
            in chain.from_iterable([coordinates_above, coordinates_beside, coordinates_below])
            if self.is_symbol(*coordinate)
            and self.symbol_map[coordinate] == "*"
        ]

    def get_stars_map(self):
        stars_map = defaultdict(list)
        for part_number in self.part_numbers:
            for star_coordinate in self.get_adjacent_stars(part_number):
                stars_map[star_coordinate].append(part_number)

        return stars_map

    def get_gears(self):
        return {star_coordinate:part_number_list for star_coordinate, part_number_list in self.stars_map.items() if len(part_number_list)==2}


def solve_part1():
    input_lines = get_input()
    game_board = Board(input_lines)
    result = sum(part_number.value for part_number in game_board.part_numbers)
    print(result)

def solve_part2():
    input_lines = get_input()
    game_board = Board(input_lines)
    
    sum_gear_ratios = 0

    for _, part_numbers in game_board.gears.items():
        a, b = part_numbers
        gear_ratio = a.value*b.value
        sum_gear_ratios += gear_ratio

    print(sum_gear_ratios)

if __name__ == "__main__":
    # solve_part1()
    solve_part2()