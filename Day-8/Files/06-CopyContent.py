# Copy the content of one file to another.

def copyContent(file1,file2):
    with open(file1,"r") as f1:
      with open(file2,"a") as f2:
          f2.write(f1.read())
          
    #with open(file1)as src,open(file2,"a") as dest:
        #dest.write(src.read())          
copyContent("txt1.text","txt2.txt")