# import math as asdf
# from math import pow
# #  math에서 pow만 가져오기

# from re import T
# # math라고 안쓰고 asdf라는 별명을 지어줄 때 as를 사용!


# # __num = 1
# # print(__num)

# temp = None
# print("temp에 None 넣었음" + str(None))

# temp = True and False

# # assert False

# # print(temp)

# for item in range(10):
#     # 처음
#     if item == 5:
#         continue
#         # 반복문의 처음으로 돌아감
#     elif item == 8:
#         break
#         # 반복문을 멈춤
#     print(item)
# 0
# 1
# 2
# 3
# 4
# 6
# 7

# try:
#     ...
# except:
#     pass
# finally:
#     pass

# pass 혹은 ... 같음, 코드가 생각 안날 때 임시 공간 메꾸기


# try:
#     temp = '가나다'
#     temp[0] = '아'
# except:
#     print('에러가 발생했습니다.')
# finally:
#     print('마지막으로 할 것은 하겠습니다.')

# print('넘어왔습니다.')


# try:
#     temp = '가나다'
#     temp[0] = '아'
# except Exception as e:
#     print(e)
#     # e.with_traceback()
# finally:
#     print('마지막으로 할 것은 하겠습니다.')

# print('넘어왔습니다.')

# temp = 1

# for i in range(10):
#     pass

# print(temp)

# temp =1

# def my_func():
#     global temp
#     temp = 3
#     return temp

# print(my_func())

# print(temp)

# raise Exception('내가 만든 에러')

# def my_func(num):
#     print(num)


# my_func(12)
# # args 아규먼트, 인자, 인수

# my_func = lambda num : print(num)
# my_func(12)

# temp = list(filter(lambda num : num != 1, [1,2,3,1]))
# print(temp)

# def my_func():
#     while True:
#         yield 1
#         yield 2
#         yield 3


# my_yield_data = my_func()

# print(next(my_yield_data))
# print(next(my_yield_data))
# print(next(my_yield_data))
# print(next(my_yield_data))

# def my_func():
#     yield 1
#     yield 2
#     yield 3


# my_yield_data = my_func()

# print(next(my_yield_data))
# print(next(my_yield_data))
# print(next(my_yield_data))
# print(next(my_yield_data))

def check_str(data : str) :
    return data.endswith('마')

print(check_str("가나다"))

# data : str 처럼 타입까지 지정해주면 data. 입력하면 드롭다운형식으로 기능이 나옴.

