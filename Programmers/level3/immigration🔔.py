#22.05.30
#입국심사

#이분탐색 적용🔔
def solution(n, times):
    str = 0
    end = n*times[-1]
    mid = end//2
    check = 0
    answer = 0

    while str <= end:
        for i in times:
            tmp = mid//i
            check += tmp   
        if check >= n:
            end = mid-1
            if answer == 0:
                answer = mid
            else:
                answer = min(answer, mid)
        else:
            str = mid+1
        mid = (str+end)//2
        check = 0

    return answer