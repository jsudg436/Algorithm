import sys
a = []

while(True):
  b = sys.stdin.readline().rstrip()
  if b == '':
    break
  a.append(b)

for i in a:
  print(i)