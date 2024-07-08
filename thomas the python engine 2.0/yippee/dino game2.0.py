class dinoGame:
    def __init__(self):
        self.x, self.y = 1, 1
        self.obj_x, self.obj_y = 2, 1
        self.win_x, exit.win_y = 18, 8

        self.grid = [
            "##################",
            "#S O     #      E#",
            "# ##### ###### ###",
            "#     #       #  #",
            "##### ####### # ##",
            "#   #       # #  #",
            "#### ######## ####",
            "##################"

        ]

def game_board(self):
    for row in range(len(self.grid)):
        for col in range(len(self.grid[row])):
            if row == self.y and col == self.x:
                print("&", end= '')
            elif row == self.obj_y and col == self.obj_x:
                print("$, end= '")
            else:
                print(self.grid[row][col], end= '')
                
            print()

def move(self, dx, dy):
    new_x, new_y = self.x +dx, self.y +dy
    if self.grid[new_y][new_x] != '#':
        if new_x == self.obj_x and new_y == self.obj_y:
            obj_new_x , obj_new_y = self.obj_y
            if self.grid[obj_new_y][obj_new_x] != '#':
                self.obj_x, self.obj_y = obj_new_x, obj_new_y
        else:
            self.x, self.y = new_x, new_y

def play(self):
    while True:
        self.game_board()
        if self.x == self.exit_x and self.y == self.exit_y:
            print("yippee !!! you won")
            break
    
        move = input("use wasd to move and q to quit").lower

        if move == 'q':
            break


        if move == 'w':
            self.move(0,-1)
        elif move == 's':
            self.move(0,1)
        elif move == 'a':
            self.move(-1,0)
        elif move == 's':
            self.move(1,0)