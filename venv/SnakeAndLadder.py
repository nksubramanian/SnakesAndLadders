class SnakeAndLadder:
    position = 1
    money_available = 500
    all_position = set(range(1, 50))
    snake = [14, 23, 43, 47]
    snake_effect = [2, 8, 41, 37]
    ladder = [5, 12, 16, 19, 35, 40]
    ladder_effect = [10, 26, 29, 33, 36, 45]

    def move(self, dice_roll):
        if (self.position + dice_roll) not in self.all_position:
            self.money_available = self.money_available - 10

        else:
            if self.position + dice_roll in self.snake:
                self.position = self.snake_effect[self.snake.index(self.position + dice_roll)]
                self.money_available = self.money_available - 100
            elif self.position + dice_roll in self.ladder:
                self.position = self.ladder_effect[self.ladder.index(self.position + dice_roll)]
                self.money_available = self.money_available + 100
            else:
                self.position = self.position + dice_roll

    def states(self):
        print("You are in position " + str(self.position) + " and availabe money is " + str(self.money_available))

    def game_declaration(self):
        if self.money_available <= 0:
            print("You lost")
            return -1
        elif self.position == 49:
            print("You won")
            return 1
        else:
            return 0

    def playonemove(self, dice_roll):
        # print("I am right below")
        self.move(dice_roll)
        # print("I am below move")
        self.states()
        return self.game_declaration()