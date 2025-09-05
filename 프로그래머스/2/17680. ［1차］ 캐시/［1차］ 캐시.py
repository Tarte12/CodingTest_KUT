def solution(cacheSize, cities):

    cities = [city.lower() for city in cities]
    #대소문자 구별 X -> 다 소문자로 만들어서 신경 ㄴㄴ
    time = 0
    space = [] #city 담을 공간
    
    if cacheSize == 0:
        return 5 * len(cities)
        
    for city in cities: #LRU 알고리즘으로 도시 처리
        if city in space: #이미 space에 city 있음 cache hit
                space.remove(city) #기존 위치 제거
                space.append(city) #맨뒤로 이동
                time += 1
                continue
        #if 꽉 차지 않고 city 없음
        if len(space) < cacheSize: 
            # space에 city 없음 cache miss
                space.append(city)             
                time += 5
        #else 꽉 차고 city 없음
        else: 
            space.pop(0) #제일 오래된 값 지우기
            space.append(city) #최신값 맨 뒤로
            time += 5
            
    return time


