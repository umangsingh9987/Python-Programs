#https://www.facebook.com/anmol.raj.reaperofsoul/posts/1038110763304900
#Subscribed by Itachi Uchiha
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1,",",end="")
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
