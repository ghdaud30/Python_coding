s = "try           hello world"

def solution(s):
    answer = ''
    s = s.split(' ')
    print(s)
    for word in s:
        for i in range(len(word)):
            if(i % 2 == 0):
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += ' '

    return answer[:-1]

print(solution(s))