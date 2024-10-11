a, b = map(int, input("Enter two numbers separated by space: ").split())
while b:
    a, b = b, a % b
print("GCD is:", a)
