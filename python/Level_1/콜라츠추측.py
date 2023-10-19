num = 626331

def solution(num):
    if(num == 1):
        return 0
    
    for i in range(1, 501):
        if(num % 2 == 0):
            num //= 2
        else:
            num = (num * 3 )+ 1
        if(num == 1):
            return i
        
    if(num != 1):
        return -1
    
    return i

print(solution(num))