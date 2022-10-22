temp ='*'
for i in range(6):
    print(temp*i)
#  트리 만들기

for i in range(5):
    print('*****')

for i in range(5):
    print(''.rjust(5,'*'))

[print('*' * 5) for i in range(5)]

# 정사각형 만드릭, 3개 다 같은 방법

# print('*')
# print('*')
# # *
# # *
# # 세로로 출력. 사실 해당 식은 print('*', end='\n')으로 기본설정이 되어 있음.

# print('*', end='')
# print('*', end='')
# #  ** , 가로로 출력

print('*', end='하하')
print('*', end='')
#  *하하*

for item in range(5):
    for item1 in range(5):
        print('*', end='')
    print()