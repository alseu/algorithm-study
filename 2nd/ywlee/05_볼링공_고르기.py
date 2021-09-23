# 두 사람이 N개의 볼링공 중 서로 다른 무게의 볼링공을 고르려고 함
# N개의 볼링공 중 같은 무게의 공이 있을 수 있지만 서로 다른 공으로 간주
# 볼링공의 무게는 1부터 M까지 자연수
import time
#n, m = map(int, input().split(' '))
#balls = list(map(int, input().split(' ')))

with open("/Users/leeyw/Documents/GitHub/algorithm-study/2nd/ywlee/balls.txt", "r") as f :
    balls = [ i for i in list(map(int, f.readlines()[0].split(' '))) ]
n = len(balls)
m = max(balls)

start_time = time.time()    # 측정 시작
result = 0
if False :
    # 단순무식, TIME : 9.8초
    for i in range(len(balls)) :
        for j in range(i+1, len(balls), 1) :
            if balls[i] != balls[j] :
                result += 1
                
if True :
    # 책의 풀이, TIME = 0.00109초
    array = [0] * 11
    for x in balls :
        array[x] += 1

    for i in range(1, m+1):
        n -= array[i]
        result += array[i] * n

print("TIME : ", time.time() - start_time) # 수행 시간 출력
print(result)