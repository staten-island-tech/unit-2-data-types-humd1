""" 
bill = float(input("enter your bill value"))
service_quality: (input("How was your service? Bad, Good, Okay, or Great?"))

if service_quality == "Good":
    print("Give a 20% tip?")
    print(bill * 1.2)
elif service_quality == "Bad":
    print("No tip?")
    print(bill)
elif service_quality == "Okay":
    print("Give a 15% tip?")
    print(bill * 1.15)
elif service_quality == "Great":
    print("Give a 25% tip?")
    print(bill * 1.25)
else: 
    print("invalid input")

service_quality(user_input)
bill()

def factors(number):
    for i in range(1,number + 1):
        if number % i == 0:
            print(i)
        
user_input = int(input("Enter a number to find the factors"))
factors(user_input)
 """

def factor(number):
def secondfactor(othernumber):
    for i in range(1,numbers and othernumber + 1):
        if number and othernumber % i ==0
            print(i)

factor = int(input("Enter the first number to find the factors"))
secondfactor = int(input("Enter second number to find the factor"))