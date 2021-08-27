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
    answer = 0

    # 임의의 시간 // 각 심사관의 심사 시간 == 각 심사관별 할당 인원
    # 각 심사관별 할당 인원을 다 더하면, n이 되어야 한다.
    # 그런 임의의 시간들 중에 최소 시간을 탐색 -> 이진탐색
    
    # 이진 탐색을 위해 오름차순 정렬
    times = sorted(times)

    # ( 1 < time < 1000000000 )
    min_time = times[0] * n // len(times)
    max_time = times[-1] * n

    while min_time <= max_time :
        mid = ( min_time + max_time ) // 2      # 중간값
        cnt = 0                                 # 심사완료 인원
        
        # 중간값을 각 심사 시간으로 나눈 몫을 다 더한다
        for time in times :
            cnt = cnt + (mid // time)

        # 만약 더한 값이 n보다 작으면 (총 인원이 더 많음))
        if cnt < n :
            min_time = mid + 1
        # 만약 더한 값이 n보다 크면 (총 인원이 더 적음)
        elif cnt >= n :
            max_time = mid - 1
            answer = mid
       
    return answer

times = [7, 10]

print(solution(6, times))


'''
테스트 결과 

테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.11ms, 10.1MB)
테스트 3 〉	통과 (7.27ms, 10.1MB)
테스트 4 〉	통과 (373.59ms, 15.1MB)
테스트 5 〉	통과 (534.89ms, 15MB)
테스트 6 〉	통과 (352.68ms, 15.2MB)
테스트 7 〉	통과 (688.41ms, 14.9MB)
테스트 8 〉	통과 (901.85ms, 15MB)
테스트 9 〉	통과 (0.03ms, 10.1MB)
'''