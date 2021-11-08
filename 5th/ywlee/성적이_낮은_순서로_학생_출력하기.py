# N 명의 학생
# 학생의 이름과 성적으로 구분
# 성적이 낮은 순서대로 학생의 이름을 출력
# 1 <= N <= 100,000

n = int(input())
students = []
for i in range(n) :
    n = input().split(' ')
    students.append([n[0], int(n[1])])

# 퀵 정렬
def quick_sort(arr, start, end) :
    if start >= end : # 원소가 1개면 종료
        return
    pivot = start

    left = start + 1
    right = end
    while left <= right :
        # 피봇보다 큰 데이터를 찾을 때까지 left를 증가
        while left <= end and arr[left][1] <= arr[pivot][1]:
            left += 1
        # 피봇보다 작은 데이터를 찾을 때까지 right를 감소
        while right > start and arr[right][1] > arr[pivot][1]:
            right -= 1
        if left > right: # 엇갈림
            arr[right], arr[pivot] = arr[pivot], arr[right] # 작은 데이터와 피봇을 swap
            # 조건에 의해 while 탈출, swap된 피봇을 기준으로 좌,우가 분할됨
        else :           # 엇갈리지 않고 작은 데이터와 큰 데이터를 찾음
            arr[left], arr[right] = arr[right], arr[left]   # 작은 데이터와 큰 데이터의 위치를 swap
    
    # 분할 된 왼쪽, 오른쪽 각각 정렬 수행
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)
    
quick_sort(students, 0, len(students)-1)

result = ''
for i in students :
    result += f'{i[0]} '
print(result)