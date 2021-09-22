# N * N 크기의 정사각형 공간, 1*1로 나누어져 있음
# 가장 왼쪽 위의 좌표 (1,1), 가장 오른쪽 아래 좌표 (N,N)
# 상,하,좌,우 로 움직일 수 있으며 시작 좌표는 항상 (1,1)
# L : 왼쪽, R : 오른쪽, U : 위쪽, D : 아래쪽
# N*N 공간을 벗어나는 움직임은 무시
# N 과 이동 계획서가 주어질 때 최종적으로 도착할 좌표 (X,Y)를 공백으로 구분하여 출력

def solution(n, plan) :
    
    result = ''
    x = 1
    y = 1
    for d in plan :
        if d == 'D' :
            if x < n :
                x += 1
        elif d == 'U' :
            if x > 1 :
                x -= 1
        elif d == 'L' :
            if y > 1 :
                y -= 1
        elif d == 'R' :
            if y < n :
                y += 1
        print('{} {}'.format(x, y))

    result = str(x) + ' ' + str(y)
    return result

if __name__ == "__main__" :
    n = 5
    plan = ['R', 'R', 'R', 'U', 'D', 'D']

    print(solution(n,plan))