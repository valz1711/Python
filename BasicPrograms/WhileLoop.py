if(__name__ == '__main__'):
    print("While loop concept")
    i = 1
    while (i<=10):
        print(i)
        i+=1
    print("exit loop")

    i = 1
    while(i<=5):
        if(i==3):
            i = i+2
            continue
        else:
            print(i)

        i = i+1
    print("Exit second loop")

    string1 = "Data#Science#is#the#study#and#exploring#of#data"
    string1 = string1.replace("#"," ")
    print(string1)
    splitString = string1.split(" ")
    print(type(splitString))
    j = 0#len(splitString)
    print(j)
    while(j<len(splitString)):
        print(j+1," element in list is ",splitString[j])
        j= j+1

    lastElement = splitString[-1]
    print(lastElement)