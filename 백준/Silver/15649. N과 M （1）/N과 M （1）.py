N, M = map(int, input().split())

def all(N, M):
  used = [False] * (N + 1)  # 사용된 숫자를 체크하기 위한 리스트
  backtrack(N, M, 0, [], used)

def backtrack(N, M, level, sol, used):
  if level == M:
    print(' '.join(map(str, sol)))
    return

  for i in range(1, N + 1):
    if not used[i]:
      sol.append(i)
      used[i] = True
      backtrack(N, M, level + 1, sol, used)
      sol.pop()
      used[i] = False

all(N, M)