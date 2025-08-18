from math import log
from math import e
from math import sqrt

from sys import argv

########################################

def f_alpha(A,y):
    
    rVal = 0
    
    N = len(alpha)
    
    N_1 = 0
    
    count = 0
    
    for a in A:
        count += a
        
    mean = float(count)/float(N)
    
    for a in A:
        difference = pow(a - mean,2)
        
        rVal += difference
    
    rVal = (float(1)/float(N - 1)) * rVal
    
    rVal = float(y - mean)/sqrt(rVal)
    
    return rVal
    
#######################################

def f_p(A,y):

    rVal = 0
    
    N = len(A)
    
    count = 0
    
    for a in A:
        if a <= y:
            count += 1
            
    rVal = float(count)/float(N)
    
    return rVal
    
#######################################

alpha = eval(argv[1])

N = len(alpha)    
S = 0

alpha_prime = []

i = 0

while i < len(alpha):
    
    alpha_prime.append(f_alpha(alpha,alpha[i]))
    
    alpha_prime[i] = sqrt(pow(alpha_prime[i],2))
    
    if alpha_prime[i] >= 1:
        alpha_prime[i] = 0.9999999999
    
    print(f"Y_{i} = {alpha_prime[i]}")
    
    i += 1

i = 1

while i <= N:
    
    co = float(2*i - 1)/float(N)
    
    i_0 = i - 1
    
    i_1 = N - i
    
    f_0 = f_p(alpha_prime,alpha_prime[i_0])

    if f_0 >= 1:
        f_0 = 0.9999999999
    
    f_1 = f_p(alpha_prime,alpha_prime[i_1])
    
    if f_1 >= 1:
        f_1 = 0.9999999999
    
    sum = log(f_0,e) + log(1 - f_1,e)
    
    S += co * sum
    
    i += 1
    

A_sqr = float(-N - S)/float(N)

print(f"A^2 = {A_sqr}")
