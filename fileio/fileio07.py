# 바이너리 파일 입력


# with open(file = "fileio/bin.txt", mode="bw", encoding="utf-8") as file_editor:
#     file_editor.write(bytes('aa',encoding='utf-8'))
# 에러남. 바이너리를 인코딩할 때는 utf-8을 쓰면 안됌

with open(file = "fileio/bin.txt", mode="bw") as file_editor:
    file_editor.write(b'aa')