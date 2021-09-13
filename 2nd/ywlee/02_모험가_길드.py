# 모험가 N명
# 공포도 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있음
# N 명의 모험가에 대한 각각의 공포도가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 출력
# 모든 모험가를 특정한 그룹에 넣지 않아도 됨

n = int(input())
fear = sorted(list(map(int, input().split(' ')))) # 오름차순 정렬

# 오름차순 정렬 후 공포도가 작은 순서대로 묶기
count   = 0 # 그룹에 포함되는 인원
result  = 0 # 결성된 그룹 수

for i in fear :
    count   += 1    # 각 그룹에 포함되는 인원
    if count >= i : # 만약 해당 공포도만큼의 인원이 쌓였다면
                    # 그룹 결성 성공
        result += 1
        count   = 0 # 그룹인원 초기화

print(result)