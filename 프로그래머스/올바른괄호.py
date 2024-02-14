# 3차 틀림 (시간 초과)
# def solution(s):
#     answer = True
#     while s:
#         if s == s.replace('()',''):
#             answer = False 
#             break
#         s = s.replace('()','') 
#     return answer



#2차 맞음
def solution(s):
    count_bracket = 0
    answer = True
    for bracket in s:
        if bracket == '(':
            count_bracket += 1
        else:
            count_bracket -= 1
        if count_bracket < 0 :
            answer = False
            break
        if s[0] == ')':
            answer = False
            break
    if count_bracket != 0 :
        answer = False
            
    return answer

#1차 틀림
#answer = (s.count('()') % 2==0)