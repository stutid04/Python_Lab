lst = list(map(int, input("Enter numbers for the list: ").split()))
n=int(input("enter the element to be appened in the list"))
print("Original list:", lst)

lst.append(n)
print("After appending 10:", lst)

lst.sort()
print("Sorted list:", lst)

lst.reverse()
print("Reversed list:", lst)

lst.remove(lst[0])
print("After removing the first element:", lst)

print("Count of 10:", lst.count(10))
