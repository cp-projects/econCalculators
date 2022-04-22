import sys

sys.path.append("/home/hello/Documents/econCalculators")


import forex

print(forex.UIP(0.93,0.02,0.04))


import BoAForclosureListingParser as BoA

print(BoA.runForclosurePriceParser("https://foreclosures.bankofamerica.com/search/ohio"))


import timeValueOfMoney

print(timeValueOfMoney.PresentValue(100, 2, 5))

