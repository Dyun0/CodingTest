def solution(triangle):
    triangle.reverse()
    for index1, i in enumerate(triangle):
        if index1 == 0:
            continue
        for index2 in range(len(i)):
            if triangle[index1-1][index2] >= triangle[index1-1][index2+1]:
                triangle[index1][index2] = triangle[index1-1][index2] + triangle[index1][index2]
            else:
                triangle[index1][index2] = triangle[index1-1][index2+1] + triangle[index1][index2]
    return triangle[-1][0]