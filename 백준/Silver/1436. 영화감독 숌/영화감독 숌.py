import sys
N = int(sys.stdin.readline())
num = -1
flag = 0

while N > 0:
  num += 1
  M = str(num)
  if '666' in M:
    N -= 1

print(num)