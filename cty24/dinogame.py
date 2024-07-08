width = 12
height = 6
char = 'X'
barrier = '#'

x, y = width // 2, height // 2
barriers = [(0,0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1,0), (1,11), (2,0), (2,11), (3,0), (3,11),(4,0),(4,11),(5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7), (5,8), (5,9), (5,10), (5,11), (2,4), (2,7), (3,8),(3,2),(4,6),(4,3)]


def display_board():
    for row in range(height):
        for col in range(width):
            if (row, col) in barriers:
                print(barrier, end='')
            elif row == y and col == x:
                print(char, end='')
            else:
                print('.', end='')
        print()



while True:
    display_board()
    
    
    move = input("Move (WASD to move, Q to quit): ").lower()
    
    if move == 'w' and y > 0 and (y - 1, x) not in barriers:
        y -= 1
    elif move == 's' and y < height - 1 and (y + 1, x) not in barriers:
        y += 1
    elif move == 'a' and x > 0 and (y, x - 1) not in barriers:
        x -= 1
    elif move == 'd' and x < width - 1 and (y, x + 1) not in barriers:
        x += 1
    elif move == 'q': 
        break
    else:
        print("error chose again")