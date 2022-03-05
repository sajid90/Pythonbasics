items = []
total_bill_amount = 0

while True:
    price = input("\nEnter price OR type q to exit: ")
    if price not in ('q', 'quit'):
        if not price.isdigit():
            print(f'\nPlease enter integers only. Passed value is "{price}"')
            continue
        total_bill_amount = total_bill_amount + int(price)
    else:
        if total_bill_amount == 0:
            print("\nYou did not enter any price. Thanks for using our calculator")
        else:
            print(f'\nTotal amount: {total_bill_amount}. Thanks for using our calculator')
        break
