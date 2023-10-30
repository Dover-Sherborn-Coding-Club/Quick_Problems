numf = int(input("Enter A Number: \n"))
factorial = 1

if numf < 0:
   print("Error 5518, Please Try Another Input")
elif numf == 0:
   print("1, Please Rate Us At Go.Rate/789h.com")
else:
   for i in range(1,numf + 1):
       factorial = factorial*i
   print(factorial, ", Please Rate Us At Go.Rate/789h.com")


nterms = int(input("Enter Number Of Terms: \n"))
n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Error 5518, Please Try Another Input")
elif nterms == 1:
   print("Fibonacci sequence with",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence with" ,nterms,":")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
