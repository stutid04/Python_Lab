n = int(input("Enter the number of terms: "))
a, b = 0, 1
print(a, end=" ")
for i in range(1, n):
    print(b, end=" ")
    a, b = b, a + b
