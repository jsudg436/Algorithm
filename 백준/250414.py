# 11718. 그대로 출력하기
# import sys
# a = []
#
# while(True):
#   b = sys.stdin.readline().rstrip()
#   if b == '':
#     break
#   a.append(b)
#
# for i in a:
#   print(i)



# 1316. 그룹 단어 체커
# import sys
# N = int(sys.stdin.readline())
# M = 0   # 그룹단어 개수
#
# for i in range(N):
#   # IndexError를 피하기 위해 개행문자를 포함하여 입력받음
#   str = sys.stdin.readline()
#   tmp = []
#   # 문자열의 첫번째 원소는 중복되지 않기 때문에 먼저 추가
#   tmp.append(str[0])
#   flag = 1  # 그룹단어 여부(True)
#
#   for j in range(1, len(str)):
#     if str[j] != str[j-1]:
#       if str[j] not in tmp:
#         # 새로운 문자열 등장 시 tmp에 추가
#         tmp.append(str[j])
#       else:
#         # 중복이 되었을 경우 그룹단어로 볼 수 없기 때문에 flag 변경 후 탈출
#         flag = 0
#         break
#     else:
#       continue
#   # 그룹단어 확인 후 M 증가
#   if flag == 1:
#     M += 1
# print(M)



# 25206. 너의 평점은
# import sys
# # 과목평점별 점수를 동일한 인덱스에 배치
# grd = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
# scr = [ 4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
# credit = 0.0
# num = 0.0
#
# for i in range(20):
#   str = sys.stdin.readline().split()
#   if str[2] == 'P':
#     # 등급이 P일 경우 연산하지 않고 넘어감
#     continue
#   # 과목평점에 따른 점수로 변환 후 학점과 곱연산 진행
#   credit += float(str[1])*scr[grd.index(str[2])]
#   num += float(str[1])
#
# print(credit/num)
