def solution(people, limit):

    count = 0 #구명보트 사용 횟수
    people.sort(reverse=True)

    main = 0 #메인으로 태울 사람
    sub = len(people)-1 #서브로 태울 사람
    
    while main <= sub:
        
        if main == sub:
            count += 1
            break
        
        sum_per = people[main] + people[sub]
        
        if sum_per > limit:
            main += 1 #하나만 태웠으니까 main만 포인터 이동
            count += 1
        else: #sum_per <= limit
            main += 1
            sub -= 1 #둘 태웠으니까 둘 다 이동
            count += 1
  
    return count
