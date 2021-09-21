# N * M 크기의 직사각형 맵
# 상하좌우로 움직일 수 있고, 바다로 되어있는 공간에는 갈 수 없다
# 1. 현재 위치(a,b)에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정함
# 2. 캐릭터의 바로 왼쪽에 아직 가보지 않은 칸이 존재한다면 왼쪽으로 회전한 다음 왼쪽으로 한 칸을 전진. 왼쪽에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 되돌아감
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어있는 칸인 경우에는 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아감. 만약 뒤쪽이 바다라면 움직임을 멈춤
# 캐릭터가 방문한 칸의 수를 출력
# 방향 > 0 : 북쪽, 1 : 동쪽, 2 : 남쪽, 3 : 서쪽
# 지형 > 0 : 육지, 1 : 바다
import time

NORTH   = 0
EAST    = 1
SOUTH   = 2
WEST    = 3

LAND    = 0
SEA     = 1

VISITED = 1

ROW     = 0
COL     = 1
DIR     = 2

def check_left (curr, visited, cord, n, m) :
    ''' 방문 가능하면 True, 바다거나 이미 방문했다면 False '''
    if curr[DIR] == NORTH :
        if curr[ROW] > 0 and curr[ROW] < n and curr[COL] > 0 :   # 왼쪽이 외곽을 벗어나지 않는지 
            print('dir = {}, {}'.format(curr[DIR], cord[curr[ROW]][curr[COL] - 1]))
            if visited[curr[ROW]][curr[COL] - 1] != VISITED and cord[curr[ROW]][curr[COL] - 1] != SEA :    # 방문하지 않았고 바다가 아니라면
                return True
            else :
                return False
        else :
            return False
    elif curr[DIR] == EAST :
        if curr[COL] > 0 and curr[COL] < m and curr[ROW] > 0 :   # 왼쪽이 외곽을 벗어나지 않는지 
            print('dir = {}, {}'.format(curr[DIR], cord[curr[ROW] - 1][curr[COL]]))
            if visited[curr[ROW] - 1][curr[COL]] != VISITED and cord[curr[ROW] - 1][curr[COL]] != SEA :    # 방문하지 않았고 바다가 아니라면
                return True
            else :
                return False
        else :
            return False
    elif curr[DIR] == SOUTH :
        if curr[ROW] > 0 and curr[ROW] < n and curr[COL] < m - 1 :   # 왼쪽이 외곽을 벗어나지 않는지 
            print('dir = {}, visited = {}, cord = {}'.format(curr[DIR], visited[curr[ROW]][curr[COL] + 1], cord[curr[ROW]][curr[COL] + 1]))
            if visited[curr[ROW]][curr[COL] + 1] != VISITED and cord[curr[ROW]][curr[COL] + 1] != SEA :    # 방문하지 않았고 바다가 아니라면
                return True
            else :
                return False
        else :
            return False
    elif curr[DIR] == WEST :
        if curr[COL] > 0 and curr[COL] < m and curr[ROW] < n - 1 :   # 왼쪽이 외곽을 벗어나지 않는지 
            print('dir = {}, {}'.format(curr[DIR], cord[curr[ROW] + 1][curr[COL]]))
            if visited[curr[ROW] + 1][curr[COL]] != VISITED and cord[curr[ROW] + 1][curr[COL]] != SEA :    # 방문하지 않았고 바다가 아니라면
                return True
            else :
                return False
        else :
            return False

    return None

def turn_left (curr) :
    ''' 반시계방향 회전 '''
    if curr[DIR] == NORTH :
        curr[DIR] = WEST
    elif curr[DIR] == EAST :
        curr[DIR] = NORTH
    elif curr[DIR] == SOUTH :
        curr[DIR] = EAST
    elif curr[DIR] == WEST :
        curr[DIR] = SOUTH

    return curr

