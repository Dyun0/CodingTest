
import re

def solution(s):
    answer=[]
    num = []

    s = re.sub("[\},{\{{\}}\,]", " ", s)
    s=s.split()
    for i in s:
        if i.isdigit():
            num.append(int(i))
    dict = {}
    for i in num:
        if i in dict.values():
            continue
        else:
            dict[num.count(i)] = i
    sortDict = sorted(dict.items(), reverse=1)

    for i in sortDict:
        answer.append(i[1])
    return answer