
for i in range(5):
    if i >= 1 and i <= 3:
        print('*   *')
    else:
        print('*****')
# range(5)는 5개 요소가 0번~4번까지임!


r = range(5) # 0~4임
for i in r:
    if i ==0 or i == len(r) - 1: # len(r) == 5 임. 따라서 -1을 해줘야 함!!
        print('*****')
    else:
        print('*   *')
