def func(a):
    if a == 1:
        return 1;
    else:
        return a * func(a - 1)


i = input("Enter a Number : ")
ans = func(int(i))
print(ans)
