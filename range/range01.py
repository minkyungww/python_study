temp = list(range(3, 30, 3))

print(temp)

temp = list(range(0, 10))

for item in temp:
    print("안녕")

# temp = [item for item in range(0, 10)] 상동

temp = {"안녕" for item in range(0, 10)}
# {}은 set이다. set은 중복된 데이터는 하나만 출력됨.
# {'안녕'}

temp = ["안녕" for item in range(0, 10)]
['안녕', '안녕', '안녕', '안녕', '안녕', '안녕', '안녕', '안녕', '안녕', '안녕']

print(temp)
