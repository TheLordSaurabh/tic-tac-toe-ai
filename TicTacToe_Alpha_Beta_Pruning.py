'''
Author : CS20B1056 SAURABH GUPTA
Course : AI Lab

Topic : TicTacToe - using Alpha Beta pruning

'''

#Limits
inf  = 1000000000
ninf = -1000000000

#if player wins then return 1, 1 for opponent wins and 0 if draw
def checkWin(state,player) :
    n = 3
    #checking rows
    for i in range(n) :
        if(state[i][0] == state[i][1] and state[i][1] == state[i][2]):
            if(state[i][0] == getOpponent(player)):
                return -1
            if (state[i][0] == player):
                return 1
                
    #checking columns
    for i in range(n) :
        if(state[0][i] == state[1][i] and state[1][i] == state[2][i]):
            if(state[0][i] == getOpponent(player)):
                return -1
            if (state[0][i] == player):
                return 1

    #checking diagnols
        #top left - bottom right
        if(state[0][0] == state[1][1] and state[1][1] == state[2][2]):
            if(state[0][0] == getOpponent(player)):
                return -1
            if(state[0][0] == player):
                return 1
        #top right - bottom left
        if(state[0][2] == state[1][1] and state[2][0] == state[1][1]):
            if(state[0][2] == getOpponent(player)):
                return -1
            if(state[0][2] == player):
                return 1 
    return 0

#check if tic tac toe is completely filled
def allDone(state):
    for i in range(3):
        for j in range(3):
            if(state[i][j]=='-'):
                return False
    return True

#get opponent player
def getOpponent(player) :
    if player == 'X':
        return 'O'
    else :
        return 'X'

#class of max node
class MaxNode :
    def __init__(self,state,player,main_player,parent_beta = inf) :
        self.main_player = main_player
        self.parent_beta = parent_beta
        self.player = player
        self.opponent = getOpponent(self.player)
        self.alpha = ninf
        self.state = list(state)
        self.n = len(self.state)
        self.createBranches()
        
    def createBranches(self):
        if(allDone(self.state)):
            self.alpha = checkWin(self.state,self.main_player)
            return self.alpha
        
        temp = list(self.state)
        for i in range(3) :
            for j in range(3) :
                self.state = list(temp) 
                #Pruning happens when current alpha is greater than the parent beta
                if self.parent_beta < self.alpha  :
                    return self.alpha
                #Exploring the new search trees
                if (self.state[i][j] == '-'):

                    self.state[i][j] = self.player #Introducing new move at (i,j) position inplace of '-'
                    minnode = MinNode(self.state,self.opponent,self.main_player,self.alpha)
                    self.state[i][j] = '-' #Removing the introduced Move

                    if(minnode.beta > self.alpha) :
                        self.alpha = minnode.beta

        return self.alpha
        

class MinNode :
    def __init__(self,state,player,main_player,parent_alpha = ninf) :
        self.main_player = main_player
        self.parent_alpha = parent_alpha
        self.player = player
        self.opponent = getOpponent(self.player)
        self.beta = inf
        self.state = list(state)
        self.n = len(self.state)
        self.createBranches()
        
    def createBranches(self) :
        if(allDone(self.state)):
            self.beta = checkWin(self.state,self.main_player)
            return self.beta

        for i in range(3) :
            for j in range(3) :
                
                #Pruning happens when current beta is less than the parent alpha or alphas of all the alpha nodes
                if self.parent_alpha > self.beta  :
                    return self.beta
                
                #Exploring the new search trees
                if (self.state[i][j] == '-'):
                    self.state[i][j] = self.player #Introducing new move at (i,j) position inplace of '-'
                    maxnode = MaxNode(self.state,self.opponent,self.main_player,self.beta)
                    self.state[i][j] = '-' #Removing the introduced Move
                    if(maxnode.alpha < self.beta) :
                        self.beta = maxnode.alpha
            
        return self.beta

def getResult(value) :
    if value == 1:
        return ("1 - Win")
    elif value == -1:
        return ("-1 - Loss")
    else :
        return ("0 - Draw")
    

#------------------------------------------------------------------------------------
#Driver Code starts here
print('\n')
print("CS20B1056 SAURABH GUPTA\n")
print("Game Tree Search (Minimax with Alpha Beta Pruning)\n")
print("TOPIC : TicTacToe - using Alpha Beta pruning\n\n")

tic_tac_toe = [['O','X','O'],['X','O','-'],['-','X','-']]
print("Initial State : ",tic_tac_toe, end = '\n\n')
#Let's find success chances of Player 'O'
ans = MaxNode(tic_tac_toe,'O','O',inf)
print('O\'s Result Value (Win : 1 ; Loss : -1 ; Draw : 0) : ', getResult(ans.alpha), end = '\n\n')

#Let's find success chances of Player 'X'
tic_tac_toe = [['O','X','O'],['X','O','-'],['-','X','-']]
print("Initial State : ",tic_tac_toe, end = '\n\n')
ans = MaxNode(tic_tac_toe,'X','X',inf)
print('X\'s Result Value (Win : 1 ; Loss : -1 ; Draw : 0) : ', getResult(ans.alpha), end = '\n\n')

'''
5 2
1 2
2 3
4 5
3 5
2 4
1 3
4 2

3 2
1 2 
2 3
1 3
1 2
1 3
'''
