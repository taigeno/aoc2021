with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def part_one():
    numbers = None
    boards = []
    b = []
    for line in lines:
        if numbers == None:
            numbers = [int(x) for x in line.split(",")]
        elif line:
            b.append([int(x) for x in line.split()])
        elif b:
            boards.append(BingoBoard(b))
            b = []
    boards.append(BingoBoard(b))

    for number in numbers:
        for board in boards:
            result = board.draw_number(number)
            if result > 0:
                print(result * number)
                return

def part_two():
    numbers = None
    boards = []
    b = []
    for line in lines:
        if numbers == None:
            numbers = [int(x) for x in line.split(",")]
        elif line:
            b.append([int(x) for x in line.split()])
        elif b:
            boards.append(BingoBoard(b))
            b = []
    boards.append(BingoBoard(b))

    last_winner = None
    for number in numbers:
        for board in boards:
            result = board.draw_number(number)
            if result > 0:
                last_winner = result * number
    print(last_winner)

class BingoBoard:
    def __init__(self, input):
        self.grid = input
        self.fill =[[False for x in range(5)] for y in range(5)]
        self.won = False

    def draw_number(self, number):
        if self.won:
            return 0

        for r in range(5):
            for c in range(5):
                if self.grid[r][c] == number:
                    self.fill[r][c] = True
        if self.check_winner():
            self.won = True
            return self.get_winning_number()
        else:
            return 0

    def check_winner(self):
        #check rows
        for r in range(5):
            winner = True
            for c in range(5):
                if not self.fill[r][c]:
                    winner = False

            if winner:
                return True

        #check columns
        for c in range(5):
            winner = True
            for r in range(5):
                if not self.fill[r][c]:
                    winner = False

            if winner:
                return True

        return False
        
    def get_winning_number(self):
        sum = 0
        for r in range(5):
            for c in range(5):
                if not self.fill[r][c]:
                    sum += self.grid[r][c]

        return sum

    def __repr__(self):
        return f"BingoBoard: {self.grid}, {self.fill}"

part_one()
part_two()
