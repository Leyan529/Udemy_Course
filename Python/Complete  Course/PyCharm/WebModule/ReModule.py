string = "My flow so fresh My swag so fresh "
print(string[0:16])
print(string[17:])

import re

print(dir(re))
print("\n")

string = "把他們圈死 老子饒舌天子 面對偏執 開闢新的大陸"
result = re.search("饒舌天子", string)  # search("欲搜尋字串",搜尋目的地)
print(result)
print("\n")

start = result.start()
end = result.end()
print(string[start:end])
end = result.start() + 7
print(string[start:end])

string2 = "這裡是夢想的中心 但夢想都遙不可及\n這裡是圓夢的聖地 但卻總是撲朔迷離\n多少人敵不過殘酷的現實 從此銷聲匿跡\n多少人陷入了昏迷 剩下一具 空殼屍體"
position = re.search("多少人",string2)
print(string2[position.start():position.end()])
