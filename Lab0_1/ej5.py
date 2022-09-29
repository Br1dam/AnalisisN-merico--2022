def factorial(n):
    factorial = 1
    res = 1
    if (n == 0) :
        res = 1
    else:
    	for i in range(1,n+1):
    		factorial = factorial * i
    		res = factorial
    return res
    		
    		
    		
 
    
    
r = factorial(3)
print(r)
