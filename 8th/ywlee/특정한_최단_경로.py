'''
문제
방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데, a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000) 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1)

출력
첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.
'''

import heapq, sys
INF = float('inf')
input = sys.stdin.readline

# 노드의 개수(n), 간선의 개수(m)
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

# 간선 정보 입력
# 방향성이 없으므로 양방향 추가
for _ in range(m) :
    a, b, c = map(int, input().split())
    # a 노드에서 b 노드로 가는 비용이 c
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int, input().split())

def dijkstra(start, end) :
    q = []
    distance = [INF] * (n+1)  # 최단거리테이블을 가장 큰 값으로 초기화

    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q : # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist :
            continue
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now] :
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return distance[end]

# 1 -> v1 -> v2 -> N
p1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
# 1 -> v2 -> v1 -> N
p2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

result = min(p1, p2)

print(result if result < INF else -1)