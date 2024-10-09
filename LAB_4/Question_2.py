num = input("Enter a number: ")
sum_digits = 0
for digit in num:
    sum_digits += int(digit)
if int(num) % sum_digits == 0:
    print(num, "is a Harshad Number.")
else:
    print(num, "is not a Harshad Number.")
