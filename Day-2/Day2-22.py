def findamt(amt , gst=.15):
    return amt+amt*gst

print(findamt(1500))
print(findamt(2000, 0.1))