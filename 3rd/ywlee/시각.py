# N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램

import time

def solution(n) :
    start_time = time.time()
    result = 0
    for h in range (n + 1) :
        for m in range (60) :
            for s in range(60) :
                #if '3' in str(h) or '3' in str(m) or '3' in str(s) :   # time = 0.04739689826965332
                if '3' in str(h) + str(m) + str(s) :                    # time = 0.06219315528869629 이게 더 느림
                    result += 1
    print('time = {}'.format(time.time() - start_time))
    return result

if __name__ == "__main__" :
    n = 23

    print(solution(n))