# 0,1로 이루어진 문자열 S
# S에 있는 모든 숫자를 전부 같게 만들려고 함
# S에서 연속된 하나 이상의 숫자를 잡고 뒤집을 수 있음
# import time

s = input()

# start_time = time.time()    # 측정 시작

count_0 = 0     # 0을 뒤집는 경우
count_1 = 0     # 1을 뒤집는 경우

s_len   = len(s)
s_0     = '0'
s_1     = '1'
i       = 0
j       = 0

while True :
    if i >= s_len :
        break

    if s[i] != s_0 :
        if i >= s_len :
            break
        else :
            count_0 += 1
        
        j = i  
        while True :
            if j >= s_len or s[j] == s_0 :
                i = j
                break
            j += 1
    else :
        i += 1

i       = 0
j       = 0

while True :
    if i >= s_len :
        break

    if s[i] != s_1 :
        if i >= s_len :
            break
        else :
            count_1 += 1
        
        j = i  
        while True :
            if j >= s_len or s[j] == s_1 :
                i = j
                break
            j += 1
    else :
        i += 1

# print("TIME : ", time.time() - start_time) # 수행 시간 출력

print(min(count_0, count_1))