'''
N개의 부품, 부품 번호
M개 종류의 부품을 요청받고 있으면 yes, 없으면 no
'''

n = int(input())

own_parts = sorted(list(map(int, input().split(' '))))

m = int(input())

req_parts = list(map(int, input().split(' ')))

def binary_search(array, target, start, end) :
    if start > end :
        return None
    mid = (start + end) // 2
    if array[mid] == target :
        return mid
    elif array[mid] > target :
        return binary_search(array, target, start, mid - 1)
    else :
        return binary_search(array, target, mid + 1, end)

result = ''

for p in req_parts :
    if binary_search(own_parts, p, 0, len(own_parts)-1) != None :
        result += 'yes '
    else :
        result += 'no '
print(result)