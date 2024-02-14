
def solution(s):
    answer1 = 0
    answer2 = 0
    while s != '1':
        answer2 += s.count('0')
        s = s.replace('0','')
        s = bin(len(s))[2:]
        answer1 += 1
    return [answer1, answer2]