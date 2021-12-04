with open('input.txt', 'r') as f:
    data = f.readlines()
    data = [x.strip() for x in data if x != '\n']

nums = [int(n) for n in data[0].split(',')]
data = data[1:]

board = []
boards = []

for i, line in enumerate(data):
    board.append([int(n) for n in line.split()])

    if (i % 5 == 4):
        boards.append(board)
        board = []

def checkBoard(board):
    for row in board:
        if row.count(-1) == 5:
            return True
    
    for col in zip(*board): 
        if col.count(-1) == 5:
            return True

    return False

def scoreBoard(board):
    ret = 0
    for row in board:
        for item in row:
            if item != -1:
                ret += item

    return ret

def playGame():
    winners = [False] * len(boards)
    for n in nums:
        for board in boards:
            for row in board:
                for i, x in enumerate(row):
                    if x == n:
                        row[i] = -1

        for i, board in enumerate(boards):
            if checkBoard(board):
                winners[i] = True

                if winners.count(True) == len(winners):
                    print(n * scoreBoard(board))
                    return

playGame()










