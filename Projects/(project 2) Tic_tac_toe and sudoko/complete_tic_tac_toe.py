'''
PROGRAM DESCRIPITON:
	With using Python Numpy module create a game of TIC TAC TOE.
    Please consider the following points while creating your project :-
        1) Use only the Numpy module not anything else of Python Data Science.
        2) Write your program using the OOPS concept of Python
'''

# PROGRAMMED BY : Badam Jwala Sri Hari
# MAIL ID       : jwalasrihari1330@gmail.com
# DATE          : 04-09-2021
# PYTHON VERSION: 3.9.7
# NUMPY VERSION : 1.21.2
# CAVEATS       : None
# LICENSE       : None



import numpy as np
import random
from time import sleep


# USER WITH COMPUTER
class user_to_computer:

    # Board is initialized with empty spaces
    board=np.array([' ',' ',' ',' ',' ',' ',' ',' ',' '],dtype=str)

    # This dictionary is used to know coins of players
    players={'O':"",'X':""}
    player_coin=''
    computer_coin=''

    # places list contains the postion where the coins is not places
    places=list(range(1,10))

    def rules(self):
        print()
        print("****Rules****")
        print("User has to choose the postion between 1 to 9")
        print("Every number representing a postion in row wise")
        print("if a coin in row ,column and diagonally same then the respected player will win")
        print("Start the game by entering the Details")
        print()
    # Set the coins to the user and computer
    def set_player_coins(self,name,player_coin):
        if player_coin=='X':
            self.player_coin=player_coin
            self.computer_coin='O'
            self.players['X']=name
            self.players['O']="computer"
        else:
            self.player_coin=player_coin
            self.computer_coin='X'
            self.players["O"]=name
            self.players["X"]="computer"

    # Displays the board
    def display_board(self):

        # Without writing self.board again and again
        # Self.board is assigned to variable 't'
        t=self.board
        print("\n")
        print("\t     |     |")
        print("\t   {0} |  {1}  | {2} ".format(t[0],t[1],t[2]))
        print('\t_____|_____|_____')

        print("\t     |     |")
        print("\t   {0} |  {1}  | {2} ".format(t[3],t[4],t[5]))
        print('\t_____|_____|_____')

        print("\t     |     |")

        print("\t   {0} |  {1}  | {2} ".format(t[6],t[7],t[8]))
        print("\t     |     |")
        print("\n")

    # Checks column wise whether coin present in all 3 positions or not
    def col_check(self,coin):

        t=self.board
        for i in range(3):
            if(t[i]==t[i+3]==t[i+6]==coin):
                return 1
        return 0

    # Checks row wise whether coin present in all 3 positions or not
    def row_check(self,coin):
        t=self.board
        postion=0
        for i in range(3):
            if(t[postion]==t[postion+1]==t[postion+2]==coin):
                return 1
            postion+=3
        return 0

    # Checks 2 diagonals
    def diagonal_check(self,coin):
        t=self.board
        if(t[0]==t[4]==t[8]==coin):
            return 1
        if(t[2]==t[4]==t[6]==coin):
            return 1
        return 0

    # evaluate calls the above three functions with respective coins
    # and check whether the game is over or not if over it will returns won player
    def evaluate(self):
        for i in ["X","O"]:
            if (self.col_check(i) or self.row_check(i) or self.diagonal_check(i)):
                return self.players[i]
        return 0

    # User turn
    def user_turn(self):
        print("Hey",self.players[self.player_coin],"it's your turn")
        selected=int(input("Enter The  Postion "))

        if selected in self.places:

            # Placing coin on board
            self.board[selected-1]=self.player_coin
        else:
            print("wrong move \n please choose again")
            selected=int(input("Enter The  Postion "))
            if selected in self.places:
                self.board[selected-1]=self.player_coin

        # Removing from the places as the coin is placed
        self.places.remove(selected)
        self.display_board()


    def computer_turn(self):
        # Generating random index
        temp=random.randint(0,len(self.places)-1)
        # Randomly generated index in places list is choose as computer option
        computer_option=self.places[temp-1]
        print("It computer turn")
        print("I choosen postion ",computer_option)
        self.board[computer_option-1]=self.computer_coin
        self.places.remove(computer_option)
        # Sleep to just wait for a while
        sleep(2)
        self.display_board()

    def play(self):
        win=-1

        # if no positions left to place coins and win is not occurced that means is  the game DRAW
        while(len(self.places)!=0):
            self.user_turn()
            print("-------------------------------------------")
            # After user Turn we have to evalute the board whether anybody won or not
            win=self.evaluate()
            if(win!=0 and win!=-1):
                return win
            elif win==0 and len(self.places)==0:
                break

            self.computer_turn()
            print("-------------------------------------------")
            # After computer Turn we are evaluting again
            win=self.evaluate()
            if(win!=-1 and win!=0):
                return win
        return "Draw"

