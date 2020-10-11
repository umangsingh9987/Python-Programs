num = int(input("Enter a number: "))

# # initialize sum
# sum = 0

# # find the sum of the cube of each digit
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10

# # display the result
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")


# one-liner armstrong check
is_armstrong = lambda num: sum([int(i)**3 for i in str(num)]) == num

# some detailed code
def isArmstrong(num):
    digits = tuple(str(num))               # create a tuple of digits
    digit_cube = []                        # create a list to store cube of digits
    for digit in digits:                   # loop over every digit
        digit_cube.append(int(digit)**3)   # add the cube of each digit to the cube list
    sum_of_cubes = sum(digit_cube)         # calculate the sum of cubes
    if sum_of_cubes == num:                # check if sum is equal to the original number
        return True                         
    else:                                  
        return False                       

# driver code
if is_armstrong(num) and isArmstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
