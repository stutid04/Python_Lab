n=4
for i in range(n):
    start_num=1 if i%2==0 else 0
    for j in range(2*i+1):
        print(start_num,end=" ")
        start_num=1 if start_num==0 else 0
    print()