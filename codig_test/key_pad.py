numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand="right"
left=[1,4,7]
right=[3,6,9]
hand_pos=['*',"#"]
position={1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2),'*':(3,0),0:(3,1),"#":(3,2)}
def solution(numbers, hand):
    answer=''
    center=''
    for i in numbers:
        if i in left:
            answer+='L'
            hand_pos[0]=i
            
        elif i in right:
            answer+='R'
            hand_pos[1]=i
        else:  
            center=central(position,hand_pos[0],hand_pos[1],i,hand)
            if center == 'L':
                answer +="L"
                hand_pos[0] = i
            else:
                answer +="R"
                hand_pos[1] = i
   
    return answer
def central(position,hl,hr,numbers,hand):
    l_move= abs(position[hl][0]-position[numbers][0])+abs(position[hl][1]-position[numbers][1])
    r_move= abs(position[hr][0]-position[numbers][0])+abs(position[hr][1]-position[numbers][1])
    if l_move == r_move:
        if hand == "left":
            cente = 'L'
        else:
            cente = "R"
    elif l_move < r_move:
        cente = "L"
    else:
        cente = "R"
    return cente