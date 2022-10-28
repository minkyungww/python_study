class Animal:

    count = 0

    def __init__(self,
                 age: int = 0
                 ):
        """

        Args:
            age (int, optional): 동물의 나이. 기본값은 0.
        """
        #위는 함수에 대한 변수 설명을 넣어줌, def식 안에 쌍따옴표(") 3번 누르고 드롭다운 선택하면 됨. 


        self.age = age

        self.name = f"{Animal.count}번"

        Animal.count = Animal.count + 1

        return

    def eat(self): # self는 인스턴스 메소드를 뜻함
        print(f"동물 {self.name}이 음식을 먹었습니다.")

    def get_age(self):
        print(f"동물 '{self.name}'의 나이는 {self.age}살 입니다.")

    @classmethod # @...는 함수 어노테이션을 다는 것임. 함수에 대한 속성을 명시.
    def get_count(cls): # cls는 클래스 메소드를 뜻함
        print(f"동물이 {cls.count}마리 생성되었습니다.")

    @staticmethod
    def hello(): # 인스턴스나 클라스 메소드가 아님
        print(f"동물 농장에 오신 것을 환영합니다.")
   