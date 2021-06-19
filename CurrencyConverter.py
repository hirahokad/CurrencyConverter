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

def inputModule(input):
    global status
    if input not in currencyCheck:
        print("Please enter a valid option!")
    else:
        status = False


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

while status:
    #Checking to see if valid option, value starts off Valid, will always run once
    start_Currency = input("What is the currency you're using now?\n").lower() #Force lower to for comparisons
    exitRequest(start_Currency)
    inputModule(start_Currency)

status = True

#We need a check for valid floats - TASK!
start_Amount = float(input("Enter the amount of money you wish to convert:\n"))
exitRequest(start_Amount)


while status:
    requested_Currency = input("Which currency do you wish to convert to?(USD, EUR, JPY, CNY, MXN)\n").lower()
    exitRequest(requested_Currency)
    inputModule(requested_Currency)


#This section will check what the current currency is and route to the appropriate function (We might not need start_Currency in the below function
usdConverter(start_Currency,requested_Currency,start_Amount)

print("Start : " + start_Currency.upper() + " : " + str(start_Amount))
print("End : " + requested_Currency.upper() + " : " + str(converted)) 