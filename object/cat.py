from animal import Animal
# animal이란 파일에서 Animal이라는 클라스를 가져옴.

class Cat(Animal): # Cat 클래스는 Animal 클래스의 기능을 물려받음

    count = 0 #Animal count가 아닌, Cat의 count임

    def __init__(self,
                 name: str = "냥",
                 age: int = 0
                 ):
        """

        Args:
            name (str, optional): 고양이의 이름. 기본값은 "냥".
            age (int, optional): 고양이의 나이. 기본값은 0.
        """

        super().__init__(age) #Animal 클래스에서 기존 같은 기능을 바로 가져옴. 단, 출력 내용은 같음.

        self.name = name # 따라서 name데이터만 받아오면 됨. age는 Animal 데이터 기능에서 바로 가져오면 됨.

        Cat.count = Cat.count + 1

        return

    def eat(self):
        print(f"고양이 '{self.name}'이 음식을 먹었습니다.")
        # Animal 메서드와 이름이 같은 eat 메서드를 만들었어도 새로운 메서드로 생성이 됨.
        
# get_age 없음 주의! 

    @classmethod
    def get_count(cls):
        print(f"고양이가 {cls.count}마리 생성되었습니다.")