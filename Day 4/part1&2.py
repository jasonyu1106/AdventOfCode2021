class Board:
    def __init__(self, n):
        self.size = n
        self.data = {}
        self.rowCount = [0 for i in range(5)]
        self.colCount = [0 for i in range(5)]

    def mark_number(self, number: int):
        if number in self.data:
            coordinates = self.data.get(number)
            self.rowCount[coordinates[0]] += 1
            self.colCount[coordinates[1]] += 1
            del self.data[number]
            return self.check_bingo(coordinates[0], coordinates[1])
        return False

    def check_bingo(self, row: int, col: int):
        return self.rowCount[row] == self.size or self.colCount[col] == self.size

    def add_number(self, num: int, row: int, col: int):
        self.data[num] = (row, col)


def find_first_winning_board(numbers: [], boards: []):
    for num in numbers:
        for index, board in enumerate(boards):
            if board.mark_number(num):
                # BINGO
                sum = 0
                for key in board.data.keys():
                    sum += key
                print("First Winning board: ", index, "\tWinning Number: ", num, "\tFinal Score: ", sum * num)
                return


def find_last_winning_board(numbers: [], boards: []):
    winning_sum = -1
    winning_num = -1
    for num in numbers:
        remaining = []
        for index, board in enumerate(boards):
            if board.mark_number(num):
                # BINGO
                winning_num = num
                winning_sum = 0
                for key in board.data.keys():
                    winning_sum += key
            else:
                remaining.append(board)
        boards = remaining
    print("Last Winning Number: ", winning_num, "\tFinal Score: ", winning_sum * winning_num)


with open("bingo_data.txt", "r") as f:
    numbers = f.readline().strip().split(",")
    numbers = [int(num) for num in numbers]

    boards = []
    for line in f:
        if not line.strip():
            board = Board(5)
            for i in range(5):
                rowNums = f.readline().strip().split(" ")
                rowNums = list(filter(None, rowNums))
                rowNums = [int(num) for num in rowNums]
                for j in range(5):
                    board.add_number(rowNums[j], i, j)
            boards.append(board)

find_first_winning_board(numbers, boards)
find_last_winning_board(numbers, boards)








