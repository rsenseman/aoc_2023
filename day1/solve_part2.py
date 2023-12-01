WORDS_DIGIT_MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
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

DIGIT_WORDS = set(WORDS_DIGIT_MAP.keys())

def get_input(input_file):
    with open(input_file) as f:
        contents = f.readlines()
    return contents

def get_first_and_last_digit(line):
    first_digits = [
        (line.find(word), WORDS_DIGIT_MAP[word])
        for word
        in DIGIT_WORDS
        if word in line
    ]
    assert first_digits, f"No digits found in string: {line}"

    first_digit_item = sorted(first_digits)[0]
    first_digit = first_digit_item[1]

    last_digits = [
        (line.rfind(word), WORDS_DIGIT_MAP[word])
        for word
        in DIGIT_WORDS
        if word in line
    ]
    last_digit_item = sorted(last_digits)[-1]
    last_digit = last_digit_item[1]

    return int(first_digit + last_digit)

def solve(input_file="input.txt"):
    lines = get_input(input_file)
    line_ints = [get_first_and_last_digit(line) for line in lines]
    line_sum = sum(line_ints)
    return line_sum

if __name__ == '__main__':
    part1_solution = solve("input.txt")
    print(part1_solution)