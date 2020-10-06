# https://www.facebook.com/vishal1427/posts/2644630989087681
# Subscribed by vishal
def Fibonacci(n):
    if n<=0:
        print("Incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
print(Fibonacci(9))
