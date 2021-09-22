# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
import sys

sys.stdin = open("/Users/leeyw/Documents/GitHub/algorithm-study/3rd/ywlee/input.txt", "r")

#T = int(input())
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    width = int(input()) # 테스트 케이스의 길이(가로 길이)
    buildings = list(map(int, input().split()))
    #print('{} . len = {}'.format(buildings, len(buildings)))
    # 맨 왼쪽 두 칸과 오른쪽 두 칸에는 건물이 지어지지 않음
    # 각 빌딩의 높이는 최대 255
    view = 0 # 조망권을 가진 세대
    for i in range(width) :
        #print("buildings[{}] = {} > buildings[{}] = {}".format(i, buildings[i], i-1, buildings[i-1]))
        if i < 2 or i > width - 2 : continue
        # 왼쪽 빌딩과 비교
        if buildings[i] > buildings[i-1] and buildings[i] > buildings[i-2] :
                # 오른쪽 빌딩과 비교
                if  buildings[i] > buildings[i+1] and buildings[i] > buildings[i+2] :
                    views = [buildings[i] - buildings[i-1], buildings[i] - buildings[i-2], buildings[i] - buildings[i+1], buildings[i] - buildings[i+2] ]
                    #print(views)
                    view += min(views)
    print('#{} {}'.format(test_case, view))
    # ///////////////////////////////////////////////////////////////////////////////////
