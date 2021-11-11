# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 문자열로 반환
# numbers의 길이는 1 이상 100,000 이하
# 각 원소는 0 이상 1,000 이하
def solution(numbers) :
    answer = ''

    s_numbers = [ (str(s_num)) for s_num in numbers ]

    s_numbers = sorted(s_numbers, key=lambda x : x*3, reverse=True)

    answer = int(''.join(map(str, s_numbers)))
    return str(answer)

print(solution([6,10,2]))       # 6210
print(solution([3,30,34,5,9]))  # 9534330
print(solution([0,0]))          # 0
print(solution([21,212]))       # 21221

'''
테스트 1 〉	통과 (809.91ms, 23.9MB)
테스트 2 〉	통과 (247.67ms, 17.4MB)
테스트 3 〉	통과 (1289.27ms, 28.2MB)
테스트 4 〉	통과 (1.87ms, 10.5MB)
테스트 5 〉	통과 (641.21ms, 22.4MB)
테스트 6 〉	통과 (487.06ms, 20.8MB)
테스트 7 〉	통과 (0.03ms, 10.4MB)
테스트 8 〉	통과 (0.03ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.4MB)
테스트 10 〉	통과 (0.02ms, 10.4MB)
테스트 11 〉	통과 (0.04ms, 10.4MB)
테스트 12 〉	통과 (0.02ms, 10.4MB)
테스트 13 〉	통과 (0.02ms, 10.4MB)
테스트 14 〉	통과 (0.03ms, 10.4MB)
테스트 15 〉	통과 (0.02ms, 10.4MB)
'''