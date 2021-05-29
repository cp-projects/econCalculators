def MoneySupplyChange(dMoneyBase,ReserveRate):

    ReserveRate = ReserveRate/100
    
    return (1/ReserveRate)*dMoneyBase


def inflationCalculator(MoneySupplyOrigional,MoneySupplyNew,Velocity,PriceLevel,rGDP):

    dMoneySupply = MoneySupplyNew - MoneySupplyOrigional

    dp = (dMoneySupply*Velocity)/rGDP

    return dp
