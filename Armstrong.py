number = int(input("Enter any number: "))
temp = number
sum = 0
while temp>0: 
    digit = temp % 10 
    sum += digit ** 3 
    temp = temp // 10
if sum == number:
    print("Your number is an armstrong number")
else:
    print("Your number is not an armstrong number")
    