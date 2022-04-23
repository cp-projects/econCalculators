import random

class Bet:

    def __init__(self, probWin, winningsProfitPerDollarBet, Ao):
        self.p = probWin
        self.b = winningsProfitPerDollarBet
        self.Ao = Ao

    def updateBet(self, newProbWin, newWinningsProfitPerDollarBet, Ao):
        self.p = newProbWin
        self.b = newWinningsProfitPerDollarBet
        self.Ao = Ao


    def kelly(self):

        p = self.p
        b = self.b

        return (p*b - (1-p))/b

    def ev(self):

        p = self.p
        b = self.b

        return (p*b - (1-p)*(1))


    def k(self):

        ev = self.ev()
        kelly = self.kelly()
        Ao = self.Ao

        thisBet = Ao*kelly
        betEv = thisBet*ev
        
        print("kelly = {:f}".format(thisBet))
        print("EV = {:f}".format(betEv))


class randBernuli(Bet):

    def hello(self):
        print("helloWorld")

    #doesn't work, underestimating to almost always 0
    def rand6Point25(self):
        rand = self.rand12Point5() & self.rand12Point5()
        return rand


    def rand12Point5(self):
        rand = self.rand2575() & self.rand2575()
        return rand


    def rand2575(self):
        rand = self.rand5050() & self.rand5050()
        return rand


    def rand5050(self):
        rand = random.randint(0,100000)
        return rand&1

    def rand7525(self):
        rand = self.rand5050() | self.rand5050()
        return rand


class monteCarlo(randBernuli):

    def test(self):

        print("test")

        

        

        
