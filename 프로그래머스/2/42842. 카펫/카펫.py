def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for height in range(3, total + 1):
        if total % height == 0:
            width = total // height
            
            if (width - 2)*(height -2) == yellow:
                return [width, height]
              
    return answer