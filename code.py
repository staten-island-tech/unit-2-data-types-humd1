bill = (input("enter your bill value"))

service_quality: (input("How was your service? Bad, Good, Okay, or Great?"))

if service_quality == "Good":
    print("Give a 20% tip?")
    print (bill * 1.2)
elif service_quality == "Bad":
    print("No tip?")
elif service_quality == "Okay":
    print("Give a 15% tip?")
elif service_quality == "Great":
    print("Give a 25% tip?")
else: 
    print("invalid input")

bill()