# 클래스를 만들 때는 파스칼 표기법을 씀(첫문자는 대문자).

class Baby:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        print("응애")

    def get_name(self):
        print(self.name)
    
    def get_age(self):
        print(self.age)

new_baby = Baby('minkyung',25)
new_baby.get_name()
new_baby.get_age()