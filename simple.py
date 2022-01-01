from random import randint

print('Start!')

blocks = [False, '[1]', '[2]', '[3]', '[4]', '[5]', '[6]', '[7]', '[8]', '[9]']


def printBoard():
    print('---------')
    print(blocks[1]+blocks[2]+blocks[3])
    print(blocks[4]+blocks[5]+blocks[6])
    print(blocks[7]+blocks[8]+blocks[9])
    print('---------')

printBoard()


def isBoardFull():
    if (blocks[1] != '[1]' and blocks[2] != '[2]' and blocks[3] != '[3]'
        and blocks[4] != '[4]' and blocks[5] != '[5]' and blocks[6] != '[6]'
            and blocks[7] != '[7]' and blocks[8] != '[8]' and blocks[9] != '[9]'):
        return True
    else:
        return False


def isBlockFree(block):
    if blocks[block] != '[X]' and blocks[block] != '[O]':
        return True
    else:
        return False


gameRun = True
while gameRun:
    if isBoardFull() != True:
        userChoiseRepeat = True
        while userChoiseRepeat:
            userChoise = int(input('Please select a free block: '))
            if isBlockFree(userChoise) == True:
                blocks[userChoise] = '[X]'
                userChoiseRepeat = False
            else:
                print('The selected block is not free.')
        printBoard()
        computerChoiseRepeat = True
        while computerChoiseRepeat:
            computerChoise = randint(1, 9)
            if isBlockFree(computerChoise) == True:
                blocks[computerChoise] = '[O]'
                computerChoiseRepeat = False
        printBoard()
        if ((blocks[1] == '[X]' and blocks[2] == '[X]' and blocks[3] == '[X]')
            or (blocks[4] == '[X]' and blocks[5] == '[X]' and blocks[6] == '[X]')
            or (blocks[7] == '[X]' and blocks[8] == '[X]' and blocks[9] == '[X]')
            or (blocks[1] == '[X]' and blocks[4] == '[X]' and blocks[7] == '[X]')
            or (blocks[2] == '[X]' and blocks[5] == '[X]' and blocks[8] == '[X]')
            or (blocks[3] == '[X]' and blocks[6] == '[X]' and blocks[9] == '[X]')
            or (blocks[1] == '[X]' and blocks[5] == '[X]' and blocks[9] == '[X]')
                or (blocks[3] == '[X]' and blocks[5] == '[X]' and blocks[7] == '[X]')):
            gameRun = False
            print('You win!')
        elif ((blocks[1] == '[O]' and blocks[2] == '[O]' and blocks[3] == '[O]')
            or (blocks[4] == '[O]' and blocks[5] == '[O]' and blocks[6] == '[O]')
            or (blocks[7] == '[O]' and blocks[8] == '[O]' and blocks[9] == '[O]')
            or (blocks[1] == '[O]' and blocks[4] == '[O]' and blocks[7] == '[O]')
            or (blocks[2] == '[O]' and blocks[5] == '[O]' and blocks[8] == '[O]')
            or (blocks[3] == '[O]' and blocks[6] == '[O]' and blocks[9] == '[O]')
            or (blocks[1] == '[O]' and blocks[5] == '[O]' and blocks[9] == '[O]')
            or (blocks[3] == '[O]' and blocks[5] == '[O]' and blocks[7] == '[O]')):
            gameRun = False
            print('You lose!')
    else:
        gameRun = False
        print('Tie!')
        
print('End!')
