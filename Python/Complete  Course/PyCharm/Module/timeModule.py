import sys
import time

def printTime():
    tm = time.time()
    print(tm)

def numbers(max):
    time1=time.time()
    for i in range(0,max):
        print(i)
        time2=time.time()
    print("Cost time : " + str(time2-time1))


def forLoopTime(max):
    start = time.time()
    for i in range(0, max):
        print(str(i))
    stop = time.time()
    print(str(stop - start))

print(time.asctime())
tuple = (2000, 10, 15, 16, 36, 22, 0, 0, 0)
print(time.asctime(tuple))

tuple = (2000, 10, 15, 16, 36, 22, 50, 5, 0)
# tuple=(年,月,日,時,分,秒,星期幾?, X , X)
print(time.asctime(tuple))  # asctime(自定義時間組) : 回傳時間格式

t = time.localtime()
print(str(time.localtime())) #localtime() : 輸出現在時間，型態為list

year = str(t[0])
month = str(t[1])
day = str(t[2])
hour = str(t[3])
min = str(t[4])
sec = str(t[5])
print(month + "/" + day)

for i in range(0,5):
    print(i)
    time.sleep(1)  #sleep(秒) : 主執行緒，時間停頓