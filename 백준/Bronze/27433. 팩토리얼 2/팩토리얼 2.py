import sys
N = int(sys.stdin.readline())
F = 1

for i in range(1, N+1):
  F *= i

print(F)