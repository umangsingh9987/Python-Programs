# https://www.facebook.com/permalink.php?story_fbid=1007992526384043&id=100015199150187
# Subscribed by Lucas Ivisson
n1 = input("type the 1 side of the square: ")
n2 = input("type the 2 side of the square: ")

if n1 == '' or n2 == '':
    n1 = 0
    n2 = 0
    
n1 = float(n1);
n2 = float(n2);

if n1 <= 0 or n2 <= 0:
    print("To calculate the area of the square you have to enter values greater than 0")
    exit()

area = n1 * n2

print("The are of the square are: ", area, "cm²")
