
def PresentValue(cs, i, n):

    i = i/100
    
    ans = cs/(1 + i)**n

    return ans
    


def FutureValue(pv, i, n):

    i = i/100

    ans = pv * (1+i)**n

    return ans


def YTM(pv,cs):

    ans = (cs-pv)/pv

    ans = ans*100

    return ans


def YTM2(pv, cs):

    ans = cs**0.5/pv**0.5 -1

    ans = ans*100

    return ans


def YTM3(pv, cs):

    ans = cs**0.33/pv**0.33 - 1

    ans = ans*100

    return ans

class Bond:

    def __init__(self, faceValue, couponRate, maturityDate):

        self.faceValue = faceValue
        self.couponRate = couponRate
        self.maturityDate = maturityDate


    def payout(self):

        maturityDate = self.maturityDate
        faceValue = self.faceValue
        couponRate = self.couponRate/100
    

        for i in range(maturityDate-1):
            print(faceValue*couponRate)

        print(faceValue + (faceValue*couponRate))


    def pv(self,marketIntrest):

        maturityDate = self.maturityDate
        faceValue = self.faceValue
        couponRate = self.couponRate/100
        payment = faceValue*couponRate
        ans = PresentValue((faceValue + payment),marketIntrest,maturityDate)
        #print(ans)

        for i in range(maturityDate-1):

            

            #print(payment)

            realPayment = PresentValue(payment,marketIntrest,1)

            #print(realPayment)

            ans += realPayment
            

        print(ans)

        
