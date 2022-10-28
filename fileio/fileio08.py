import pickle

# 바이너리 파일 입력

with open(file = "fileio/bin.pickle", mode="bw") as file_editor:
    pickle.dump([1,2,3], file_editor)
    
# 파일이 정상적으로 생성되지만, 인코딩을 안해서 읽을 수는 없음. 단, 데이터는 잘 입력되어 있음
# 출력하면 데이터가 들어있는지 확인 가능
