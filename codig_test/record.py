record=["Enter uid1234 tom", "Enter uid4567 tomas","Leave uid1234","Enter uid1234 jin","Change uid4567 Ryan"]

def solution(record):
    answer = []
    login=[]
    log={}
    for i in record:
        login=i.split(' ')
        if login[1] not in log:
            log[login[1]]=login[2]
        if login[0]=='Change':
            log[login[1]]=login[2]
        if login[0]=='Enter':
            if log.get(login[1]) != login[2] :
                log[login[1]]=login[2]
    for i in record:
        i=i.split(' ')
        if i[0]=='Enter':
            answer.append(f'{log.get(i[1])}님이 들어왔습니다.')
        elif i[0]=='Leave':
            answer.append(f'{log.get(i[1])}님이 나갔습니다.')
    return answer