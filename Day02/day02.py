with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def part_one():
    depth = 0
    hor = 0
    for line in lines:
        args = line.split()
        command = args[0]
        mag = int(args[1])
        if command == "forward":
            hor += mag
        elif command == "down":
            depth += mag
        elif command == "up":
            depth -= mag
    print(depth * hor)


def part_two():
    depth = 0
    aim = 0
    hor = 0
    for line in lines:
        args = line.split()
        command = args[0]
        mag = int(args[1])
        if command == "forward":
            hor += mag
            depth += aim * mag
        elif command == "down":
            aim += mag
        elif command == "up":
            aim -= mag
    print(depth * hor)

part_one()
part_two()
