def greeting(fname, lname):
    print(f'Hello {fname} {lname} !')
    print("Welcome Aboard")
    return f'Greetings End'

def score(percentage,grade,credit):
    print(f'You secured {percentage}% which accounts to {credit} credits and have a {grade} grade')
    print(f'Percentage squared is {percentage*percentage}')
    return                                     # By default all functions return None

print("Start")
print(greeting('Vaishnavi', "Gajinkar"))
print(score(85,credit=7.07,grade='A'))          # Keyword args always should be after Positional args
print("Stop")