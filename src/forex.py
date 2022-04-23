
def graph(x,y, func):
    import matplotlib.pyplot as plt
    import numpy as np
    
    
    xAxis = np.array([0,10])    
    yAxis = np.array([0,10])

    plt.plot(xAxis, yAxis)
    plt.show()
    
def close():
    import matplotlib.pyplot as plt
    plt.close(1)

def fxMarket(iH, iF, Ee):
    
    i = 0.1;
    while(iH != FR(iF, Ee, i)):
        i += 0.1
                
    return i
    
def DR(iH):
    return iH
    
def FR(iF, Ee, x):
    return round(iF + (Ee-x)/x, 2)
    
def mewTheG(mA,mB,gA,gB):

    moneyDiff = mA - mB
    outputDiff = gA -gB

    realA = mA - gA
    realB = mB -gB

    print(moneyDiff - outputDiff)
    print(realA - realB)
    
def UIP(E,iF,iH):

    return E*(iF/iH)
    
#def iHuip()    
    
def srPL(M,L,Y):
    return M/(L*Y)
    



def main():
    print("hello world")
    
    
if __name__ == '__main__':
    main()
    close()
    graph()
    fxMarket(x)
    DR(x)
    FR(x)
    mewTheG()
    UIP()
    srPL()
