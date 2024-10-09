import sys
if len(sys.argv) < 3:
    print("Please provide at least two numbers.")
    sys.exit(1)
numbers = [float(arg) for arg in sys.argv[1:]]
total_sum = sum(numbers)
print("The sum is:", total_sum)