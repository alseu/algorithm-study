INF = int(1e9) # 10억
# 노드의 개수(n), 간선의 개수(m)
n, m = map(int, input().split())

# 시작 노드
start = int(input())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)  # 최단거리테이블을 가장 큰 값으로 초기화

# 간선 정보 입력
for _ in range(m) :
    a, b, c = map(int, input().split())
    # a 노드에서 b 노드로 가는 비용이 c
    graph[a].append((b,c))

# 방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드 반환
def getSmallestNode():
    min_value = INF
    idx = 0
    for i in range(1, n+1) :
        if distance[i] < min_value and not visited[i] :
            min_valude = distance[i]
            idx = i
    return idx

def dijkstra(start) :
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    for i in graph[start] :
        distance[i[0]] = i[1]
    
    # 시작 노드를 제외한 전체 n-1개 노드에 대해 반복
    for i in range(n-1) :
        now = getSmallestNode()
        visited[now] = True

        for j in graph[now] :
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1) :
    if distance[i] == INF :
        print("INF")
    else :
        print(distance[i])