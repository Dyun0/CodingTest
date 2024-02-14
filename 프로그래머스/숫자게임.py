def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    answer=0
    while B:
        if A[-1] < B[-1]:
            A.pop()
            B.pop()
            answer+=1
        else:
            B.pop()
    return answer