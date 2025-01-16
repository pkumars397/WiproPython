def newStr(s):
    if len(s)>=4:
      newS=s[:2]+s[-2:]
      return newS
    else: return ""
    
s1= "w3school"
s2="w3"
s3="w3sc"
print("new string made of ",s1,"is ",newStr(s1));
print("new string made of ",s2,"is ",newStr(s2));
print("new string made of ",s3,"is ",newStr(s3));