'''
팀 결성

학생 0 ~ N

모든 학생이 서로 다른 팀으로 구성, 총 N + 1 개의 팀

1. '팀 합치기' : 두 팀을 합치는 연산
    0 a b 형태, a번 학생이 속한 팀과 b번 학생이 속한 팀을 합침

2. '같은 팀 여부 확인' : 특정한 두 학생이 같은 팀에 속하는지를 확인하는 연산
    1 a b 형태, a번 학생과 b번 학생이 같은 팀에 속해있는지 확인
    YES 또는 NO로 출력

선생님이 M개의 연산을 수행할 수 있을 때, '같은 팀 여부 확인' 연산에 대한 연산 결과를 출력

(1<=N, M<=100,000)

M 개의 줄에 각각의 연산이 주어짐
'''


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


n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(0, n+1):
    parent[i] = i

for i in range(m):
    oper, a, b = map(int, input().split())
    # 합집합(union)
    if oper == 0:
        union_parent(parent, a, b)
    # 찾기(find)
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
