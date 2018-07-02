
def moonWeight(currentWeight,gain):
    try:
        for i in range(0,10):
            Weightmoon = currentWeight/6
            s = "For %d Year , Moon weight = %d Kg"
            print(s%(i,Weightmoon))
            currentWeight +=gain
    except:
        print("An error occur")


moonWeight(int(input("Enter weight : \n")),int(input("Enter gain : \n")))
