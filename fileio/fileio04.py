# 파일 읽기
# mode r은 파일 읽기(read)

file_editor = open(file="fileio/test.txt", mode="r", encoding="utf-8")

# readlines()는 파일 데이터를 한 줄 씩 배열로 가져온다.
my_text = file_editor.readlines()


file_editor.close()

print(my_text)
# ['안녕하세요.\n', '반갑습니다.']
