# 01_Immigration_.py
#!/usr/bin/python3

def solution(n, times):
    answer = 0
    smaller_value = min(times) * n
    bigger_value = max(times) * n
    while smaller_value <= bigger_value:
        median_value = (smaller_value+bigger_value)//2
        comp = 0

        for t in times:
            comp = 

        if():
            smaller_value = median_value + 1
        else if(comp):
            bigger_value = median_value - 1


    return answer

if __name__ == "__main__":
    print(solution(6, [7,10]))
