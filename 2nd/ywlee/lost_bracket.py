'''
문제
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

입력
첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.
'''

'''
아이디어
- 덧셈, 뺄셈밖에 없으므로 식은 왼쪽에서 오른쪽으로 진행된다.
- 가장 작은 수를 구해야 하므로 뺄셈 사이사이에 괄호를 씌운다
- (..+..+..)-(..+..+..)-(..+..+..+..) 이런식
'''

equation = input()

num = list()    # 숫자
op  = list()    # 연산자

seperate_index = 0  # 
index = 0

# 숫자와 연산자 분리
for s in equation :
    if s == '+' :
        num.append(int(equation[seperate_index:index]))
        op.append(equation[index:index+1])
        seperate_index = index + 1
    elif s == '-' :
        num.append(int(equation[seperate_index:index]))
        op.append(equation[index:index+1])
        seperate_index = index + 1
    index += 1

num.append(int(equation[seperate_index:index])) # 마지막 숫자

'''
index 0   1   2   3   4
num   1   2   3   4   5
op    -   +   +   -   +
'''
result = 0
last_index = 0
# - 가 나오면 좌우로 묶는다
for i in range(len(op)) :
    if op[i] == '-' :
        if last_index == 0 :     # 첫 번째 -는 전부 index까지 더한다.
            result = sum(num[last_index:i+1])
            last_index = i + 1
            #print('index = ', last_index, ', i =', i)
            #print('sum = ', sum(num[last_index:i+1]))
            #print('result =', result)
            
        else :
            result -= sum(num[last_index:i+1])
            last_index = i + 1
            #print('el sum = ', sum(num[last_index:i+1]))
            #print('el result =', result)
    #print(last_index)

#print('last = ' , sum(num[last_index:]))
result -= sum(num[last_index:])   # 마지막 '-'부터 마지막 숫자까지 빼기

print(result)
