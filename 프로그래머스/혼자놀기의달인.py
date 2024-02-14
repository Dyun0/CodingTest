def solution(cards):
    box_groups = []
    box_group = []
    i = 0
    for i in range(len(cards)):
        if i>0 and cards[i] == 0:
            i+=1
            continue
        while True:
            if cards[i] ==0:
                break
            box_group.append(i+1)
            j = cards[i] - 1
            cards[i] = 0
            i=j
        if len(box_group) > 0:
            box_groups.append(box_group)
            box_group = []
        if cards.count(0) == len(cards):
            break
        i+=1
    answers = [len(j) for j in box_groups]
    answers.sort(reverse=True)
    if len(answers)==1:
        answer = 0
    else:
        answer = answers[0]*answers[1]
    return answer