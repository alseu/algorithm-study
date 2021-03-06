'''
입국심사를 기다리는 사람 수 n ( 1 < n < 1000000000 )
각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times ( 1 < time < 1000000000 , 1 < len(times) < 100000 )
모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return

입출력 예
| n   | times   | return |
| --- | ------- | ------ |
| 6   | [7, 10] | 28     |
'''

def immigration( n, times, min_time, max_time ):
    mid = ( min_time + max_time ) // 2
    cnt = 0
    
    for time in times :
        cnt = cnt + (mid // time)

    # 만약 더한 값이 n보다 크면 (총 인원이 더 적음)
    if cnt >= n :
        if min_time >= mid :
            return mid
        else :
            return immigration( n, times, min_time, mid )
    # 만약 더한 값이 n보다 작으면 (총 인원이 더 많음))
    else :
        if mid + 1 > max_time :
            return mid
        else :
            return immigration( n, times, mid + 1, max_time )
    
def solution(n, times):
    answer = 0

    # 임의의 시간 // 각 심사관의 심사 시간 == 각 심사관별 할당 인원
    # 각 심사관별 할당 인원을 다 더하면, n이 되어야 한다.
    # 그런 임의의 시간들 중에 최소 시간을 탐색 -> 이진탐색
    
    # 이진 탐색을 위해 오름차순 정렬
    times = sorted(times)

    # ( 1 < time < 1000000000 )
    min_time = times[ 0]
    max_time = times[-1] * n
    
    answer = immigration( n, times, min_time, max_time )
    
    return answer

times = [7, 10]

print(solution(6, times))


'''
테스트 결과 

테스트 1 〉	실패 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.10ms, 10.1MB)
테스트 3 〉	실패 (2.25ms, 10.2MB)
테스트 4 〉	실패 (294.68ms, 14.9MB)
테스트 5 〉	실패 (354.30ms, 14.9MB)
테스트 6 〉	실패 (346.75ms, 15.1MB)
테스트 7 〉	실패 (540.09ms, 14.8MB)
테스트 8 〉	실패 (502.29ms, 14.9MB)
테스트 9 〉	실패 (0.04ms, 10.1MB)
'''