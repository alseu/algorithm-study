# 8 * 8 좌표평면의 체스판
# 나이트는 L자 형태로만 이동 가능
# - 수평으로 두 칸 이동 후 수직으로 한 칸
# - 수직으로 두 칸 이동 후 수평으로 한 칸
# 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력
# 행의 위치는 1부터 8
# 열의 위치는 a부터 h

import time

def solution(n) :
    start_time = time.time()
    x = ord(n[0]) - 96   # 아스키 코드로 변환, 'a' = 97
    y = int(n[1])
    result = 0
    cord = [x,y]
    # 최대 가짓수는 8가지
    p = [[-2, -1],[-2, 1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]
    for i in p :
        tmp = [cord[0] + i[0], cord[1] + i[1]]
        if tmp[0] > 0 and tmp[0] <= 8 and tmp[1] > 0 and tmp[1] <= 8 :
            result += 1

    print('time = {}'.format(time.time() - start_time))
    return result

if __name__ == "__main__" :
    n = ['a1', 'c2']
    for i in n :
        print(solution(i))