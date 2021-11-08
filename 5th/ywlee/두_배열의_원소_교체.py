# N 개 원소를 갖는 배열 A, B
# K 번 A, B 배열의 원소를 바꿔치기 할 수 있음
# A 배열 원소의 합이 최대가 되도록
# ==> A, B 배열을 정렬 후 B 배열의 가장 큰 원소부터 K개와 A 배열의 가장 작은 원소 K개를 바꿔치기

import copy

n , k = map(int, input().split(' '))

a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

# 선택 정렬
def s_sort(array):
    arr = copy.deepcopy(array)
    a_len = len(arr)
    for i in range(a_len) :
        min_idx = i
        for j in range(i+1, a_len) :
            if arr[min_idx] > arr[j] : # 만약 가장 값이 작은 인덱스면
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

sorted_a = s_sort(a)
sorted_b = s_sort(b)

print(a)
print(b)
print(sorted_a)
print(sorted_b)

def replacement(_a, _b, _k) :
    for i in range(k) :
        if _a[i] < _b[-i-1] :
            print(f'a[{i}]={_a[i]} <-> b[{-i-1}]={_b[-i-1]}')
            _a[i] = _b[-i-1]
    print(_a)
    return sum(_a)

print(replacement(sorted_a, sorted_b, k))

# 기본 라이브러리 정렬
sorted_a = sorted(a)
sorted_b = sorted(b)

print(a)
print(b)
print(sorted_a)
print(sorted_b)
print(replacement(sorted_a, sorted_b, k))