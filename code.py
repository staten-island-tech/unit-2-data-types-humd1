bill = float(input("enter your bill value"))
service_quality = (input("How was your service? Bad, Good, Okay, or Great?"))

if service_quality == "Good":
    print("Give a 20% tip?")
    print(float(bill * 0.2))
elif service_quality == "Bad":
    print("No tip?")
    print(float(bill))
elif service_quality == "Okay":
    print("Give a 15% tip?")
    print(float(bill * 0.15))
elif service_quality == "Great":
    print("Give a 25% tip?")
    print(float(bill * 0.25))
else: 
    print("invalid input")
