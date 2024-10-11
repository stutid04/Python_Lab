s = input("Enter a string: ")
uppercase_count = sum(1 for c in s if c.isupper())
lowercase_count = sum(1 for c in s if c.islower())
print(f"Uppercase letters: {uppercase_count}, Lowercase letters: {lowercase_count}")
