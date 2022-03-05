# WAP to convert Currency
currency_dict = {}
with open("currency_rates.txt") as f:
    lines = f.readlines()
    for line in lines:
        currency = line.split(" \t")
        currency_dict[currency[0]] = currency[1]
    print(currency_dict)

amount = int(input("Enter amount: \n"))
print("Available currencies: ")
# for item in currency_dict.keys():
#     print(item)
[print(item) for item in currency_dict.keys()]
curr = input("Enter the name of currency you want to convert from above list: ")
print(f"Value of {amount} INR is equal to {amount * (1/float(currency_dict[curr])):.2f} {curr}")
