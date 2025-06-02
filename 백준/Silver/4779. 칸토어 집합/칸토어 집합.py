import sys

while(True):
  try:
    N = int(sys.stdin.readline())
    M = '- -'

    if N == 0: print('-')
    elif N == 1: print(M)
    else:
      for i in range(N-1):
        tmp = M
        M += (' '*len(M))
        M += tmp
      print(M)
  except:
    break