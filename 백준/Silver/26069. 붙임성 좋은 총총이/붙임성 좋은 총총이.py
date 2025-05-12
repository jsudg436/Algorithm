import sys
N = int(sys.stdin.readline())   # 사람들이 만난 기록 수 입력
rbw = {'ChongChong'}            # 무지개 댄스를 추고 있는 사람의 목록(처음엔 ChongChong 한명), 중복 제거를 위해 set으로 선언언

for i in range(N):
  str = sys.stdin.readline().rstrip()           # 만난 사람들의 이름 입력
  for j in rbw:
    if str.find(j) != -1:                       # 만난 사람들의 이름 중 무지개 댄스를 추고 있는 사람이 있는지 rbw에서 find
      rbw.update([str.replace(j, '').strip()])  # 무지개 댄스를 추고 있는 사람이 있다면 이를 삭제하하고 공백 제거 후 rbw에 추가
      break                                     # 반복문 탈출

print(len(rbw))                 # 마지막 기록 이후 무지개 댄스를 추는 사람의 수를 출력