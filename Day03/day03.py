with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def part_one():
    half = len(lines) / 2
    digits = [0] * len(lines[0])
    for line in lines:
        for i, num in enumerate(line):
            digits[i] += int(num)

    gamma = ""
    epsilon = ""
    for digit in digits:
        if digit > half:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    print(gamma, epsilon)
    print(int(gamma, 2) * int(epsilon, 2))

def part_two():
    gamma = find_last_item(lines, True)
    epsilon = find_last_item(lines, False)
    print(gamma, epsilon)
    print(int(gamma[0], 2) * int(epsilon[0], 2))

def find_last_item(input, most_common):
    index = 0
    while len(input) > 1:
        input = get_remaining(input, index, most_common)
        index += 1

    return input

def get_remaining(input, index, most_common):
    half1 = []
    half2 = []
    for item in input:
        if item[index] == "0":
            half1.append(item)
        else:
            half2.append(item)
    
    if len(half1) > len(half2):
        return half1 if most_common else half2
    else:
        return half2 if most_common else half1



part_one()
part_two()
