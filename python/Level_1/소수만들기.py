from itertools import combinations
import math

nums = [1,2,7,6,4]	

def solution(nums):
    answer = 0
    nums_list = list(combinations(nums,3))
    nums_list = [i[0] + i[1] + i[2] for i in nums_list]
    
    max_value = max(nums_list)
    
    #처음엔 모두 소수라고 가정
    prime = [True for _ in range(max_value + 1)]
    
    # 에라토스테네스의 체 이용
    for i in range(2, int(math.sqrt(max_value) + 1)):
        if(prime[i] == True):
            j = 2
            while(i * j <= max_value):
                prime[i * j] = False
                j += 1
                    
    for i in nums_list:
        if(prime[i] == True):
            answer += 1
            
    print(prime)

    return answer

print(solution(nums))