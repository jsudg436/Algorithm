import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
A.sort()

for i in B:
  if i < A[0] or i > A[-1]:
    print(0)
  elif i in A:
    print(1)
  else:
    print(0)