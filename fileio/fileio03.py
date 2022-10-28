# 파일 읽기
# mode r은 파일 읽기(read)

file_editor = open(file="fileio/test.txt", mode="r", encoding="utf-8")

# readline()는 파일에서 한 줄씩 데이터를 가져온다.
my_text = file_editor.readline()
my_text1 = file_editor.readline()
my_text2 = file_editor.readline()
my_text3 = file_editor.readline()

file_editor.close()

print(my_text)
print(my_text1)
print(f"{my_text2=}") #값이 없어도 line을 가져옴
print(f"{my_text3=}")
# 안녕하세요.

# 반갑습니다.

# print(,end='\n')이 사실 디폴트값이기 때문에 한 줄 띄어서 나옴.
