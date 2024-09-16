
num = int(input("Please enter a positive number!"))

if num <= 0:
    print ("Please enter positive number!")
else:
    print ("counting down!" )


while num >= 1:
    print (num)
    num -= 1
