# 4. Add two numbers without using the addition or subtraction operator.

#Using Logic Gates
def add(a,b):
    while (b):
        a, b = (a | b), (a ^ b)
    print (a)
add(8, 3)


# 3. Find the factors of an integer down to the limit.

x = int(input("Enter a Number:  "))
        
for i in range(1,x+1): 
	if not x%i: 
	    print(i,end=' ') 
