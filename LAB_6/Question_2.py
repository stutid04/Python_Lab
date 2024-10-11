def display_list(lst):
    print("The list is:", lst)
user_input = list(map(int, input("Enter numbers separated by space: ").split()))
display_list(user_input)
