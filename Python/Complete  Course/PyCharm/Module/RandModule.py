import random

food =["sweet cake","StrawBerry cake","Pizza","Fried Chicken"]
print(random.choice(food))  #random.choice(list) : 隨機挑選一個list元素

print(food)
random.shuffle(food)  #random.shuffle(list) : 對list做重新隨機排序
print(food)