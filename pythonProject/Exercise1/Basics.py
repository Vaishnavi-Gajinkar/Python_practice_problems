#code to enter patient details like name,age etc.
fname = "John"
lname = "smith"
age = str(20)
print("Patient name is "+fname+lname)
print("Patient age is " + age )

#code to calculate sum of numbers
num1 = input("enter 1st number")
num2 = input("enter 2nd number")
sum = int(num1) + int(num2)
print(sum)

#code to convert weight from Kg to Lbs and vice versa
weight = float(input("enter weight: "))
unit = input("type K or L depending on whether unit of weight is Kg or LBS: ")
if unit == "K" or "k":
    print("Weight in LBS is " + str(weight * 0.4535))#convert to lbs
elif unit == "L" or "l":
    print("Weight in Kgs is " + str(weight * 2.204))#convert to kgs
else:
    print("invalid input ")