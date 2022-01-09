'''
문제
V개의 마을와 E개의 도로로 구성되어 있는 도시가 있다. 도로는 마을과 마을 사이에 놓여 있으며, 일방 통행 도로이다. 마을에는 편의상 1번부터 V번까지 번호가 매겨져 있다고 하자.

당신은 도로를 따라 운동을 하기 위한 경로를 찾으려고 한다. 운동을 한 후에는 다시 시작점으로 돌아오는 것이 좋기 때문에, 우리는 사이클을 찾기를 원한다. 단, 당신은 운동을 매우 귀찮아하므로, 사이클을 이루는 도로의 길이의 합이 최소가 되도록 찾으려고 한다.

도로의 정보가 주어졌을 때, 도로의 길이의 합이 가장 작은 사이클을 찾는 프로그램을 작성하시오. 두 마을을 왕복하는 경우도 사이클에 포함됨에 주의한다.

입력
첫째 줄에 V와 E가 빈칸을 사이에 두고 주어진다. (2 ≤ V ≤ 400, 0 ≤ E ≤ V(V-1)) 다음 E개의 줄에는 각각 세 개의 정수 a, b, c가 주어진다. a번 마을에서 b번 마을로 가는 거리가 c인 도로가 있다는 의미이다. (a → b임에 주의) 거리는 10,000 이하의 자연수이다. (a, b) 쌍이 같은 도로가 여러 번 주어지지 않는다.

출력
첫째 줄에 최소 사이클의 도로 길이의 합을 출력한다. 운동 경로를 찾는 것이 불가능한 경우에는 -1을 출력한다.
'''
import sys
input = sys.stdin.readline
INF = float('inf')

v,e = map(int, input().split())

# 2차원 리스트를 무한으로 초기화
graph = [[INF] * (v+1) for _ in range(v+1)]

# 각 간선의 정보 입력
for _ in range(e) :
    # A에서 B로 가는 비용은 C로 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, v+1) :
    for a in range(1, v+1) :
        for b in range(1, v+1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 가장 작은 사이클 찾기
min_cycle = INF
for i in range(1, v+1) :
    min_cycle = min(min_cycle, graph[i][i]) # 자기 자신에게 돌아오는 경우만 생각하면 된다

if min_cycle == INF :
    print(-1)
else :
    print(min_cycle)

# pypy3로 하지 않으면 시간초과