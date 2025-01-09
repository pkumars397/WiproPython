cel=[34,36,45]
fahList=map(lambda x:x*1.8+32,cel)
#for I in cel:
#    I=1.8*I+32
#    fahList.append(I)

fahAbove100=filter(lambda x:x>100,fahList)
print(list(fahAbove100))