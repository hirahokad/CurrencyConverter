import time

eur = 0.83
jpy = 110.478
cny = 6.40
mxn = 20.26
usd = 1
start_Currency = "usd"
currencyCheck = ["usd","mxn","cny","jpy","eur"]
start_Amount = "usd"
converted = 0.00
tracker = 0

status = True

def converter(currency):
    global converted
    status = True
    if ( currency == "stop" ) :
        exit()

    if ( currency == "eur"):
        converted = round(start_Amount * eur,2)
        status = False
    elif ( currency == "jpy"):
        converted = round(start_Amount * jpy,2)
        status = False
    elif ( currency == "cny"):
        converted = round(start_Amount * cny,2)
        status = False
    elif ( currency == "mxn"):
        converted = round(start_Amount * mxn,2)
        status = False
    elif ( currency == "usd"):
        converted = round(start_Amount * usd,2)
        status = False
    else:
        print("That's not a valid option")


print("Welcome to my Currency Converter! Follow the prompts and then please type stop when you're done")
time.sleep(2)


while status:
    if start_Currency in currencyCheck:
        start_Currency = input("What is the currency you're using now?\n").lower()
        if ( start_Currency == "stop" ):
            exit()

        start_Amount = float(input("Enter the amount of money you wish to convert:\n"))
        #runs converter function to convert current currency
        converter(start_Currency)
        #If option is valid we want to break
        status = False
    else:
        print("Please enter a Valid option.")
        #If Option isn't valid we want to loop
        status = True

status = True
time.sleep(1)

while status and tracker == 0:
    if start_Currency in currencyCheck:
        requested_Currency = input("Which currency do you wish to convert to?(USD, EUR, JPY, CNY, MXN)\n").lower()
        converter(requested_Currency)
        status = False
    else:
        print("Please enter a Valid option.")

converter(requested_Currency)

print("Start : " + start_Currency + " : " + str(start_Amount))
print("End : " + requested_Currency + " : " + str(converted)) 