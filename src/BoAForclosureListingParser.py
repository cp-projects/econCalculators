from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen


"https://foreclosures.bankofamerica.com/search/illinois/chicago"


#test functions to debug parsers

def testPriceParser(url):
    content = urlopen(url).read().decode()
    parser = priceParser()
    parser.feed(content)
    return parser.getPriceItems()

def testAddressParser(url):
    content = urlopen(url).read().decode()
    parser = addressParser()
    parser.feed(content)
    return parser.getAddressItems()


def testDetailsParser(url):
    content = urlopen(url).read().decode()
    parser = detailsParser()
    parser.feed(content)
    return parser.getDetailsItems()






#run parsers to scrape data



#creates symbolTable key(address):val(everything else)

def runForclosureAddressParser(url):
    propertyInfoBasic = {}
    propertyInfoComplex = {}
        
    content = urlopen(url).read().decode()
    parser = priceParser()
    parser.feed(content)
    prices = parser.getPriceItems()

    parser = addressParser()
    parser.feed(content)
    addresses = parser.getAddressItems()

    parser = detailsParser()
    parser.feed(content)
    details = parser.getDetailsItems()

    
    
    counter = 0
    for price in prices:
        propertyInfoBasic[price] = addresses[counter]
        counter += 1
            
    #i = 0
    for info in propertyInfoBasic:
        propertyInfoComplex[propertyInfoBasic[info]] = info + " " + str(details)
        #str(info) + " " + details[i] + " " + details[i+1] + " " + details[i + 2] + " " + details[i+3]
        #i += 1

    
    return propertyInfoComplex




#creates symbolTable key(price):val(everything else)

def runForclosurePriceParser(url):
    propertyInfoBasic = {}
    propertyInfoComplex = {}
    

        
    content = urlopen(url).read().decode()
    parser = priceParser()
    parser.feed(content)
    prices = parser.getPriceItems()

    parser = addressParser()
    parser.feed(content)
    addresses = parser.getAddressItems()

    parser = detailsParser()
    parser.feed(content)
    details = parser.getDetailsItems()

    
    
    counter = 0
    for address in addresses:
        propertyInfoBasic[address] = prices[counter]
        counter += 1
            
    
    for info in propertyInfoBasic:
        propertyInfoComplex[propertyInfoBasic[info]] = info + " " + str(details)
        

    
    return propertyInfoComplex




#returns symboltable of price:address

def runForclosurePriceParserBasic(url):
    propertyInfoBasic = {}
    propertyInfoComplex = {}
    

        
    content = urlopen(url).read().decode()
    parser = priceParser()
    parser.feed(content)
    prices = parser.getPriceItems()

    parser = addressParser()
    parser.feed(content)
    addresses = parser.getAddressItems()

    parser = detailsParser()
    parser.feed(content)
    details = parser.getDetailsItems()

    
    
    counter = 0
    for price in prices:
        propertyInfoBasic[price] = addresses[counter]
        counter += 1
            
    
    return propertyInfoBasic



#returns symboltable of address:price

def runForclosureAddressParserBasic(url):
    propertyInfoBasic = {}
    propertyInfoComplex = {}
    

        
    content = urlopen(url).read().decode()
    parser = priceParser()
    parser.feed(content)
    prices = parser.getPriceItems()

    parser = addressParser()
    parser.feed(content)
    addresses = parser.getAddressItems()

    parser = detailsParser()
    parser.feed(content)
    details = parser.getDetailsItems()

    
    
    counter = 0
    for address in addresses:
        propertyInfoBasic[address] = prices[counter]
        counter += 1
            
    
    return propertyInfoBasic


#returns symboltable address:details


def runForclosureDetailsParserBasic(url):
    propertyInfoBasic = {}
    propertyInfoComplex = {}
    

        
    content = urlopen(url).read().decode()
    parser = priceParser()
    parser.feed(content)
    prices = parser.getPriceItems()

    parser = addressParser()
    parser.feed(content)
    addresses = parser.getAddressItems()

    parser = detailsParser()
    parser.feed(content)
    details = parser.getDetailsItems()

    
    
    counter = 0
    
    for address in addresses:

        propertyInfoBasic[address] = details
        counter += 1
            
    
    return propertyInfoBasic



#parsers used in other functions


class priceParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        #self.propertyInfo = {}
        self.items = []
        self.listTag = False
        
        
    def handle_starttag(self, tag, attrs):
        if ('class','rec-result-price') in attrs:
            self.listTag = True
            #self.propertyInfo[price:data]
    def handle_endtag(self, tag):
        if tag == 'div':
            self.listTag = False
            
    def handle_data(self, data):
        if self.listTag == True:
            self.items.append(data)
            #self.propertyInfo[(str)"price":data]
        
    def getPriceItems(self):
        return self.items



class addressParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.items = []
        self.listTag = False
        
        
    def handle_starttag(self, tag, attrs):
        if ('class','rec-result-address') in attrs:
            self.listTag = True
            
    def handle_endtag(self, tag):
        if tag == 'div':
            self.listTag = False
            
    def handle_data(self, data):
        if self.listTag == True:
            self.items.append(data)

        
    def getAddressItems(self):
        return self.items



#beds baths and square footage

class detailsParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.items = []
        self.listTag = False
        
        
    def handle_starttag(self, tag, attrs):
        if ('class','rec-result-details') in attrs:
            self.listTag = True
            
    def handle_endtag(self, tag):
        if tag == 'div':
            self.listTag = False
            
    def handle_data(self, data):
        if self.listTag == True:
            self.items.append(data)

        
    def getDetailsItems(self):
        return self.items

