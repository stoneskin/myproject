from mcpi_e.minecraft import Minecraft
from mcpi_e import block

import pickle

serverAddress="192.168.1.155" # change to your minecraft server
playerName ="stoneskin2020"
pythonApiPort=4711

mc=Minecraft.create(serverAddress,pythonApiPort,playerName) 

#this function make sure the smaller number as value1
def sortPair(v1,v2):
    if v1>v2:
        return v2,v1
    else:
        return v1,v2

# this function will get the value of blockId in the input location and save as 3d list
def copyStructure(x1,y1,z1,x2,y2,z2):
    x1,x2 = sortPair(x1,x2)
    y1,y2 = sortPair(y1,y2)
    z1,z2 = sortPair(z1,z2)

    structure=[]
    print ("starting build the data structure...")
    for x in range(x1,x2):
        listX=[]
        structure.append(listX)
        for y in range(y1,y2):
            listY=[]
            listX.append(listY)
            for z in range(z1,z2):
                #print("x:{},y:{},z:{}".format(x,y,z))
                blockId=mc.getBlock(x,y,z)
                listY.append(blockId)
            print(listY)
    return structure

print("This python code will save the minecraft structure to the file")
input("Move to the first position, and press Enter:")
(x1,y1,z1)=pos1=mc.player.getTilePos()
input("Move to the second position, and press Enter:")
(x2,y2,z2)=pos2=mc.player.getTilePos()

data=copyStructure(x1,y1,z1,x2,y2,z2)
print(data)
filename=input("Please give a file name you want to save:")
if(filename==""):
    filename="test_tata"
filename=filename+".txt"
print("will save as "+filename)


#theFile=open(filename,"wb")
#pickle.dump(data,theFile)
with open(filename, "wb") as f:
    pickle.dump(data, f)
