# 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
# 카드는 N * M 형태로 놓여 있다.
# 1. 뽑고자 하는 카드가 포함되어 있는 행(N)을 선택한다
# 2. 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다
# 3. 따라서 처음 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세운다. ???
# 각 행의 가장 숫자가 낮은 카드들 중 가장 높은 수를 구하는 문제인듯
# 어렵게도 써놨네

# 1 <= N,M <= 100
# 1 <= num <= 10000

n, m   = map(int, input().split(' '))

row    = list()    # 행 (n)
result = 0

for i in range (n) :
    row.append(list(map(int, input().split(' '))))
    print ( row )
    min_row = min(row[i])
    if min_row > result :
        result = min_row

print(result)