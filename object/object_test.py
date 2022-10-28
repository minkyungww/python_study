from animal import Animal
from cat import Cat
from dog import Dog

Animal.hello()

print()  # 그냥 한 줄 띄어쓰기할려고 넣음

a = Animal(12)
b = Cat("나옹", 5)
c = Dog(age=10, name='멍뭉이')
# name: str ='멍' 기본값을 설정해주고, name파라미터는 생략하되 기본값은 출력하고 싶으면
# c=Dog(,10)이 아닌,
# c=Dog(age=10)을 해줘야 "동물 '멍'의 나이는 10살 입니다."라고 출력됨.
# c = Dog(age=10, name ='d'), 이렇게 아규먼트명을 써주면, 파라미터 순서는 상관 없음.

#  def __init__(self,
#                  name,
#                  age: int = 0
#                  ):

# 이렇게 name 파라미터만 생성하고, 기본값을 지정안하면, name파라미터는 무조건 지정해줘야 함
# c = Dog('멍뭉이',age=10) 이런식으로.

a.eat()
b.eat()
c.eat()

print()

a.get_age()
b.get_age()
c.get_age()

print()

Animal.get_count()
Cat.get_count()
Dog.get_count()
