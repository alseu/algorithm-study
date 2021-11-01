# 수열이 주어지면 큰 수부터 작은 수의 순서로 정렬(내림차순)
# 각 수를 공백으로 구분하여 출력
# 1 <= n <= 500
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

# 선택 정렬
for i in range(n) :
    min_idx = i
    for j in range(i+1, n) :
        if arr[min_idx] > arr[j] :
            min_idx = j
            print(min_idx)
    arr[min_idx], arr[i] = arr[i], arr[min_idx]

print(arr)
