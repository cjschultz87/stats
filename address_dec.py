import sys

digits = "0123456789abcdef"

inFile = sys.argv[1]

outFile = sys.argv[3]

try:
    foxtrot = open(inFile,"r")
    foxtrotOut = open(outFile,"w")
except:
    print("invalid file")
    quit()

line_start = sys.argv[2]

try:
    line_start = int(line_start)
except:
    print("line start must be decimal integer")
    quit()
    
i = 0

while i < line_start:
    foxtrot.readline()
    i += 1

sierra = ""

line = ""

while True:
    line = foxtrot.readline()
    
    if "0:000" in line:
        break
    
    delta = 0
    
   i = 0
    accent_count = 0
    
    while True:
        if line[i] == '`':
            i += 1
            accent_count += 1
        elif not(line[i] in digits):
            break
        
        hex = 0
        
        i_0 = 0
        
        while i_0 < 2:
            hex += digits.find(line[i]) * pow(16,1-i_0)
            
            i += 1
            i_0 += 1
        
        delta += hex * pow(256,7-((i - (accent_count + 2))//2))
    
    sierra = str(delta)
    
    foxtrotOut.writelines(f"{sierra}\n")

foxtrot.close()
foxtrotOut.close()
