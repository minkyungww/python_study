# name = 'minkyung'
# age = 10
# # print('내 이름은 '+ name + " 내 나이는 " + str(age)) #ctrl+/ 누르면 주석으로 처리됨. 그럼 코드 실행이 안됨.
# # 다시 누르면 코딩 처리됨.

# # print(f"내 이름은 {name} 내 나이는 {age}")
# # print(f"내 이름은 {name} 내 나이는 {age}") #ctrl+d 누르면 바로 다음 행에 복사됨.
# #f는 format를 뜻함.

# # print(f"{name=} {age=}")

# # print("내 이름은 %s 내 나이는 %d" %(name, age))
# # print("내 이름은 {0} 내 나이는 {1}".format(name, age)) #컴퓨터에서는 0번인 첫 번째 순서임.
# # print("내 이름은 {0} 내 나이는 {0}".format(name, age)) #이렇게 하면, name만 출력됨.
# # print("내 이름은 {n} 내 나이는 {a}".format(n=name, a=age)) #format에 제목을 지정해줘서, 제목을 입력해도 됨.


# my_list = [1,2,3,4]
# my_list[0] = 9
# print(my_list)
# #0번은 첫 번째를 뜻함, list(가변)여서 바로 수정 가능


# # for element in my_list:
# #     print(element)

# string = "가나다라 마바사"
# # string[0] = '하'
# # pring(string)
# #에러남. 왜냐하면 문자형(불변)이여서 동일 방법으로 바로 수정 불가

# # char_list = string.split(' ')
# # print(char_list)

# change_string = string.replace('가', '하')
# print(change_string)
# #따라서 좌측의 변수를 가공해서 새로운 변수로 지정해줘야 함

# print(id(string)) 
# print(id(change_string))
# #id()는 변수 id를 확인할 수 있음 -> 같은 변수인지 아닌지 확인 용이

# data1 = '가나다'
# data2 = '가나다'
# print(id(data1))
# print(id(data2))
# #단, 같은 데이터는 같은 변수 id를 가짐, 숫자와 문자에만 적용됨!!

# list1 = [1,2,3]
# list2 = [1,2,3]
# print(id(list1))
# print(id(list2))
# #list형은 다른 변수 id가 나옴

# data = int(input())

# if data == 1: # == 는 '같다'
#     print("1이다")
# elif data == 2:
#     print("2이다")
# else:
#     print("모르겠다") 

# x = 1
# while  x <10:
#     print("가나다")
#     x = x+1
        
# for item in [1,2,3,4]:
#     print(item)

from pickle import FALSE, TRUE
from re import T
from unittest import result


# def check_data(): #def는 함수를 만들 때 사용
    
#     data = int(input())
#     if data == 1: # == 는 '같다'
#         print("1이다")
#     elif data == 2:
#         print("2이다")
#     else:
#         print("모르겠다") 

# while TRUE:
#     check_data()


# def sum_two_num(n1, n2):
#     return n1 + n2

# sum_num = sum_two_num(1 ,3)
# print(sum_num)
    

# print(not False)

# result = not (1 != 2)
# print(result)

# # my_set = {1,2,3,4,1,1,1,1}
# my_set = set([1,2,3,4,1,1,1,1])
# print(my_set) 
# #집합에서는 중복된 데이터는 하나만 출력됨

# for item in my_set:
#     print(my_set)

# my_dict = {"score" : "good", "age" : 18}
# print(my_dict["score"])

# my_dict = {"score" : "good", "age" : 18}
# for key, value in my_dict.items():
#     print(f"{key} 은/는 {value}")


my_tuple = (1,2,3,4, 4, 1)

my_tuple[0] = 1 #에러남, 왜냐하면 튜플은 불변이기 때문에 내부적으로 바꿀 순 없음

my_tuple = (58, 2) #작동됨, 외부적으로 바꿔치기는 가능

print(my_tuple)

for item in my_tuple:
    print(item)



