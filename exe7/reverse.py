myNumList = [1,2,3,4,5,6,7,8,9,10]
myAlfList = []

def alfabetoReverse(la):
    tempList=[]
    myAlfList.extend("abcdefghilmnopqrstuvz")
    for i in range( len(myAlfList)-1,-1,-1):
        tempList.append(myAlfList[i])
    for i in range(0,len(tempList)):
        myAlfList[i]=tempList[i]


def algReverse1(ln):
    tempList = []
    for i in range(len(myNumList)-1,-1,-1):
        tempList.append(myNumList[i])
    for j in range(0,len(tempList)):
        myNumList[j]=tempList[j]
    return myNumList

algReverse1(myNumList)