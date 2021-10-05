import numpy as np
import random
from time import sleep

class user_to_computer:
    board=np.array([' ',' ',' ',' ',' ',' ',' ',' ',' '],dtype=str)
    players={'O':"",'X':""}
    player_coin=''
    computer_coin=''
    places=list(range(1,10))
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

    def col_check(self,coin):

        t=self.board
        for i in range(3):
            if(t[i]==t[i+3]==t[i+6]==coin):
                return 1
        return 0

    def row_check(self,coin):
        t=self.board
        postion=0
        for i in range(3):
            if(t[postion]==t[postion+1]==t[postion+2]==coin):
                return 1
            postion+=3
        return 0

    def diagonal_check(self,coin):
        t=self.board
        if(t[0]==t[4]==t[8]==coin):
            return 1
        if(t[2]==t[4]==t[6]==coin):
            return 1
        return 0
    def evaluate(self):
        for i in ["X","O"]:
            if (self.col_check(i) or self.row_check(i) or self.diagonal_check(i)):
                return self.players[i]
        return 0

    def user_turn(self):
        print("Hey",self.players[player_coin],"it's your turn")
        selected=int(input("Enter The  Postion "))
        if selected in self.places:
            self.board[selected-1]=self.player_coin

        #self.places=np.delete(self.places, np.where(self.places == selected))

        self.places.remove(selected)
        self.display_board()


    def computer_turn(self):
        temp=random.randint(0,len(self.places)-1)
        computer_option=self.places[temp-1]
        print("It computer turn")
        print("I choosen postion ",computer_option)
        self.board[computer_option-1]=self.computer_coin
        self.places.remove(computer_option)
        #self.places=np.delete(self.places, np.where(self.places == computer_option))
        #self.places=np.delete(self.places,temp-1)
        sleep(2)
        self.display_board()

    def play(self):
        self.display_board()
        win=-1
        while(len(self.places)!=0):
            self.user_turn()
            print("-------------------------------------------")
            win=self.evaluate()
            if(win!=0 and win!=-1):
                return win
            elif win==0 and len(self.places)==0:
                break
            self.computer_turn()
            print("-------------------------------------------")
            win=self.evaluate()
            if(win!=-1 and win!=0):
                return win
        return "Draw"


class user_to_user(user_to_computer):
    player1_coin,player2_coin="X","O"

    def set_player_coins(self,player1,player2):
        self.players={"X":player1,"O":player2}

    def user1_turn(self):
        print("Hey",self.players[self.player1_coin],"it's your turn")
        selected=int(input("Enter The  Postion "))
        if selected in self.places:
            self.board[selected-1]=self.player1_coin

        #self.places=np.delete(self.places, np.where(self.places == selected))

        self.places.remove(selected)
        self.display_board()

    def user2_turn(self):
        print("Hey",self.players[self.player2_coin],"it's your turn")
        selected=int(input("Enter The  Postion "))
        if selected in self.places:
            self.board[selected-1]=self.player2_coin

        #self.places=np.delete(self.places, np.where(self.places == selected))

        self.places.remove(selected)
        self.display_board()

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
if type_of_game==1:
    s=user_to_computer()
    player_name=input("Enter your name : ")
    player_coin=input("Enter your coin either 'X' or 'O' :")
    s.set_player_coins(player_name,player_coin)
    results=s.play()
    if results!="Draw":
        print("winner is ",results)
    else:
        print("Draw")
else:
    s=user_to_user()
    player1=input("Enter you player1 name : ")
    player2=input("Enter you player2 name : ")
    s.set_player_coins(player1,player2)
    results=s.play()
    if results!="Draw":
        print("winner is ",results)
    else:
        print("Draw")


