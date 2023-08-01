def solution(today, terms, privacies):
    type_dic = {}
    ty, tm, td = map(int, today.split("."))
    answer = []
    for t in terms:
        type, dur = t.split()
        type_dic[type] = int(dur)
    
    for i in range(len(privacies)):
        date, type = privacies[i].split()
        year, month, day = map(int, date.split("."))
        
        month += type_dic[type]
        yd = month // 12 if month % 12 != 0 else month//12 -1
        year += yd
        month = month - yd*12
        
        if year > ty:
            continue  
        elif year < ty:
            answer.append(i+1)
            continue
        
        if month > tm:
            continue
        elif month < tm:
            answer.append(i+1)
            continue
            
        if day > td:
            continue
        else:
            answer.append(i+1)
            continue
        
    return answer