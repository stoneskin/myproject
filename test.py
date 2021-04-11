import os
path = os.getcwd()
print(path)


#import pickle
from pickle import dump,load
list=[1,2,3,4,5]
myFile=open("testData.txt","wb")
dump(list,myFile)
print("list dumpped")
myFile=open("testData.txt","rb")
list2= load(myFile)
print(list2)

print("test github")
