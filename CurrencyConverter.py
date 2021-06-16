import time

eur = 0.83
jpy = 0.0091
cny = 0.16
mxn = 0.050
usd = 1
start_Currency = "usd"
currencyCheck = ["usd","mxn","cny","jpy","eur"]

status = True

def converter(currency):
    status = True
    if ( currency == "eur"):
        converted = start_Converstion * eur
        status = False
    elif ( currency == "jpy"):
        converted = start_Converstion * jpy
        status = False
    elif ( currency == "cny"):
        converted = start_Converstion * cny
        status = False
    elif ( currency == "mxn"):
        converted = start_Converstion * mxn
        status = False
    elif ( currency == "usd"):
        converted = start_Converstion * usd
        status = False
    else:
        print("That's not a valid option")


print("Welcome to my Currency Converter! Follow the prompts and then please type 1 when you're done")
time.sleep(2)


while status:
    if start_Currency in currencyCheck:
        print("What is the currency you're using now?")
        converter(start_Currency)
        status = False
    else:
        print("Please enter a Valid option.")

status = True
time.sleep(1)

start_Amount = float(input("Enter the amount of money you wish to convert:\n"))
start_Converstion = start_Currency * start_Amount

requested_Currency = input("Which currency do you wish to convert to?(USD, EUR, JPY, CNY, MXN)\n").lower()

while status:
    if start_Currency in currencyCheck:
        requested_Currency = input("Which currency do you wish to convert to?(USD, EUR, JPY, CNY, MXN)\n").lower()
        converter(requested_Currency)
        status = False
    else:
        print("Please enter a Valid option.")

converter(requested_Currency)

print(f"You will have {converted} {requested_Currency}")



