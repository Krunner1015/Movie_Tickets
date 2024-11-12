timeChoice = 0
adultTC = 0
childTC = 0
numAdultT = 0
numChildT = 0
totalC = 0

print("Available movies today:")
print("A)12 Strong:	1)2:30	2)4:40	3)7:50	4)10:50")
print("B)Coco: ","1)12:40","2)3:45", sep = '\t')
print("C)The Post:   ","1)12:45","2)3:35","3)7:05","4)9:55", sep = '\t')
movieChoice = input("Movie choice:   ")

if movieChoice == "A" :
    timeChoice = int(input("Showtime:       "))
    if timeChoice >= 1 and timeChoice <= 4:
        adultTC = 12.45
        childTC = 9.68
        numAdultT = int(input("Adult tickets:  "))
        numChildT = int(input("Kid tickets:    "))
        if 0<= numAdultT + numChildT <= 30:
            totalC = (numAdultT * adultTC) + (numChildT * childTC)
            type('{0:.2f}'.format(totalC))
            print("Total cost:", ("%.2f" % totalC), sep="     $")
        else:
            print("Invalid option; please restart app...")
    else:
        print("Invalid option; please restart app...")
elif movieChoice == "B" :
    timeChoice = int(input("Showtime:       "))
    if timeChoice == 1 :
        adultTC = 11.27
        childTC = 8.00
        numAdultT = int(input("Adult tickets:  "))
        numChildT = int(input("Kid tickets:    "))
        if 0<= numAdultT + numChildT <= 30:
            totalC = (numAdultT * adultTC) + (numChildT * childTC)
            type('{0:.2f}'.format(totalC))
            print("Total cost:", ("%.2f" % totalC), sep="     $")
        else:
            print("Invalid option; please restart app...")
    elif timeChoice == 2 :
        adultTC = 12.45
        childTC = 9.68
        numAdultT = int(input("Adult tickets:  "))
        numChildT = int(input("Kid tickets:    "))
        if 0<= numAdultT + numChildT <= 30:
            totalC = (numAdultT * adultTC) + (numChildT * childTC)
            type('{0:.2f}'.format(totalC))
            print("Total cost:", ("%.2f" % totalC), sep="     $")
        else:
            print("Invalid option; please restart app...")
    else:
        print("Invalid option; please restart app...")
elif movieChoice == "C" :
    timeChoice = int(input("Showtime:       "))
    if timeChoice == 1 :
        adultTC = 11.27
        childTC = 8.00
        numAdultT = int(input("Adult tickets:  "))
        numChildT = int(input("Kid tickets:    "))
        if 0<= numAdultT + numChildT <= 30:
            totalC = (numAdultT * adultTC) + (numChildT * childTC)
            type('{0:.2f}'.format(totalC))
            print("Total cost:", ("%.2f" % totalC), sep="     $")
        else:
            print("Invalid option; please restart app...")
    elif timeChoice >= 2 and timeChoice <= 4 :
        adultTC = 12.45
        childTC = 9.68
        numAdultT = int(input("Adult tickets:  "))
        numChildT = int(input("Kid tickets:    "))
        if 0<= numAdultT + numChildT <= 30:
            totalC = (numAdultT * adultTC) + (numChildT * childTC)
            type('{0:.2f}'.format(totalC))
            print("Total cost:", ("%.2f" % totalC), sep="     $")
        else:
            print("Invalid option; please restart app...")
    else:
        print("Invalid option; please restart app...")
else:
    print("Invalid option; please restart app...")