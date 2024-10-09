x = float(input("Enter the base (X): "))
n = int(input("Enter the exponent (n): "))
result = 1
for i in range(abs(n)):
    result *= x
if n < 0:
    result = 1 / result
print("X^n =", result)
