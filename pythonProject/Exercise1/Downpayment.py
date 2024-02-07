credScore = int(input("what is yout creadit score"))
home_cost = float(1000000)
if credScore > 701 and credScore < 999:
    dwnPymt = float(home_cost * 0.1)
    print(f'you have to pay $ {dwnPymt} as downpayment of house')
elif credScore < 700:
    dwnPymt = float(home_cost * 0.2)
    print(f'you have to pay $ {dwnPymt} as downpayment of house')



