n = int(input())    # 거스름돈 입력

unit = [50000, 10000, 5000, 1000, 500, 100, 50, 10]     # 거슬러 줄 수 있는 화폐 단위

i = 0
change = 0

while True :
    change += n // unit[i]  # // : 나눈 몫의 정수 부분만
    n = n % unit[i]
    i += 1
    if i >= len(unit) :
        break

print(change)