
def solution(record):
    result = {}
    answer = []

    for i in record:
        command = i.split()
        if command[0] == 'Enter':
            result[command[1]] = command[2]

        elif command[0] == 'Change':
            result[command[1]] = command[2]

    for i in record:
        command = i.split()
        if command[0] == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(result[command[1]]))

        elif command[0] == 'Leave':
            answer.append("{}님이 나갔습니다.".format(result[command[1]]))

    return answer