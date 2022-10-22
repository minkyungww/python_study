from ast import Return


temp = [1, 2] + [3, 4]
# [1,2,3,4] list 합체
temp.append(5)  # 숫자 추가
temp.remove(1)  # 숫자 제거
print(temp)
#[2, 3, 4, 5]

temp = [1, 1, 1, 1]
temp.remove(1)
# 모든 같은 데이터를 지우지는 않는다
# 하나만 지운다
# [1, 1, 1]

temp = [1, 1, 2, 3, 1, 1]


def check(num):
    if num == 1:
        return False
    else:
        return True

# print(check(2323))
# True


temp = filter(check, temp)
# filter에 False가 떨어지면 지우고, True 값이 떨어지면 남긴다
temp = list(temp)
print(temp)
# [2, 3]

# temp = [1,2,3,4,5] # 1차원
temp = [[1, 2], [3, 4]]  # 2차원, 행렬배열
print(temp[0])
# 첫 번째 2차원 배열을 가져옴
# [1, 2]

temp = [[1, 2], [3, 4]]  # 2차원, 행렬배열
print(temp[0][0])
# 첫 번째 2차원 배열에서 첫 번째 요소(차원을 타고타고 들어가면 원하는 요소를 가져올 수 있음)
# 1

temp = [
    {'key':'value', 'name': '이름'},
    {'a', 'b'}    
]

print(temp[0]['name'])
# 이름