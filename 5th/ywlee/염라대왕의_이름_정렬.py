# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWqU0zh6rssDFARG&categoryId=AWqU0zh6rssDFARG&categoryType=CODE&problemTitle=%EC%A0%95%EB%A0%AC&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 길이가 짧을수록, 길이가 같다면 알파벳순으로

t = int(input())    # 테스트 케이스의 수
for test_case in range(1,t+1) :
    n = int(input())    # 이름의 개수(1 <= n <= 20,000)
    names = set()
    for _ in range(n) :
        name = input()
        names.add((name, len(name)))
    
    print(f'#{test_case}')
    names = sorted(names, key=lambda x: (x[1], x[0])) # 길이순, 알파벳순으로 정렬
    for i in range(len(names)) :
        print(names[i][0])