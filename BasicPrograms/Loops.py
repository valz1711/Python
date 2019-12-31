import re
if(__name__ == "__main__"):
    a = 5
    listVariable = ["Apple","Samsung","Nokia"]
    for x in listVariable:
        print("iterating through listVariable:",x)
        if(x=="Apple"):
            print("Apple products are good and reliable")
        elif(x=="Samsung"):
            print("Premium products of samsung are ultimate innovations")
        else:
            print("Budget section of mobile phone industry")

    age = 25
    txt = "My name is Valan, I am " + str(age)
    a = txt.count("a")
    print(txt)
    print("Count of a",a)

    string = "Valan1711&"
    print(string.isalnum())

    zfillEG = "70"
    print("Zfill")
    fill = zfillEG.zfill(60)
    print("fill ",fill)

    s = 'as32{ vd"s k!+'
    print(re.sub('[^a-zA-Z]+', '', s))


    for x in range(5):
        print(x)