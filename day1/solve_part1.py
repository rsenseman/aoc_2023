def get_input(input_file="input.txt"):
    with open(input_file) as f:
        contents = f.readlines()
    return contents

def get_first_and_last_digit(line):
    digits_of_interest = ""
    for char in line:
        if char.isdigit():
            digits_of_interest += char
            break

    for char in line[::-1]:
        if char.isdigit():
            digits_of_interest += char
            break

    return int(digits_of_interest)

def solve():
    lines = get_input()
    line_ints = [get_first_and_last_digit(line) for line in lines]
    line_sum = sum(line_ints)
    return line_sum

if __name__ == '__main__':
    part1_solution = solve()
    print(part1_solution)