import sys
input = sys.stdin.readline
INF = float('inf')

n = int(input())
m = int(input())

# 2차원 리스트를 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1) :
    for b in range(1, n+1) :
        if a == b :
            graph[a][b] = 0

# 각 간선의 정보 입력
for _ in range(m) :
    # A에서 B로 가는 비용은 C로 설정
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)   # 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1) :
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1) :
    for b in range(1, n+1):
        if graph[a][b] == INF :
            print(0, end=" ")
        else :
            print(graph[a][b], end=" ")
    print()