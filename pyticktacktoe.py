import random

board = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

stage = 1


def changeToIndex(position):
    if 0 < position < 10:
        fIndex = int(position / 3)
        if position % 3 == 0:
            fIndex -= 1
        sIndex = int(position - fIndex * 3 - 1)
    return fIndex, sIndex

def displayBoard(board):
    for i in board:
        for j in i:
            print(j, end='  ')
        print(' ')

def playerMark(board, position):
    index = changeToIndex(position)
    board[index[0]][index[1]] = '●'

def isAlreadyMarked(board, position):
    index = changeToIndex(position)
    if board[index[0]][index[1]] in ['●', 'X']:
        return True
    return False

def isCircleMarked(board, position):
    index = changeToIndex(position)
    if board[index[0]][index[1]] == '●':
        return True
    return False

def isDangerous(board):
    #가로 확인
    for i in range(3):
        count = 0
        for j in range(3):
            position = i * 3 + j + 1
            if isCircleMarked(board, position):
                count += 1
        if count == 2:
            return True
    #세로 확인
    for i in range(3):
        count = 0
        

def computerMark(board):
    if stage == 1:
        #1순위: 5
        if not isAlreadyMarked(board, 5):
            index = changeToIndex(5)
            board[index[0]][index[1]] = 'X'
            return
        #2순위: 1, 3, 7, 9
        huboPos = [1, 3, 7, 9]
        while True:
            back = len(huboPos) - 1
            position = huboPos.pop(random.randint(0, back))
            if len(huboPos) == 0:
                break
            if not isAlreadyMarked(board, position):
                index = changeToIndex(position)
                board[index[0]][index[1]] = 'X'
                return
            else:
                continue
    elif stage == 2:
        if isDangerous(board):
            print('I found it!')
    
while True:
    displayBoard(board)

    position = int(input('놓을 위치: '))
    if not isAlreadyMarked(board, position):
        playerMark(board, position)
    else:
        print('이미 마킹 되었습니다')
        continue
    print('\n')

    #displayBoard(board)
    computerMark(board)
    print('\n')

    stage += 1

    
