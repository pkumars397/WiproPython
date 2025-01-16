def leapYear(startYear):
  listOfnext15LeapYears=[]
    
  while True:
    if startYear%4!=0: startYear+=1
    if startYear%4==0 and startYear%100!=0:
          listOfnext15LeapYears.append(startYear)
          startYear+=4
    else:
        if startYear%400==0:
            listOfnext15LeapYears.append(startYear)
            startYear+=4
        else:
            startYear+=1
    if len(listOfnext15LeapYears)==15: break
  return listOfnext15LeapYears

staryear=int(input("enter year from where u want to generate 15 leap years: "))
print(leapYear(staryear)) #will print all leap years starting from entered year