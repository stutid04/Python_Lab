n=4
for i in range(n):
    start_char="A" if i%2==0 else "B"
    for j in range(2*i+1):
        print(start_char,end=" ")
        start_char="B" if start_char=="A" else "A"
    print()