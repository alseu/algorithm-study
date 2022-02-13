# 4386번 별자리 만들기

'''
문제
도현이는 우주의 신이다. 이제 도현이는 아무렇게나 널브러져 있는 n개의 별들을 이어서 별자리를 하나 만들 것이다. 별자리의 조건은 다음과 같다.

별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태이다.
모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 한다.
별들이 2차원 평면 위에 놓여 있다. 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때, 별자리를 만드는 최소 비용을 구하시오.

입력
첫째 줄에 별의 개수 n이 주어진다. (1 ≤ n ≤ 100)

둘째 줄부터 n개의 줄에 걸쳐 각 별의 x, y좌표가 실수 형태로 주어지며, 최대 소수점 둘째자리까지 주어진다. 좌표는 1000을 넘지 않는 양의 실수이다.

출력
첫째 줄에 정답을 출력한다. 절대/상대 오차는 10-2까지 허용한다.

예제 입력 1 
3
1.0 1.0
2.0 2.0
2.0 4.0

예제 출력 1 
3.41
'''

import math


def find_parent(parent, x):
    # 특정 원소가 속한 집합을 찾기
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    # 두 원소가 속한 집합을 합치기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수 입력받기
n = int(input())
parent = [i for i in range(n + 1)]

stars = []
edges = []
result = 0

for _ in range(n):
    a, b = map(float, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번쨰 원소를 비용으로 설정
    stars.append((a, b))

# 간선 만들기
for i in range(n - 1):
    for j in range(i + 1, n):
        edges.append(
            (math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2), i, j))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(round(result, 2))
