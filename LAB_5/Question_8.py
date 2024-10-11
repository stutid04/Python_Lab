lst = list(map(int, input("Enter list of integers: ").split()))
tpl = tuple(map(int, input("Enter tuple of integers: ").split()))
result = list(map(str, lst + list(tpl)))
print(result)
