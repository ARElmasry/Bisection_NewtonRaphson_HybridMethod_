# A combined  Newton-Raphson method with bisection method
# to find a root of f(x) = 0 
import sys                                
from numpy import sign    
    
   
	
def NewtonRaphson (f, df, tol=1.0e-09):
	
	while True:
		a = float(input("Enter First Arbitrary value of x: "))
		b = float(input("Enter Second Arbitrary value of x: "))
	                                                            
		fa = f(a)                                  
		if fa == 0.0: return 0,a  
		fb = f(b)
		if fb == 0.0: return 0,b	    
		if sign (fa) == sign (fb): 
			print('Root is not within the provided x-range ') 
			ans=input("Press 1 to Re-enter Arbitrary values of x or press 2 to exit: ") 
			if ans == '1': continue 
			elif ans =='2': sys.exit()            
		else:
			break
				
	x = 0.5*(a+b)
	for i in range(0, 1000):
		fx = f(x)
		if fx == 0.0:   return i+1, x 
	# Tighten the range on the root
		if sign (fa) != sign (fx): b = x
		else: a = x
	
	# Newton-Raphson step
		dfx = df(f,x)
	# If division by zero, push x out of bounds
		try: dx= -fx/dfx ; print('NewtonRaphson step')
		except ZeroDivisionError: dx = b - a ; print('ZeroDivision')
		x = x + dx 													 
	# If the result is outside the range, use bisection
		if (b - x)*(x - a) < 0.0:         
			dx = 0.5*(b - a)                   ; print('Bisection step') 
			x = a + dx
	# Check for convergence
		if abs(dx) < tol*max(abs(b),1.0):  return i+1, x  
			
	return i+1,"No Answer: Number of iterations Exceeded "

def df (f, x, eps=1.0e-05):
	return (f(x+eps)-f(x))/eps	




def f(x):
	
##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################
#************************Enter your function here*****************************	
# Example Function:
	 return x**2 - 2.0
##############################################################################
##############################################################################
##############################################################################
##############################################################################	
############################################################################## 
	
	
def main():	
	
	i, x = NewtonRaphson (f, df)
	
	print(f"\n After {i} iterations ", "\n", f"The answer is {x} \n\n")
	
	with open("Results.txt",'a') as outFile:
		outFile.writelines([f"\n After {i} iterations ","\n", f" The answer is {x} \n\n"])
	
if __name__=='__main__':
	main()
