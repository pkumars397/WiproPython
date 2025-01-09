# Dictionary ,it can be modified,key value pair 

staff= {"Name " : "doss",
        "Age  " :  45,
        "Salary":  50000
        }

for i in staff:
   print(i)
for i in staff.values():
   print(i)
for i in staff.items():
   print(i)

print("\n")
print(staff)


# its values can be modified ,not keys ,or we can add new key-val

staff["salary"]=50000
print(staff)
