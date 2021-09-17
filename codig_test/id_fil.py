
new_id=	"...!@BaT#*..y.abcdefghijklm"
import re
def solution(new_id):
    new_id=new_id.lower()
    answer=new_id
    answer = re.sub('[^a-zA-Z0-9\-\_\.]', '', new_id)
    answer = re.sub('[.]+','.',answer)
    answer=answer.strip('.')
    if answer == '':
        answer += 'a'
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1]=='.':
        answer =answer[:-1]
    if len(answer)<=2:
        while len(answer)<3:
            answer +=answer[-1]
        
    return answer