# 각 자리가 숫자(0~9)로만 이루어진 문자열 S
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 '*' 혹은 '+' 연산자를 넣어
# 결괏값이 가장 큰 수를 구하여라
# 사칙연산 순서와 상관 없이 왼쪽부터 오른쪽으로 연산이 진행된다고 가정

s = list(map(int, input()))

result  = s[0]
i       = 1

while True :
    if s[i-1] == 0 :        # 만약 이전 값이 0이면 더하고
        result  += s[i]
        i       += 1
    else :                  # 나머지는 전부 곱해줘야 최댓값이 나온다
        result  *= s[i]
        i       += 1
    
    if i >= len(s) :
        break

print(result)