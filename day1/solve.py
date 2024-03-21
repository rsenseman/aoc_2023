import sys

DIGITS = set([str(val) for val in range(10)])
DIGIT_WORDS = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

def get_input(filename=sys.argv[1]):
    with open(filename) as f:
        for l in f.readlines():
            yield l.strip()

def get_first_and_last_digit(input_string):
    digits = ""
    # get first digit
    for val in input_string:
        if val in DIGITS:
            digits += val
            break

    for val in input_string[::-1]:
        if val in DIGITS:
            digits += val
            break 

    if len(digits) != 2:
        debug_info = {
            "input_string": input_string,
            "digits": digits,
        }
        raise ValueError(f"digits expected to have length 2. debug: {debug_info}")

    return int(digits)

def solve_part1():
    lines = get_input()

    two_digits_map = map(get_first_and_last_digit, lines)
    total = sum(two_digits_map)
    print(total)

def get_first_digit(input_string):
    for i in range(len(input_string)):
        front_slice = input_string[i:]
        for digit_word in DIGIT_WORDS:
            if front_slice.startswith(digit_word):
                first_digit = str(DIGIT_WORDS[digit_word])
                return first_digit

def get_last_digit(input_string):
    for i in range(len(input_string)-1, -1, -1):
        back_slice = input_string[i:]
        for digit_word, digit in DIGIT_WORDS.items():
            if back_slice.find(digit_word) != -1:
                first_digit = str(digit)
                return first_digit

def get_first_and_last_digit_part2(input_string):
    first_digit = get_first_digit(input_string)
    last_digit = get_last_digit(input_string)    
    return int(first_digit + last_digit)

def solve_part2():
    lines = get_input()

    two_digits_map = [get_first_and_last_digit_part2(line) for line in lines]
    total = sum(two_digits_map)
    print(total)

if __name__ == "__main__":
    # solve_part1()
    solve_part2()