try :
    x=5
    x.append(7) 
    print(x)
except AttributeError:
    print("append() does not exist ")