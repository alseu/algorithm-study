# N 개의 동전을 이용하여 만들 수 '없는' 양의 정수 금액 중 최솟값
# 각 화폐 단위는 1000000 이하의 자연수

n       = int(input())
coins   = sorted(list(map(int, input().split(' '))))    # 오름차순 정렬
result  = 1 # 양의 정수 최솟값은 1

# 작은 화폐부터 화폐의 수 만큼 반복
for coin in coins :
    
    if result >= coin :    # ?? 다시 생각
        result += coin
    else :
        break

    '''
    if result < coin :
        break
    result += coin
    '''

print(result)