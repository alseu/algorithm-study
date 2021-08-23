#!/usr/bin/python3

def solution(n, times):
    answer = 0
    person = n
    while(True):
        answer = answer + 1
        for a in times :
            if(answer%a == 0):
                person = person-1
        if(person == 0):
            return answer

if __name__ == "__main__":
    print(solution(6, [7,10]))      #28
