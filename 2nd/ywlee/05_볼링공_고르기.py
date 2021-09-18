# 두 사람이 N개의 볼링공 중 서로 다른 무게의 볼링공을 고르려고 함
# N개의 볼링공 중 같은 무게의 공이 있을 수 있지만 서로 다른 공으로 간주
# 볼링공의 무게는 1부터 M까지 자연수

n, m = map(int, input().split(' '))

balls = list(map(int, input().split(' ')))

result = 0
for i in range(len(balls)) :
    for j in range(i+1, len(balls), 1) :
        if balls[i] != balls[j] :
            result += 1

print(result)