sequence = input("Enter a sequence: ")
unique_chars = set(sequence)
result = list(map(lambda x: (x.upper(), x.lower()), unique_chars))
print(result)
