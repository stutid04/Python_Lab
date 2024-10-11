tpl = tuple(map(int, input("Enter tuple of integers: ").split()))
index_lst = list(map(int, input("Enter indices separated by space: ").split()))
result = list(map(lambda i: tpl[i], index_lst))
print(result)
