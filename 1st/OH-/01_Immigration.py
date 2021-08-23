# 01_Immigration_.py
#!/usr/bin/python3

def solution(n, times):
    answer = 0
    smaller_value = 0
    bigger_value = max(times) * n
    while( smaller_value <= bigger_value ):
        med_value = (smaller_value+bigger_value)//2
        comp = 0

        for t in times:
            comp += med_value//t
            if( comp >= n ):
                answer = med_value
                bigger_value = med_value - 1
                break

        if(comp < n):
            smaller_value = med_value + 1

    return answer


if __name__ == "__main__":
    print(solution(6, [7,10]))
