class MazeGame:
    def __init__(self, game_board, move, play):
        self.game_board = game_board()
        self.move = move()
        self.play = play()
        self.x, self.y = 1, 1  # Start position
        self.exit_x, self.exit_y = 18, 8  # Exit position
        self.maze = [
            "####################",
            "#S       #        E#",
            "# ###### ####### ###",
            "#      #        #  #",
            "###### ######## # ##",
            "#    #        # #  #",
            "# ## ##### ## # ####",
            "# ##      # ##     #",
            "##### ######## #####",
            "####################"
        ]

    def game_board(self):
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if row == self.y and col == self.x:
                    print('X', end='')
                else:
                    print(self.maze[row][col], end='')
            print()

    def move(self, direction):
        if direction == 'w' and self.maze[self.y - 1][self.x] != '#':
            self.y -= 1
        elif direction == 's' and self.maze[self.y + 1][self.x] != '#':
            self.y += 1
        elif direction == 'a' and self.maze[self.y][self.x - 1] != '#':
            self.x -= 1
        elif direction == 'd' and self.maze[self.y][self.x + 1] != '#':
            self.x += 1

    def play(self):
        while True:
            self.game_board()
            if self.x == self.exit_x and self.y == self.exit_y:
                print("Congratulations! You've reached the exit!")
                break

            move = input("Move (WASD to move, Q to quit): ").lower()
            if move == 'q':
                break

            self.move(move)
            print("\n" * 50)


game = MazeGame()
game.play()
