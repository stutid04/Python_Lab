data = []
for i in range(20):
    element = float(input(f"Enter element {i + 1}: "))
    data.append(element)
mean = sum(data) / len(data)
data.sort()
if len(data) % 2 == 0:
    median = (data[len(data) // 2 - 1] + data[len(data) // 2]) / 2
else:
    median = data[len(data) // 2]
mode = max(set(data), key=data.count)
sliced_lists = [data[i:i + 4] for i in range(0, len(data), 4)]
even_list = []
odd_list = []
for sublist in sliced_lists:
    for num in sublist:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Even List:", even_list)
print("Odd List:", odd_list)
