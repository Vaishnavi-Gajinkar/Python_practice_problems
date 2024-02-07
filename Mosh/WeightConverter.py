weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit.lower() == "l":
    convert = weight * 0.453592
    print(f'You are {convert} Kilos')
elif unit.lower() == 'k':
    convert = weight * 2.20462
    print(f'You are {convert} Pounds')

