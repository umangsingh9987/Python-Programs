# https://www.facebook.com/permalink.php?story_fbid=1007992526384043&id=100015199150187
# Subscribed by Lucas Ivisson
n1 = input("type the base of the triangle: ")
n2 = input("type the height of the triangle: ")


if n1 == '' or n2 == '':
    n1 = 0
    n2 = 0

n1 = float(n1);
n2 = float(n2);

if n1 <= 0 or n2 <= 0:
    print("To calculate the volume of the triangle you have to enter values greater than 0")
    exit()

areaBase = n1 * n1;
volumeTriangle = (areaBase * n2)/3

print("The volume of the triangle are: ", volumeTriangle, "cm³")
