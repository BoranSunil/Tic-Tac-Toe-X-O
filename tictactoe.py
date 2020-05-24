#Global Variables
player1 = "X"
player2 = "O"
#Game_Board
board = [ "-","-","-",
          "-","-","-",
         "-","-","-"]
player = "X"   
count = 0   
game_over = False

def reference():
    print(" 1 | 2 | 3 ")
    print(" 4 | 5 | 6 ")
    print(" 7 | 8 | 9 ")
    
def display_board():
    print("\n")
    print( " "+board[0] + " | " + board[1] + " | " + board[2]+" ")
    print( " "+board[3] + " | " + board[4] + " | " + board[5]+" ")
    print( " "+board[6] + " | " + board[7] + " | " + board[8]+" ")
    print("\n")

def winsituation():
    #check rows 
    #check conditions for player1
    if((board[0] == board[1]) and (board[1]== board[2]) and (board[0] == player1)):
        print(player1 + "\t" + "wins the game!")
        game_over = True
        return game_over
        
    elif(((board[3] == board[4]) and (board[4]== board[5]) and board[3] == player1)):
        print(player1 + "\t" + "wins the game!")
        game_over = True
        return game_over
        
    elif(((board[6] == board[7]) and (board[7]== board[8]) and board[6] == player1)):
        print(player1 + "\t" + "  wins the game!")    
        game_over = True
        return game_over

    #check conditions for player2
    elif(((board[0] == board[1]) and (board[1]== board[2]) and board[0] == player2)):
        print(player2 + "\t" + "  wins the game!")
        game_over = True
        return game_over
        
    elif(((board[3] == board[4]) and (board[4]== board[5]) and board[3] == player2)):
        print(player2 + "\t" + "  wins the game!")
        game_over = True
        return game_over
        
    elif(((board[6] == board[7]) and (board[7]== board[8]) and board[6] == player2)):
        print(player2 + "\t" + "  wins the game!")   
        game_over = True
        return game_over

    #check columns 
    #check conditions for player1
    if((board[0] == board[3]) and (board[3]== board[6]) and (board[0] == player1)):
        print(player1 + "\t" + "  wins the game!")
        game_over = True
        return game_over 
        
    elif(((board[1] == board[4]) and (board[4]== board[7]) and board[1] == player1)):
        print(player1 + "\t" + "  wins the game!")
        game_over = True
        return game_over 
        
    elif(((board[2] == board[5]) and (board[5]== board[8]) and board[2] == player1)):
        print(player1 + "\t" + "  wins the game!") 
        game_over = True
        return game_over

    #check conditions for player2
    if((board[0] == board[3]) and (board[3]== board[6]) and (board[0] == player2)):
        print(player2 + "\t" + "wins the game!")
        game_over = True
        return game_over
        
    elif(((board[1] == board[4]) and (board[4]== board[7]) and board[1] == player2)):
        print(player2 + "\t" + "wins the game!")
        game_over = True
        return game_over
    
    elif(((board[2] == board[5]) and (board[5]== board[8]) and board[2] == player2)):
        print(player2 + "\t"+"  wins the game!")  
        game_over = True
        return game_over

    
    #check diagonals
     #check conditions for player1
    if((board[0] == board[4]) and (board[4]== board[8]) and (board[0] == player1)):
        print(player1 + "\t"+"wins the game!")
        game_over = True
        return game_over
    elif(((board[2] == board[4]) and (board[4]== board[6]) and board[2] == player1)):
        print(player1 + "\t"+"wins the game!")
        game_over = True
        return game_over

    #check conditions for player1
    if((board[0] == board[4]) and (board[4]== board[8]) and (board[0] == player2)):
        print(player2 + "\t"+"wins the game!")
        game_over = True
        return game_over
    elif(((board[2] == board[4]) and (board[4]== board[6]) and board[2] == player2)):
        print(player2 + "\t"+"wins the game!")
        game_over = True
        return game_over

def tictactoe():
    #Show the initial layout of the board.
    print("Welcome to the command line version of TIC TAC TOE game")
    num=0
    display_board()
    reference()
    while not game_over: 
        ret = winsituation()
        if (ret == True):
            break 
        
        handler()
        t=tie_game()
        if(t == True):
            break
        display_board()
        

def handler():
    print("Choose a position between 1-9 where you want to place your move:")
    pos = input()
    if pos not in ["1","2","3","4","5","6","7","8","9"]:
        pos= input("Enter a valid number")
        
        
    position = int(pos)-1
    
    if ( board[position] != "-" ):
        print("Choose another place")
        handler()
        
    global player
    
    if(player == "X"):
        board[position] = player
        player = "O"
    elif(player == "O"):
        board[position] = player
        player = "X"    
     
    

def tie_game():
    
    global game_over

    if "-" not in board:
        game_over = True
        print("The game is over!IT'S A TIE")
        return game_over
    else:
        game_over = False
        return game_over   

tictactoe()
