# 파일 수정
# mode a는 파일을 수정(append)하는 거다, 이어서 작업 가능; w는 새로 덮어씌어짐

file_editor = open("fileio/test.txt", mode="a",encoding="utf-8")

file_editor.write("\n반갑습니다.")

file_editor.close()
