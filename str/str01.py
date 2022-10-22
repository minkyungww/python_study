temp = "가나다"
print(f"{temp[0]}")
# 문자열은 요소를 번호로 가져올 수 있다.
# 가

# temp[0] = '라'
# # 문자열은 불변이라 내부적 요소를 변경할 수 없다.
# # TypeError: 'str' object does not support item assignment

temp = '라'
print(f'{temp=}')
# 변수에 다른 문자열을 넣을 수는 있다.
# temp='라'

# del temp
# print(temp)
# # 변수를 삭제한다.
# # 출력 시 에러 발생
# # NameError: name 'temp' is not defined

temp = "가나다"
print(f"{id(temp)=}")
temp = "라"
print(f"{id(temp)=}")
temp = "가나다"
print(f"{id(temp)=}")
# id(temp)=1738999079888
# id(temp)=1738999244368
# id(temp)=1738999079888
# 같은 문자열, 숫자는 변수 id명이 같음

temp = "가나다\n라마바"
print(f"{temp}")
# 문자열을 여러줄로 출력하고 싶으면 \n 사용한다.
# 가나다
# 라마바

temp = """\
가나다
마바사"""
print(temp)

temp = '그가 말했다. "안녕하세요"'
print(f'{temp}')
# 쌍따옴표를 문자열 안에 넣고 싶을 때 홀따옴표로 감싼다.
# 그가 말했다. "안녕하세요"

temp = "나는 생각했다. '잠온다'"
print(f'{temp}')
# 나는 생각했다. '잠온다'

temp = """그가 말했다. "안녕하세요" 나는 생각했다. '잠온다' \""""
print(temp)
# 쌍따옴표 홀따옴표 모두 넣을 경우 """ 또는 ''' 를 사용
# 그가 말했다. "안녕하세요" 나는 생각했다. '잠온다'

temp = temp[0:4]
print(temp)
# 시퀀스는 대괄호를 이용해서 잘라낼 수 있다.
# 그가 말

temp = '가나다라'
temp = temp[-1]
print(temp)
# -1은 마지막 요소를 가져옴

# temp = temp[4]
# print(temp)
# # 범위는 0부터 세야함. 범위를 넘어가는 요소 번호를 호출하면 에러가 발생한다
# # IndexError: string index out of range

temp = '가나다라'
temp = temp[-4]
print(temp)
# -1이 마지막 요소이니, 가나다라에서 '가'는 -4임. -5를 입력하면 our of range 에러가 발생함.

temp = "가나다라"
temp = temp[1:]
print(f"{temp=}")
# 1번(두 번째 요소)부터 끝까지
# 나다라

temp = "가나다라"
temp = temp[:2]
print(temp)
# 가나

temp = "가나다라"
temp = temp[1:100]
print(temp)
# 파이썬 문자열 컷팅은 유연하다
# 나다라

temp = "가나다라"
temp = temp[-100:100]
print(temp)
# 파이썬 문자열 컷팅은 유연하다
# 가나다라

temp = "가나다라"
temp = temp[30:100]
print(temp)
# 없는 범위는 안나올 뿐, 에러가 나진 않음.

for item in temp:
    print(item)
# 문자열을 반복 가능하다

temp = "가나"  "다라"
print(temp)
# 가나다라

temp = ("가나"
        "다라"
        "여러줄"
        '쓰고싶어요')
print(temp)
# 가나다라여러줄쓰고싶어요

# temp = len(temp)
# print(temp)
# # 문자열의 길이를 알고 싶으면 len 함수를 사용한다
# # 12

temp = temp[len(temp) - 1]
print(temp)
# len과 마지막 요소는 1개 차이남. len 이 1숫자 더 많으니 빼기를 해줘야 함
# -1를 안하면 에러가 남: TypeError: object of type 'int' has no len()
# 요

temp = "가나다라"
temp = f"한글은 {temp}"
print(f"{temp=}")
# f"" 혹은 f''를 이용해서 변수를 문자열에 입력할 수 있다.
# temp='한글은 가나다라'

temp = "가나다라"
temp = "한글은 " + temp
print(f"{temp=}")
# temp='한글은 가나다라'

temp = "가나다라"
temp = "한글은 %s" % temp
print(f"{temp=}")
# temp='한글은 가나다라'

temp = "가나다라"
temp = "한글은 {0}".format(temp)
print(f"{temp=}")
# temp='한글은 가나다라'

temp = "가나다라"
temp = "한글은 {1}".format(temp, 12)
print(f"{temp=}")
# temp='한글은 12'

temp = "가나다라"
temp = "한글은 {arg1}".format(arg1=temp)
print(f"{temp=}")
# temp='한글은 가나다라'

temp = '가나다라'
temp = temp.startswith("가나")
print(f"{temp=}")
# 문자열의 시작을 확인하여 True False로 리턴한다
# temp=True

temp = '가나다라'
temp = temp.endswith("다라")
print(f"{temp=}")
# temp=True

temp = '가나다라'
temp = temp.index("가")
print(f"{temp=}")
# index는 해당 문자(문자열)의 요소 번호를 리턴하낟
# temp=0

temp = '1'
temp = temp.zfill(3)
# 숫자 자릿수를 만들어줌. 빈 자리는 0으로 채운다
# temp='001'


temp = '1'
temp = temp.rjust(5, '!')
# 숫자뿐만 아니라, 내가 원하는 문자로 채울 수 있음
# temp='!!!!1'

print(f"{temp=}")
