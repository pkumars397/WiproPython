# Read values from the console [ values are integer ]. add these values to the variable total.
# if you want to stop entering values , give zero to come out from the  loop
# print total

total=0
while True:
   num=int(input("enter:"))
   if num:
     total+=num
     continue
   else:
     break
print(total)