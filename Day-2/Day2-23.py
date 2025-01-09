def find_bonus_hra(salary):
     bon = salary*0.5
     hr=salary*0.25
     return bon,hr


x=int(input("Enter your salary"))
bonus,hra=find_bonus_hra(x)
print("Bonus    = " , bonus)
print("Hra      = " , hra)