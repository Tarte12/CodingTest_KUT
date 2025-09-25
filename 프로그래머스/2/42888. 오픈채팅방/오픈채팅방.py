def solution(record):
    answer = []
    users = {}

    # 1. record 파싱해서 users 딕셔너리 최신화
    for i in record:
        parts = i.split()
        action = parts[0]
        uid = parts[1]

        if action == "Enter":
            nickname = parts[2]
            users[uid] = nickname
        elif action == "Change":
            nickname = parts[2]
            users[uid] = nickname
        # Leave는 닉네임 업데이트 없음

    # 2. 다시 record 돌면서 메시지 생성
    for i in record:
        parts = i.split()
        action = parts[0]
        uid = parts[1]

        if action == "Enter":
            answer.append(f"{users[uid]}님이 들어왔습니다.")
        elif action == "Leave":
            answer.append(f"{users[uid]}님이 나갔습니다.")
        # Change는 메시지 없음

    return answer
