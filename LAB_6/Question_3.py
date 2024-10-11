def cube_of_elements(*args):
    cubes = [x**3 for x in args]
    print("Cubes of the elements:", cubes)
user_input = list(map(int, input("Enter numbers separated by space: ").split()))
cube_of_elements(*user_input)
