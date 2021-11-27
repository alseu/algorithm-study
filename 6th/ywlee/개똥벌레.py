'''
백준 3020번 - 개똥벌레
N : 동굴의 길이(짝수) (2 <= N <= 200,000)
H : 동굴의 높이 (2 <= H <= 500,000)
첫 번째 장애물은 항상 석순, 그 다음은 종유석과 석순이 번갈아가며 나타남
높이 1미터씩 구간을 나누고 구간을 지나갈 때 파괴해야하는 장애물의 최솟값과 그러한 구간이 총 몇개 있는지 출력
'''
from sys import stdin

n, h = map(int, input().split(' '))

s = []  # 석순
j = []  # 종유석

for i in range(n) :
    obs = int(stdin.readline())
    if i % 2 == 0 :
        j.append(obs)
    else :
        s.append(obs)

j.sort()
s.sort()

min = n
count = 0

def binary_search( arr, target, start, end ) :
    while start <= end :
        # target 을 찾는다고 바로 리턴하지 않고 start <= end가 되는 지점을 찾는다
        mid = (start + end)// 2
        if arr[mid] < target : 
            start = mid + 1
        else :
            end = mid - 1
    
    return start    # start 반환

for i in range(1, h+1) :    # 높이(구간)가 1부터 시작하므로
    j_count = len(j) - binary_search( j, i   - 0.5, 0, len(j)-1 )
    s_count = len(s) - binary_search( s, h-i + 0.5, 0, len(s)-1 )

    if min == j_count + s_count :
        count += 1
    elif min > j_count + s_count :
        count = 1
        min = j_count + s_count

print(min, count)