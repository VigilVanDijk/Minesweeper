import numpy as np
import random

def get_backboard():
    backboard = np.ones((1,5,5), dtype=str)
    return backboard

class Mines:
    x_cord:int = None
    y_cord:int = None
    is_Active:bool = False

class Player:
    name:str= None
    lives:int = 0
    is_Alive:bool = False
    def __init__(self, name):
        self.name = name

def get_mines():
    m1=Mines()
    m2=Mines()
    m3=Mines()
    mines_array=[m1,m2,m3]
    for i in range(len(mines_array)):
        x_cord_new = random.randint(0,4)
        y_cord_new = random.randint(0,4)
        mines_array[i].x_cord = x_cord_new
        mines_array[i].y_cord = y_cord_new
        mines_array[i].is_Active = True
    return mines_array

def create_player():
    name = str(input("Enter your name:"))
    current_player = Player(name)
    current_player.is_Alive = True
    current_player.lives = 3
    print(f"Player's name is set to {name} \n")
    return current_player
 
def checkDeath(lives:int):
    if(lives == 0):
        return True
    else:
        return False
    
##Entry point to the game
print("\nMINESWEEPER (almost)\n")
    
def start_game():
    ip=str(input("To play, hit 'f', to exit, hit 'e' : "))
    if(ip=='f'):
        backboard = get_backboard()
        mine_array = get_mines()
        print(mine_array[0].x_cord, mine_array[0].y_cord)
        print(mine_array[1].x_cord, mine_array[1].y_cord)
        print(mine_array[2].x_cord, mine_array[2].y_cord)
        player = create_player()
        def hit_checker():
            mine_hit:bool = False
            for i in range(len(mine_array)):
                if(x_c == mine_array[i].x_cord and y_c == mine_array[i].y_cord and mine_array[i].is_Active == True):
                    player.lives = player.lives - 1
                    mine_hit = True
                    mine_loc_x = mine_array[i].x_cord
                    mine_loc_y = mine_array[i].y_cord
                    mine_array[i].is_Active = False
                    
            if(mine_hit):
                if(checkDeath(player.lives)):
                    print("Status : Failure!!\n")
                    print(f"You encountered a mine and died. No of lives left : {player.lives}\n")
                    print(f"Mine encountered at coordinates ({mine_loc_x} ,{mine_loc_y}), marked by an '0' on the backboard")
                    backboard[0][mine_loc_x][mine_loc_y] = 0
                    print(f"\n{backboard[0]}")
                    ans = str(input("\nDo you want to play again? Answer in y/n : "))
                    if(ans=='y'):
                        start_game()
                    else:
                        print("Exiting")
                        exit()
                else:
                    print("Status : Failure!!\n")
                    print(f"You encountered a mine. No of lives left : {player.lives}")
                    print(f"\nMine encountered at coordinates ({mine_loc_x} ,{mine_loc_y}), marked by an '0' on the backboard")
                    backboard[0][mine_loc_x][mine_loc_y] = 0
                    print(f"\nCurrent status of backboard: \n{backboard[0]}")
            else:               
                print("Status : Success!!\n")
                print(f"Lives Remaining for player  {player.name} : {player.lives}\n")
                print(f"\nCurrent status of backboard: \n{backboard[0]}")
                
        print(f"{backboard[0]}\n")
        print(f"Lives Remaining for player  {player.name} : {player.lives}")
        while True:
            x_c = int(input("Enter the x co-ordinate which you want to hit: "))
            y_c = int(input("Entyer the y co-ordinate which you want to hit: "))
            print(f"\nHitting position ({x_c},{y_c})\n")
            backboard[0][x_c][y_c] = 'X'
            hit_checker()
            
    elif(ip=='e'):
        print("Exiting")
        exit()
    else:
        print("Invalid input dummy\n")
        start_game()

start_game()