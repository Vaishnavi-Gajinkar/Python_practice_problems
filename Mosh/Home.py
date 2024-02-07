price = 1000000
# good_credit = bool(input('Is your credit score good? (True/False)'))
good_credit=False
if good_credit:
    cost = 0.1 * price
    print(f'You will need to pay only Rs.{cost} downpayment')
else:
    cost = 0.2 * price
    print(f'You will need to pay higher Rs.{cost} downpayment')