x = int(input("Enter the first number to find the factors"))
y = int(input("Enter the second number to find the factors"))

gcf = 1

for i in range(1, min(x, y) + 1):
    if x % i == 0 and y % i == 0:
        gcf = i
    
print("gcf is", gcf)
