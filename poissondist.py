import sys

euler = 2.71828182845904523536028747135266249775724709369995

def factorial(x):
    index = 1
    
    xray = 1
    
    while index <= x:
        xray *= 1+(index-1)
        index += 1
        
    return xray

def am(array):
    xray = 0
    
    for entry in array:
        xray += int(entry)
        
    return float(xray)/float(len(array))

def pd(avg_delta,x):
    return pow(euler,0-avg_delta)*pow(avg_delta,x)/factorial(x)

if len(sys.argv) < 4:
    try:
        x = int(sys.argv[2])
    except:
        quit()

    try:
        path = sys.argv[1]
    except:
        print "path does not exist"
        quit()
    
    foxtrot = open(path,"r")
    
    delta = []
    
    for lima in foxtrot:
        delta.append(lima)
        
    avg_delta = am(delta)
    
    print "p(x;lambda) = " + str(pd(avg_delta,x))
    print "p(x) = " + str(avg_delta/len(delta))
    
    


else:
    print "poissondist takes two additional args (file path of the data and x)"