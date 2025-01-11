marks=[12,34,50,60,40]
#create plist marks>=50 and faillist Marks<50
plist=[e for e in marks if e>=50]
flist=[e for e in marks if e<50]
print(f"PassList: {plist}, faillist {flist}")