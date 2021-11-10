import random
import numpy as np

X_FIELD = 'X X X\nX X X\nX X X'

class Mine_Field(object):
    def __init__(self):
        self.field = np.array([[random.randint(0,1), random.randint(0,1), random.randint(0,1)],
                                [random.randint(0,1), random.randint(0,1), random.randint(0,1)],
                                [random.randint(0,1), random.randint(0,1), random.randint(0,1)]])

class Mine_Game(object):
    
    def __init__(self):
        self.game_field = Mine_Field().field
        print("Starting game:")
        print(X_FIELD)
        self.play_game()
    
    def play_game(self):
        try:
            self.x = int(input("Enter x coordinate to make a step:")) - 1
            self.y = int(input("Enter y coordinate to make a step:")) - 1
        
            if self.game_field[self.x, self.y] == 1:
                print("You lose")
                exit()
            else:
                self.game_field[self.x, self.y] = 1
                if not np.where(self.game_field == 0):
                    print("Good game")
                    exit()
                print('Good step. Keep playing')
                print(X_FIELD)
                print(f'There are {9 - np.count_nonzero(self.game_field)} blocks left to be mined')
                if np.count_nonzero(self.game_field) == 9:
                    print("Good game")
                    exit()
                self.play_game()
            print(self.game_field)
        except IndexError:
            print("Incorrect coordinates.The field is square and there are 9 blocks on it. Try again")
            self.play_game()

        

if __name__ == "__main__":
    Mine_Game()

