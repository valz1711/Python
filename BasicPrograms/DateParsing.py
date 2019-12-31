import datetime as dt
from datetime import timedelta

if(__name__ == '__main__'):
    print('Current date/time: ',dt.datetime.now())
    a = dt.datetime.now()
    print(a)
    formatDT = '%Y-%m-%d'
    strDT = "2019-12-26"
    parsedDT = dt.datetime.strptime(strDT,formatDT)
    print("parsed date ::",parsedDT.strftime(formatDT))

    holidays = ["2019-12-25","2019-12-28","2019-12-31","2019-12-22","2019-12-30"]
    holidaysDT = []
    for x in holidays:
        r = dt.datetime.strptime(x,formatDT)
        holidaysDT.append(r)

    for x in holidaysDT:
        print(x.strftime(formatDT))


    workingDaysDT = []
    counterVariable = 0
    givenDT = "2019-12-20"
    gvnDateParsed = dt.datetime.strptime(givenDT,formatDT)
    numOfBizDays = 10
    while(counterVariable<numOfBizDays):
        if(gvnDateParsed in holidaysDT):
            gvnDateParsed = gvnDateParsed+timedelta(days=1)
            continue
        else:
            counterVariable+=1
            workingDaysDT.append(gvnDateParsed)
            gvnDateParsed = gvnDateParsed + timedelta(days=1)

    i = 1
    for _ in workingDaysDT:
        print(i," working day = ",_.strftime(formatDT))
        i = i + 1