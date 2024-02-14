# def solution(n, left, right):
#     a = []
#     answer=[]
#     for i in range(0, n):
#         a.append(list(range(n)))

#     for i in range(0, n):
#         for j in range(0, i+1):
#             a[i][j] = i + 1
#         for j in range(0, i):
#             a[j][i] = i + 1

#     for i in a:
#         answer+=i

#     return answer[left:right+1]

def solution(n, left, right):
    answer = []

    for i in range(left // n, right // n + 1):
        for j in range(0, n):
            if j < i:
                answer.append(i + 1)
            else:
                answer.append(j + 1)
    return answer[left % n:right - (left // n) * n + 1]