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
    answer = []  # 걸리는 시간이 담길 리스트

    # n번째 사람이 완료되는 모든 시간 탐색
    for time in times :                     # n번째 사람이 각 심사관에게 할당되는 모든 경우를 찾기 위해
        for i in range(n) :                 # 한 명씩 늘려가면서 리스트에 추가해서
            answer.append( (i+1) * time )   # 걸리는 모든 시간을 계산 (한 번은 꼭 걸릴테니 i+1)

    # 모든 경우의 수 중에서, 조건을 만족하는 가장 최소의 시간을 찾아야함
    # ????
    
    return answer

times = [7, 10]

print(solution(6, times))