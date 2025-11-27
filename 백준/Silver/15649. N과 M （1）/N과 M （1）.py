n, m = map(int, input().split())

visited = [False] * (n+1) #방문 체크
selected = []

def backtrak(): 
	# 1) 종료 조건: 수열 중 m개를 다 골랐으면 (길이가 m인 수열)
	if len(selected) == m:
		print(*selected) #*selected가 뭐임 => 리스트 풀어서 개별인자로 출력
		return

	# 2) 1~n 숫자 중 아직 안 쓴 숫자 선택
	for num in range(1, n+1):
		if not visited[num]:
			visited[num] = True #True는 다시 가지 않아 중복 X
			selected.append(num) 
			backtrak() #재귀로 다음 자리 탐색
			selected.pop() #백트래킹(도로 빼기)
			visited[num] = False #방문 해제
backtrak()