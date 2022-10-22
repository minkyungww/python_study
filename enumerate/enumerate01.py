# temp = {'a', 'b', 'c'}

# for item in temp:
#     print(item)
# # set은 시퀀스가 아니기 때문에 출력 순서가 계속 바뀜

# temp = {'a', 'b', 'c'}
# temp = enumerate(temp)

# for num, value in temp:
#     print(num, value)

a, b = (1, 2)
print(a)
print(b)
# 앞, 뒤 개수만 맞춰서 지정하면 변수에 들어감
#     a, b =(1, 2, 3), 이렇게 앞, 뒤 변수 개수가 다르면 에러남
# ValueError: too many values to unpack (expected 2)


a, b = {'name': '이름', 'age': 12}
print(a)
print(b)
# 키 값만 나옴
# name
# age

a, b = {'name': '이름', 'age': 12}.items()
print(a)
print(b)
# .items()를 사용하면 튜플형식으로 출력됨
# ('name', '이름')
# ('age', 12)
