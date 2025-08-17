import math
def solution(numer1, denom1, numer2, denom2):
    numer = numer1*denom2 + numer2*denom1
    denom = denom1*denom2
    
    #최대공약수 내장 함수 gcd
    gcd = math.gcd(numer, denom)
    answer = [numer // gcd, denom // gcd]
    
    return answer