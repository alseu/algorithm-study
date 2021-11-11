# 논문 n편 중 h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index
# 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations, H-Index를 return

def solution(citations) :
    answer = 0
    n = len(citations)
    citations.sort(reverse=True)
    if citations[0] == 0 :
        return answer

    # 전체 논문의 개수 만큼 h-index가 증가할 수 있는데
    # 인용 횟수(citations[i])가 많은 것부터 확인해가면서
    # 만약 어떤 인용 횟수가 인용한 논문의 횟수(i)보다 크면 h-index를 하나씩 증가시키고
    # 만약 어떤 인용 횟수가 인용한 논문의 횟수보다 작으면 h-index는 더이상 커질 수 없기 때문에 탈출
    for i in range(n) :
        if i < citations[i] :
            answer += 1
        else :
            break
    return answer

print(solution([3,0,6,1,5]))
