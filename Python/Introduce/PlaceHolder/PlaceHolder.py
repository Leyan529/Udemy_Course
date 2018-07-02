# PlaceHolder
same = "Hello %s, you are the girl for the best "
arr=["Abby","Baby","Yabb"]
for i in arr:
    print(same%(i))

# PlaceHolder + dict
diffWithYear = "Hello %s, you are the girl for the best , yor age is %d ."
dict={21:"Abby",22:"Baby",23:"Yabb"}
for i in dict:
    print(diffWithYear%(dict[i],i))
