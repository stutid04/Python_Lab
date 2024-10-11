n = int(input("Enter the value of N: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i - 1] + fib[i - 2])
result = list(map(lambda x: x ** 2, fib[:n]))
print(result)
