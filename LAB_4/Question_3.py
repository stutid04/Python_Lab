for num in range(1, 1001):
    sum_armstrong = 0
    length = len(str(num))
    for digit in str(num):
        sum_armstrong += int(digit) ** length
    if sum_armstrong == num:
        print(num)