def check_sea (curr, cord, n, m) :
    ''' 바다면 True, 바다가 아니면 False '''
    if curr[DIR] == NORTH :
        if curr[ROW] > 0 and curr[ROW] < n - 1 and curr[COL] > 0 :   # 왼쪽이 외곽을 벗어나지 않는지 
            print('dir = {}, {}'.format(curr[DIR], cord[curr[ROW]][curr[COL] - 1]))
            if cord[curr[ROW]][curr[COL] - 1] != SEA :    # 바다가 아니라면
                return False
            else :
                return True
        else :
            return True
    elif curr[DIR] == EAST :
        if curr[COL] > 0 and curr[COL] < m - 1 and curr[ROW] > 0 :   # 왼쪽이 외곽을 벗어나지 않는지 
            print('dir = {}, {}'.format(curr[DIR], cord[curr[ROW] - 1][curr[COL]]))
            if cord[curr[ROW] - 1][curr[COL]] != SEA :
                return False
            else :
                return True
        else :
            return True
    elif curr[DIR] == SOUTH :
        if curr[ROW] > 0 and curr[ROW] < n - 1 and curr[COL] > m - 1 :   # 왼쪽이 외곽을 벗어나지 않는지 
            print('dir = {}, {}'.format(curr[DIR], cord[curr[ROW]][curr[COL]] + 1))
            if cord[curr[ROW]][curr[COL] + 1] != SEA :
                return False
            else :
                return True
        else :
            return True
    elif curr[DIR] == WEST :
        if curr[COL] > 0 and curr[COL] < m - 1 and curr[ROW] > n - 1 :   # 왼쪽이 외곽을 벗어나지 않는지 
            print('dir = {}, {}'.format(curr[DIR], cord[curr[ROW] + 1][curr[COL]]))
            if cord[curr[ROW] + 1][curr[COL]] != SEA :
                return False
            else :
                return True
        else :
            return True

    return None

def go_forward(curr) :
    if curr[DIR] == NORTH :
        curr[ROW] -= 1
    elif curr[DIR] == EAST :
        curr[COL] += 1
    elif curr[DIR] == SOUTH :
        curr[ROW] += 1
    elif curr[DIR] == WEST :
        curr[COL] -= 1

    return curr

def go_back(curr) :
    if curr[DIR] == NORTH :
        curr[ROW] += 1
    elif curr[DIR] == EAST :
        curr[COL] -= 1
    elif curr[DIR] == SOUTH :
        curr[ROW] -= 1
    elif curr[DIR] == WEST :
        curr[COL] += 1

    return curr

def solution(move) :
    start_time = time.time()
    
    n, m    = map(int, move[0].split(' '))
    a, b, d = map(int, move[1].split(' '))
    
    cord    = []
    for i in range(n) :
        cord.append(list(map(int, move[i+2].split(' '))))
    print('cord = ', cord)
    curr    = [a, b, d]    # x, y, direction
    visited = [ [0 for col in range(m)] for row in range(n) ]  # 미방문 : 0 , 방문 : 1
    visited[a][b] = VISITED # 처음 좌표도 포함

    turn_count   = 0
    move_count   = 1    # 처음 좌표도 포함

    while True :
        time.sleep(0.5)
        print('visited = ', visited)
        print('curr = ', curr)
        if turn_count < 4 :  # 네 방향 탐색
            res = check_left(curr, visited, cord, n, m)
            print('check_left = ', res)
            if  res : # 왼쪽에 가보지 않은 칸이 존재
                curr   = turn_left(curr)    # 왼쪽으로 회전
                curr   = go_forward(curr)   # 앞으로 전진
                visited[curr[0]][curr[1]] = VISITED # 방문
                move_count += 1
                turn_count  = 0
                print('MOVE!')
            else :              # 왼쪽에 가보지 않은 칸이 없음
                curr   = turn_left(curr)  # 왼쪽으로 회전
                turn_count += 1                     # 네 방향 탐색할 때까지 회전
                print('JUST TURN!')
        else :              # 네 방향 모두 탐색했다면
            res = check_sea(curr, cord, n, m)
            print('check_sea = ', res)
            if  res :   # 뒤쪽이 바다인지 탐색
                break       # 바다면 탈출
            else :
                curr   = go_back(curr)           # 바다가 아니라면 뒤로 이동
                move_count += 1
                turn_count  = 0
                print('GO BACK')

    print('time = ', time.time() - start_time)
    return move_count

if __name__ == "__main__" :
    moves = [['4 4', '1 1 0', '1 1 1 1', '1 0 0 1', '1 1 0 1', '1 1 1 1'], ['3 3', '1 1 0', '1 1 1', '1 0 0', '1 1 0']]
    for move in moves :
        print(solution(move))