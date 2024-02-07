try :
    age = int(input("Enter Age: "))
    print(f'You entered {age}')
    salary = float(input("Enter Salary: "))
    risk = salary/age
    print(f'You can take {risk} units of risk at this age')
except ValueError:                              # to handle input error
    print("Please enter a numeric value")
except ZeroDivisionError:                       # to handle if salary is divided by 0
    print('Age cannot be zero!')

# Use Comments to describe Whys? and Hows? Not Whats?(what the code does)
# Use comments to state any assumptions made or Notes for other readers