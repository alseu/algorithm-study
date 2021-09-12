# 어떠한 수 N이 1이 될 때까지
# 1. N 에서 1을 뺀다
# 2. N 을 K 로 나눈다 (K로 나누어 떨어질 때만)
# 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하시오
import time

n, k = map(int, input().split(' '))

start_time = time.time()    # 측정 시작
count = 0
'''
# 1
while True :
    if n % k == 0 :
        n /= k
        count += 1
    else :
        n -= 1
        count += 1
        
    if n == 1 :
        break
'''
'''
# 2
while n >= k :
    while n % k != 0 :
        n -= 1
        count += 1
    
    n //= k
    count += 1

while n > 1 :
    n -= 1
    count += 1
'''

# 3
while True :
    target = (n // k) * k
    count += (n - target)
    n = target

    if n < k :
        break

    count += 1
    n //= k

count += (n-1)

end_time = time.time()      # 측정 끝

print(count)

print("TIME : ", end_time - start_time) # 수행 시간 출력

'''
수행시간 비교
# 1
❯ python3 2nd/ywlee/1이_될_때까지.py
1234561234561234561 123456123456
11234561
TIME :  2.6760969161987305

# 2
❯ python3 2nd/ywlee/1이_될_때까지.py
1234561234561234561 123456123456
11234561
TIME :  1.6039459705352783

# 3
❯ python3 2nd/ywlee/1이_될_때까지.py
1234561234561234561 123456123456
11234561
TIME :  1.5020370483398438e-05
       =0.000015020370483398438
'''