# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PrmyKAWEDFAUq&categoryId=AV5PrmyKAWEDFAUq&categoryType=CODE&problemTitle=%EC%A0%95%EB%A0%AC&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

t = int(input())
for test_case in range(t) :
    n = int(input())
    numbers = list(map(int, input().split(' ')))
    result = ''
    for i in sorted(numbers) :
        result += f'{i} '
    print(f'#{test_case} {result} ')
