print(abs(-23))  # abs

print(bool("regvrfegrf"))  # bool() : 物件內容判斷指令
print(bool(0))
print(bool([]))

# print(dir([]))  #dir() : 列出相關物件所有方法
array = []
help(array.count)  # help() : 物件方法說明指令

print(dir(""))
help("".upper)

eval("print('hello')") #具有可執行運算式的字串 => 用法eval("運算式")
print(eval('  0xff * 0x5c'))

print (float("12")) #str -> float

print (str(50.456))   #double -> int

testStr = "This is a test string"
print(len(testStr))


testArray=[1,2,6,4,8]  #len() : 長度函數
print(len(testArray))

# for i in range(0,len(testArray)):
#     print(testArray[i])

charArray = ["A","b","b","y","w","h","e","re you"]

# charArray = ["1","2","3"]

print(max(charArray))  #max() => 值取陣列中最大值
print(min(charArray))   #min() => 值取陣列中最小值
# print(sum(charArray))   #sum()=> 陣列中所有元素總和

print(list(range(0,6)))  #list()=> 生成可變串列
print(list("trhbtrhb"))  #list()=> 生成可變串列




