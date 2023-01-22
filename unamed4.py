from math import comb

fibList = [1,1]

def fibListFunct(max):
    while True:
        fibListLen = len(fibList)
        nextFib = fibList[fibListLen - 1] + fibList[fibListLen - 2]
        if(nextFib <= max):
            fibList.append(nextFib)
        else:
            break


def fibMatrix(fibNum):
    listMatrix = -1
    for i in range(len(fibList)):
        if fibList[i] == fibNum:
            listMatrix = i
            break
    return listMatrix


def diagonal(i):
    diagonalList = []
    for n in reversed(range(i+1)):
        for r in range(i+1):
            if(n >= r and n+r == i):
                diagonalList.append(comb(n,r))
                
    return " ".join(str(i) for i in diagonalList)

def fibDiagonal(fibNum):
    fibListFunct(fibNum)
    i = fibMatrix(fibNum)
    if (i > -1):
        diagonalList = diagonal(i)
        return diagonalList
    else: 
        return None
    
if __name__ == "__main__":
    fibNum = 8
    print(fibDiagonal(fibNum))