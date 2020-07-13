
def genPrimes():
    yield 2
    
    listPrimes = [2]
    
    x = 3  
    while True:
        ctr = 0
        for i in listPrimes:
            ctr += 1
            if x%i == 0:
                break
            elif ctr == len(listPrimes): 
                yield x
                listPrimes.append(x)
        
        x += 1
        
        

l = genPrimes()
l.__next__()