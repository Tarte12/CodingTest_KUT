from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    nums = set()  # 중복 방지용 set

    # 1자리부터 len(numbers)자리까지 모든 순열 생성
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            num = int(''.join(p))
            nums.add(num)

    # 소수 판별 후 개수 세기
    cnt = 0
    for num in nums:
        if is_prime(num):
            cnt += 1

    return cnt
