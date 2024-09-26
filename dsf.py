def factors(number):
    for i in range(1,number + 1):
        if number % i == 0:
            print(i)
        
user_input = int(input("Enter a number to find the factors"))
factors(user_input)