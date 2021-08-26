'''
입국심사를 기다리는 사람 수 n ( 1 < n < 1000000000 )
각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times ( 1 < time < 1000000000 , 1 < len(times) < 100000 )
모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return

입출력 예
| n   | times   | return |
| --- | ------- | ------ |
| 6   | [7, 10] | 28     |
'''

def solution(n, times):
    answer = [] 

    # 임의의 시간 // 각 심사관의 심사 시간 == 각 심사관별 할당 인원
    # 심사관들의 심사 시간을 임의의 시간으로 나눈 몫을 다 더하면, n이 되어야 한다.
    # 그런 임의의 시간들 중에 최소 시간을 탐색
    
    max_time = sorted(times)[len(times)-1] * n

    for i in range(max_time) :
        cnt = 0
        for time in times :
            cnt = cnt + ( (i+1) // time )

        if (cnt == n) :
            answer.append(i+1)
    
    return sorted(answer)[0]

times = [7, 10]

print(solution(6, times))


'''
테스트 결과

테스트 1 〉	통과 (0.96ms, 10.1MB)
테스트 2 〉	통과 (6875.40ms, 10.1MB)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	실패 (시간 초과)
'''