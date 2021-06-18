import time

eur = 0.83
jpy = 110.478
cny = 6.40
mxn = 20.26
usd = 1
start_Currency = "usd"
requested_Currency = "usd"
currencyCheck = ["usd","mxn","cny","jpy","eur"]
usdValues = [1,20.26,6.40,110.478,0.83]
start_Amount = 0.00
converted = 0.00
tracker = 0

status = True

#check for exit flag
def exitRequest(input):
    if ( input == "stop" ):
            exit()

def converter(currency):
    global converted
    global status
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
        status = True



def usdConverter(current_Currency,currency,amount):
    global converted
    global status
    global currencyCheck
    global usdValues

    #we check where the value is in the array and use that to find the value in the other array
    for i in currencyCheck:
        if currency == i:
            index = currencyCheck.index(i)
            converted = round(amount * usdValues[index],2)

    


print("Welcome to my Currency Converter! Follow the prompts and then please type stop when you're done")
time.sleep(1)

#Parameter input
while status:
    #Checking to see if valid option, value starts off Valid, will always run once
    start_Currency = input("What is the currency you're using now?\n").lower() #Force lower to for comparisons
    exitRequest(start_Currency)

    while start_Currency not in currencyCheck:
        start_Currency = input("That's not a valid option, Please enter a valid option (USD, EUR, JPY, CNY, MXN)\n").lower()
        exitRequest(start_Currency)
    else:
        converter(start_Currency)



#We need a check for valid floats - TASK!
start_Amount = float(input("Enter the amount of money you wish to convert:\n"))
exitRequest(start_Amount)

#runs converter function to convert current currency
converter(start_Currency)

status = True
time.sleep(1)

while status:
    if requested_Currency in currencyCheck:
        requested_Currency = input("Which currency do you wish to convert to?(USD, EUR, JPY, CNY, MXN)\n").lower()
        converter(requested_Currency)
    else:
        requested_Currency = input("That's not a valid option, Please enter a valid option (USD, EUR, JPY, CNY, MXN)\n").lower()
        converter(requested_Currency)

usdConverter(start_Currency,requested_Currency,start_Amount)

print("Start : " + start_Currency.upper() + " : " + str(start_Amount))
print("End : " + requested_Currency.upper() + " : " + str(converted)) 