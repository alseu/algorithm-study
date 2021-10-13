# n * m 크기의 미로
# root = (1,1), 출구 = (n, m)
# 괴물이 있으면 0, 없으면 1
# 미로를 탈출하기 위해 움직여야 하는 최소 칸의 개수(시작, 마지막칸 포함)

n, m = map(int, input().split(' '))
graph = []
for i in range(n) :
    graph.append(list(map(int, input())))

from collections import deque

dx = [-1,  1,  0,  0]
dy = [ 0,  0,  1, -1]

def bfs(x, y) :
    queue = deque()
    queue.append((x, y))

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue

            if graph[nx][ny] == 0 :
                continue

            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))