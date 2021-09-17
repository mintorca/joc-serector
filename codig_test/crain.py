board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
move=[1,5,3,5,1,2,1,4]	
def solution(board,moves):
    moves = list(map(lambda mv :mv-1,moves))
    stack = [0]
    cnt = 0
    for i in moves:
        for bod in board:
            if bod[i] != 0:
                stack.append(bod[i])
                bod[i]=0
                if stack[-1]==stack[-2]:
                    stack.pop()
                    stack.pop()
                    cnt += 2
                break
    return cnt