# 수열이 주어지면 큰 수부터 작은 수의 순서로 정렬(내림차순)
# 각 수를 공백으로 구분하여 출력
# 1 <= n <= 500
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

# 선택 정렬
cpy_arr = arr
for i in range(n) :
    min_idx = i
    for j in range(i+1, n) :
        if cpy_arr[min_idx] > cpy_arr[j] :
            min_idx = j
    cpy_arr[min_idx], cpy_arr[i] = cpy_arr[i], cpy_arr[min_idx]


def printResult(arr, alg) :
    print(alg)
    for i in reversed(arr) :
        print(f'{i} ', end='')
    print('')
    
printResult(cpy_arr, '선택정렬')

# 삽입 정렬
cpy_arr = arr
for i in range(1, len(cpy_arr)) :
    for j in range(i, 0, -1) :
        if cpy_arr[j] < cpy_arr[j-1] :
            cpy_arr[j], cpy_arr[j-1] = cpy_arr[j-1], cpy_arr[j]
        else :
            break
printResult(cpy_arr, '삽입정렬')

# 기본 라이브러리 정렬
cpy_arr = arr
cpy_arr = sorted(arr)
printResult(cpy_arr, '기본라이브러리')