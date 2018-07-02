# coding=utf-8
#一個中文佔三個字元
file = open("Rap.txt")
print("原文 : \n" + file.read() + "\n")

position = file.tell(); #tell() 回傳檔案指標的位置
print("Position : " + str(position) + "\n")
position = file.seek(0, 0)

################READ#####################
file = open("Rap.txt", "w+")  # mode = w+ 可寫入又可讀
team1 = open("Kruis Wu team")
file.write("\n" + team1.read(502)+ "\n\n")
position = file.seek(0, 0)  # seek(起始偏移量,表示要从哪个位置开始偏移[0,1,2]) : Reset檔案指標
print("\n" + "Modify : " + file.read() + "\n")
file.close()
team1.close()
############WRITE#####################
file = open("Rap.txt", "a+")  # mode=a+ 可增加又可讀
team1 = open("Kruis Wu team")
team2 = open("Will Pan team")
file.write("\n" + team2.read(1009))
str = "\nMIX String : \n" + team1.read(115) + "\n"+ team2.read(100)
file.write(str)
position = file.seek(0, 0)
print("Append : " + file.read() + "\n")
file.close()
team1.close()
team2.close()
############Return#####################
file = open("Rap.txt", "w+")  # mode = w+ 可寫入又可讀
copy = open("Copy.txt", "r")
file.write(copy.read() + "\n")
file.seek(0, 0)
# print(file.read())
file.close()
copy.close()
