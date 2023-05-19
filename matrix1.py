import sys

power = int(sys.argv[1])
power_i = 1

gotoEnd = 0

a = input("m1: ")
b = input("m2: ")


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

		print "matrix power", power_i + 1
	

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
		
			print x[c]
		
			r = 0
	
			rl1 = 0
	
			r0 += 1
	
			
			c += 1

		
		print ""
		
		i = 0
		
		while i < len(x):
			a[i] = x[i]
			
			i += 1
		
		x = []
		
		power_i += 1	
	
	


else:
	print "syntax error"
