# https://www.facebook.com/permalink.php?story_fbid=1007992526384043&id=100015199150187
# Subscribed by Lucas Ivisson
number = input("Type a number: ")

if number == "":
    number = 0;
    
number = int(number)

if number % 2 == 0:
    print("This number", number,"is even")
else:
    print("This number", number,"is odd")
