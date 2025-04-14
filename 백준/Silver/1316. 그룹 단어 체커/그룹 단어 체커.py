import sys
N = int(sys.stdin.readline())
M = 0   # 그룹단어 개수

for i in range(N):
  # IndexError를 피하기 위해 개행문자를 포함하여 입력받음
  str = sys.stdin.readline()
  tmp = []
  # 문자열의 첫번째 원소는 중복되지 않기 때문에 먼저 추가
  tmp.append(str[0])
  flag = 1  # 그룹단어 여부(True)

  for j in range(1, len(str)):
    if str[j] != str[j-1]:
      if str[j] not in tmp:
        # 새로운 문자열 등장 시 tmp에 추가
        tmp.append(str[j])
      else:
        # 중복이 되었을 경우 그룹단어로 볼 수 없기 때문에 flag 변경 후 탈출
        flag = 0
        break
    else:
      continue
  # 그룹단어 확인 후 M 증가
  if flag == 1:
    M += 1

print(M)