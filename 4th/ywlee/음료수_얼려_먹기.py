# n * m 크기의 얼음 틀
# 구멍이 뚫려 있는 부분 0, 칸막이가 존재하는 부분 1
# 얼음 틀의 모양이 주어졌을 때 생성되는 총 얼음의 개수

n, m = map(int, input().split(' '))

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >=n or y <= -1 or y >= m :
        return False
    
    if graph[x][y] == 0 :
        graph[x][y] = 1
        dfs(x-1, y  )
        dfs(x  , y-1)
        dfs(x+1, y  )
        dfs(x  , y+1)
        return True
    return False

result = 0
for i in range(n) :
    for j in range(m) :
        # 전체 node를 돌면서, 탐색
        # graph를 공유하기때문에, 이미 방문한 묶음은 False를 반환
        if dfs(i, j) == True :
            result += 1

print(result)