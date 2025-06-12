import sys

power = int(sys.argv[1])
power_i = 1

gotoEnd = 0

sierra_1 = input("m1: ")
sierra_2 = input("m2: ")

a = []
b = []

a_n_0 = 0
a_n_1 = 0
a_c = 0
b_n_0 = 0
b_n_1 = 0
b_c = 0

for s in sierra_1:
    if s == '[':
        a_n_0 += 1
    elif s == ']':
        a_n_1 += 1
        
    if s == ',':
        a_c += 1
        
for s in sierra_2:
    if s == '[':
        b_n_0 += 1
    elif s == ']':
        b_n_1 += 1
        
    if s == ',':
        b_c += 1
        
a_n = a_n_0 - a_n_1
b_n = b_n_0 - b_n_1

#(a + b)(a - b)
#a(a - b) + b(a - b)
#a^2 - b^2

if a_n == 0 and b_n == 0 and a_c == (pow(a_n_0,2) - 1) and b_c == (pow(b_n_0,2) - 1):
    i_0 = 0
    i_1 = 0
    i_2 = 0
    
    alpha = ""
    alpha_n = False
    
    for i,s in enumerate(sierra_1):
        if s == '[':
            a.append([])
            i_0 = i
            i_1 = i + 2*a_n_0
            alpha_n = True
            
            if sierra_1[i_1] == ']':
                pass
            else:
                gotoEnd = 1
                print("input a square matrix")
                break
                
        if s == ']':
            a[i_2].append(int(alpha))
            alpha = ""
            alpha_n = False
            i_2 += 1
                
        if alpha_n == True and i > i_0:
            if s != ',':
                alpha += s
            else:
                a[i_2].append(int(alpha))
                alpha = ""
    
    i_0 = 0
    i_1 = 0
    i_2 = 0
    
    bravo = ""
    bravo_n = False
    
    for i,s in enumerate(sierra_2):
        if s == '[':
            b.append([])
            i_0 = i
            i_1 = i + 2*b_n_0
            bravo_n = True
            
            if sierra_2[i_1] == ']':
                pass
            else:
                gotoEnd = 1
                print("input a square matrix")
                break
                
        if s == ']':
            b[i_2].append(int(bravo))
            bravo = ""
            bravo_n = False
            i_2 += 1
                
        if bravo_n == True and i > i_0:
            if s != ',':
                bravo += s
            else:
                b[i_2].append(int(bravo))
                bravo = ""
                
else:
    gotoEnd = 1
        


i = 0

while i < (len(a) - 1):
	if (len(a[i]) != len(a[i+1])) | (len(a[i]) != len(b)):
		gotoEnd = 1
		
	i += 1
	
i = 0


if gotoEnd == 0:

	while power_i < power:

		r = 0

		x = []

		while r < len(a):
			x.append([])
			r += 1
	
		if r == len(a):
			r = 0
	
		rl0 = 0
		r0 = 0
		rl1 = 0
		r1 = 0

		c = 0

		print(f"matrix power, {power_i + 1}")
	

		while c < len(a):

			while r < len(a):
	
				A = 0
		
				while rl0 < len(a[r]):
		
					A += a[r0][rl0]*b[r1][rl1]			
			
					rl0 += 1
					r1 += 1
		
				x[c].append(A)
		
				rl0 -= len(a)
				r1 -= len(a)
			
				r += 1
		
				rl1 += 1
		
			print(x[c])
		
			r = 0
	
			rl1 = 0
	
			r0 += 1
	
			
			c += 1

		
		print("")
		
		i = 0
		
		while i < len(x):
			a[i] = x[i]
			
			i += 1
		
		x = []
		
		power_i += 1	
	
	


else:
	print("syntax error")
