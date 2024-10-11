bases = list(map(int, input("Enter bases: ").split()))
result = list(map(lambda x, i: x ** i, bases, range(len(bases))))
print(result)
