import math


def solution(progresses, speeds):
    answer = []
    Max = 0
    count = 1
    for i, j in zip(progresses, speeds):
        days = math.ceil((100 - i) / j)
        if Max == 0:
            Max = days
        elif Max < days:
            answer.append(count)
            Max = days
            count = 1
        else:
            count += 1
    else:
        answer.append(count)
    return answer