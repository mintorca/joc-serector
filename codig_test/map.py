n=5
arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]
import re
def solution(n, arr1, arr2):
    map_1=[]
    map_2=[]
    
    answer = []
    for a1,a2 in zip(arr1,arr2):
        arr_all=format((a1 | a2),'b')
        arr_all='0'*(n-len(arr_all))+arr_all
        arr_all=arr_all.replace('1','#')
        arr_all=arr_all.replace('0',' ')
        answer.append(arr_all)
    return answer