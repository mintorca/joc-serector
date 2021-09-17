m=6
n=6
board=["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

def solution(m, n, board):
    answer = 0
    game=[]
    dis=[]

    n_game=[]
    count=0
    next= []
    for i in board:
        game.append(list(i))
    for i in range(0,m-1):
        for j in range(0,n-1):
            if game[i][j] == game[i+1][j] == game[i][j+1] == game[i+1][j+1]:
                dis.append((i,j))
                dis.append((i+1,j))
                dis.append((i,j+1))
                dis.append((i+1,j+1))
    
    dis=list(set(dis))
    
    for i in dis:
        game[i[0]][i[1]]=""
    
    for k in range(60):
        for i in range(m-1):
            for j in range(n):
                if game[i+1][j]=="":
                    game[i][j],game[i+1][j]=game[i+1][j],game[i][j]
   
              
    while True:
        for i in range(0,m-1):
            for j in range(0,n-1):
                if game[i][j] =="" or game[i][j+1] =="" :
                    continue
                elif game[i][j] == game[i+1][j] == game[i][j+1] == game[i+1][j+1]:
                        n_game.append((i,j))
                        n_game.append((i+1,j))
                        n_game.append((i,j+1))
                        n_game.append((i+1,j+1))
            
        if len(n_game) != 0:
            n_game=list(set(n_game)) 
            dis=dis+n_game            
            for i in n_game:
                game[i[0]][i[1]] =""
            
            for k in range(60):
                for i in range(m-1):
                    for j in range(n):
                        if game[i+1][j]=="":
                            game[i][j],game[i+1][j]=game[i+1][j],game[i][j]
                    
            n_game=[]      
        else:
           break

    return len(dis)