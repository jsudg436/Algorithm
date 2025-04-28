import sys
N = int(sys.stdin.readline())

a = N // 5
b = N - (5 * a)

while(True):
  if(a == -1):
    print(-1)
    break
  elif(b % 3 == 0):
    print(a+(b // 3))
    break
  else:
    a -= 1
    b += 5