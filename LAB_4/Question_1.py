num = input("Enter a number: ")
length = len(num)
sum_disarium = 0
for i in range(length):
    sum_disarium += int(num[i]) ** (i + 1)
if sum_disarium == int(num):
    print(num, "is a Disarium Number.")
else:
    print(num, "is not a Disarium Number.")
