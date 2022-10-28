# import time


file_editor = open(file="fileio/test.txt", mode="w", encoding="utf-8")
#fileio/test.text  -> fileio라는 파일 내에 test.text 생성
# mode w는 write 모드, 파일 안에 무언가 쓰고 싶을 때
 
file_editor.write("안녕하세요.")

# time.sleep(10)
# CPU가 과부하되지 않도록 일부로 슬립을 걸어두는 것임.

# 파일을 open 했으면 반드시 close 해주는 것이 좋다. 
# 열어있는 파일을 닫지 않고 다시 사용하려고 하면 오류가 발생한다.
file_editor.close()


print("작업종료" )

