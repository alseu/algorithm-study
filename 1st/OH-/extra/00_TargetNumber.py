#00_TargetNumber.py

def solution(numbers, target):
    if(len(numbers) == 1):
        if( (numbers[0] == target)or(numbers[0] == -target)):
            return 1
        else:
            return 0
    else:
        return solution(numbers[0:-1], target+numbers[-1]) + solution(numbers[0:-1], target-numbers[-1])


if __name__ == "__main__":
    print(solution([1,1,1,1,1], 3))     #5
