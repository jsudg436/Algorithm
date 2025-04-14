import sys
# 과목평점별 점수를 동일한 인덱스에 배치
grd = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
scr = [ 4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
credit = 0.0
num = 0.0

for i in range(20):
  str = sys.stdin.readline().split()
  if str[2] == 'P':
    # 등급이 P일 경우 연산하지 않고 넘어감
    continue
  # 과목평점에 따른 점수로 변환 후 학점과 곱연산 진행
  credit += float(str[1])*scr[grd.index(str[2])]
  num += float(str[1])

print(credit/num)