# USER WITH USER
# we are inherting the user_to_computer property(which is best way to reuse the written code)
class user_to_user(user_to_computer):
    player1_coin,player2_coin="X","O"

    # Setting the coins of two users
    def set_player_coins(self,player1,player2):
        self.players={"X":player1,"O":player2}

    # Executed when the turn is 1st user's
    def user1_turn(self):
        print("Hey",self.players[self.player1_coin],"it's your turn")
        selected=int(input("Enter The  Postion "))
        if selected in self.places:
            self.board[selected-1]=self.player1_coin
        self.places.remove(selected)
        self.display_board()
    # Executed when the turn is 1st user's
    def user2_turn(self):
        print("Hey",self.players[self.player2_coin],"it's your turn")
        selected=int(input("Enter The  Postion "))
        if selected in self.places:
            self.board[selected-1]=self.player2_coin
        self.places.remove(selected)
        self.display_board()

    # Overriding the Base class method (rewriting the property)
    def play(self):
        self.display_board()
        win=-1
        while(len(self.places)!=0):
            self.user1_turn()
            print("-------------------------------------------")
            win=self.evaluate()
            if(win!=0 and win!=-1):
                return win
            elif win==0 and len(self.places)==0:
                break
            self.user2_turn()
            print("-------------------------------------------")
            win=self.evaluate()
            if(win!=-1 and win!=0):
                return win
        return "Draw"


type_of_game=int(input("Choose the Type of Game \n 1.User Vs Computer \n 2.User Vs User \n Select your Option : "))
# if user wants to player with computer
if type_of_game==1:
    s=user_to_computer()
    s.rules()
    player_name=input("Enter your name : ")
    player_coin=input("Enter your coin either 'X' or 'O' :")
    s.set_player_coins(player_name,player_coin)
    results=s.play()
    if results!="Draw":
        print("winner is ",results)
    else:
        print("Draw")
# if user to want to play with another user
elif type_of_game==2:
    s=user_to_user()
    s.rules()
    player1=input("Enter you player1 name : ")
    player2=input("Enter you player2 name : ")
    s.set_player_coins(player1,player2)
    results=s.play()
    if results!="Draw":
        print(results,"Won the game")
    else:
        print("Draw")
else:
    print("choosen number was not in option \n please choose again")


'''
output

#USER VS COMPUTER

Choose the Type of Game 
 1.User Vs Computer
 2.User Vs User
 Select your Option : 1

****Rules****
User has to choose the postion between 1 to 9
Every number representing a postion in row wise
if a coin in row ,column and diagonally same then the respected player will win
Start the game by entering the Details

Enter your name : Jwala
Enter your coin either 'X' or 'O' :O
Hey Jwala it's your turn
Enter The  Postion 3


             |     |
             |     | O
        _____|_____|_____
             |     |
             |     |
        _____|_____|_____
             |     |
             |     |
             |     |


-------------------------------------------
It computer turn
I choosen postion  5


             |     |
             |     | O
        _____|_____|_____
             |     |
             |  X  |
        _____|_____|_____
             |     |
             |     |
             |     |


-------------------------------------------
Hey Jwala it's your turn
Enter The  Postion 2


             |     |
             |  O  | O
        _____|_____|_____
             |     |
             |  X  |
        _____|_____|_____
             |     |
             |     |
             |     |


-------------------------------------------
It computer turn


             |     |
             |  O  | O
        _____|_____|_____
             |     |
             |  X  | X
        _____|_____|_____
             |     |
             |     |
             |     |


-------------------------------------------
Hey Jwala it's your turn
Enter The  Postion 1


             |     |
           O |  O  | O
        _____|_____|_____
             |     |
             |  X  | X
        _____|_____|_____
             |     |
             |     |
             |     |


-------------------------------------------
winner is  Jwala


#USER VS USER

Choose the Type of Game 
 1.User Vs Computer
 2.User Vs User
 Select your Option : 2

****Rules****
User has to choose the postion between 1 to 9
Every number representing a postion in row wise
if a coin in row ,column and diagonally same then the respected player will win
Start the game by entering the Details

Enter you player1 name : Jwala 
Enter you player2 name : Sri Hari


             |     |
             |     |
        _____|_____|_____
             |     |
             |     |
        _____|_____|_____
             |     |
             |     |
             |     |


Hey Jwala  it's your turn
Enter The  Postion 1


             |     |
           X |     |
        _____|_____|_____
             |     |
             |     |
        _____|_____|_____
             |     |
             |     |
             |     |


-------------------------------------------
Hey Sri Hari it's your turn
Enter The  Postion 5


             |     |
           X |     |
        _____|_____|_____
             |     |
             |  O  |
        _____|_____|_____
             |     |
             |     |
             |     |


-------------------------------------------
Hey Jwala  it's your turn
Enter The  Postion 2


             |     |
           X |  X  |
        _____|_____|_____
             |     |
             |  O  |
        _____|_____|_____
             |     |
             |     |
             |     |


-------------------------------------------
Hey Sri Hari it's your turn
Enter The  Postion 3


             |     |
           X |  X  | O
        _____|_____|_____
             |     |
             |  O  |
        _____|_____|_____
             |     |
             |     |
             |     |


-------------------------------------------
Hey Jwala  it's your turn
Enter The  Postion 4


             |     |
           X |  X  | O
        _____|_____|_____
             |     |
           X |  O  |
        _____|_____|_____
             |     |
             |     |
             |     |


-------------------------------------------
Hey Sri Hari it's your turn
Enter The  Postion 7


             |     |
           X |  X  | O
        _____|_____|_____
             |     |
           X |  O  |
        _____|_____|_____
             |     |
           O |     |
             |     |


-------------------------------------------
Sri Hari Won the game
'''
