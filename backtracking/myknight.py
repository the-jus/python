from ast import Not
from operator import truediv
from pickle import FALSE

#Given a N*N board with the Knight placed on the first block of an empty board. Moving according to the rules of chess knight must visit 
# each square exactly once. Print the order of each cell in which they are visited.

# Input : 
# N = 8
# Output:
# 0  59  38  33  30  17   8  63
# 37  34  31  60   9  62  29  16
# 58   1  36  39  32  27  18   7
# 35  48  41  26  61  10  15  28
# 42  57   2  49  40  23   6  19
# 47  50  45  54  25  20  11  14
# 56  43  52   3  22  13  24   5
# 51  46  55  44  53   4  21  12

# Naive Algorithm for Knight’s tour 
# The Naive Algorithm is to generate all tours one by one and check if the generated tour satisfies the constraints. 

# while there are untried tours
# { 
#    generate the next tour 
#    if this tour covers all squares 
#    { 
#       print this path;
#    }
# }


N=8
def safeposition(board,x,y):
    if(x>=0 and y>=0 and x<N and y<N and board[x][y]==-1):
        return True
    return False

def printSolutn(board,N):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end="   ")
        print()
        
def SolveKT(N):
    board =[[-1 for i in range(N)]for i in range(N)]
    # print(board)
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board[0][0]=0
    pos=1
    if(not SolveKTuntil(N,board,0,0,move_x,move_y,pos)):
        print("Cannot be solved")
    else:
        printSolutn(board,N)
    
def SolveKTuntil(N,board,cur_x,cur_y,move_x,move_y,pos):
    if(pos==N**2):
        return True
    for i in range(8):
        new_x= cur_x +move_x[i]
        new_y=cur_y +move_y[i]
        if(safeposition(board,new_x,new_y)):
            board[new_x][new_y]=pos
            if(SolveKTuntil(N,board,new_x,new_y,move_x,move_y,pos+1)):
                return True
            board[new_x][new_y]=-1
    return False

if __name__ == "__main__":
    SolveKT(N)


