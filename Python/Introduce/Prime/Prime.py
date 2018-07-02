#Prime number generator
for i in range(2,100):
    j=2                         #假想除數
    isPrime = True                 #非質數flag
    while j < i:
        if i % j==0: isPrime = False #可被假想除數整除, 設定非質數flag
        j+=1   #假想除數+=1
        
    if isPrime==True:
            print(str(i)+" is a prime number")
    else:
            isPrime=True             #重置質數flag



