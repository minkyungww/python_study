# 파일 삭제
import os
# 파일 삭제는 파이썬 기능이 아니라, window os에서 해주는 기능이여서 import 해야함

# print(os.path.exists('test.txt'))
# if os.path.exists('test.txt'):
#     os.remove('test.txt')

# 위처럼 하면 실행이 안됨, 왜냐믄 파일경로 지정을 안해줬기 때문에 해당 파일을 찾을 수 없음

# 1번 방법
# if os.path.exists('fileio/test.txt'):
#     os.remove('fileio/test.txt')
    
# 2번 방법
# os.system('rm fileio/test.txt')

# 파일 및 모든 폴더 삭제
# os.system('rm -r fileio/')
# 
# 파일 및 모든 폴더 강제삭제, 알림창 안뜸
# os.system('rm -rf fileio/')