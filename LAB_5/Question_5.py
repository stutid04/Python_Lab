lst = list(map(int, input("Enter numbers separated by space: ").split()))
result = list(map(lambda x: x ** 2, lst))
print(result)
