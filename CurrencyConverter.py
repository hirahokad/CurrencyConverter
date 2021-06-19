import time

eur = 0.83
jpy = 110.478
cny = 6.40
mxn = 20.26
usd = 1
start_Currency = "usd"
requested_Currency = "usd"
currencyCheck = ["usd","mxn","cny","jpy","eur"]
currencyRates = [[1,20.26,6.40,110.478,0.83],[0.048,1,0.31,5.33,0.041],[0.15,3.20,1,17.08,0.13],[0.0091,0.19,0.059,1,0.0076],[1.19,24.53,7.66,130.79,1]]

start_Amount = 0.00
converted = 0.00
tracker = 0

status = True

#check for exit flag
def exitRequest(input):
    if ( input == "stop" ):
            exit()

def inputCheck(input):
    global status
    if input not in currencyCheck:
        print("Please enter a valid option!")
    else:
        status = False

def currencyConverter(current_Currency,currency,amount):
    global converted
    global status
    global currencyCheck
    global currencyRates

    #we check where the value is in the array and use that to find the value in the other array - WE NEED TO CHECK HERE *BUG IS HERE*
    for i in currencyCheck:
        if current_Currency == i:
            index = currencyCheck.index(i)
            currencyRates = currencyRates[index]
    for i in currencyCheck:
        if currency == i:    
            index2 = currencyCheck.index(i)
            converted = round(amount * currencyRates[index2],2)

    
print("Welcome to my Currency Converter! Follow the prompts and then please type stop when you're done")
time.sleep(1)

while status:
    #Checking to see if valid option, value starts off Valid, will always run once
    start_Currency = input("What is the currency you're using now?\n").lower() #Force lower to for comparisons
    exitRequest(start_Currency)
    inputCheck(start_Currency)

status = True

#We need a check for valid floats - TASK!
start_Amount = float(input("Enter the amount of money you wish to convert:\n"))
exitRequest(start_Amount)


while status:
    requested_Currency = input("Which currency do you wish to convert to?(USD, EUR, JPY, CNY, MXN)\n").lower()
    exitRequest(requested_Currency)
    inputCheck(requested_Currency)


#This section will check what the current currency is and route to the appropriate function (We might not need start_Currency in the below function
currencyConverter(start_Currency,requested_Currency,start_Amount)

print("Start : " + start_Currency.upper() + " : " + str(start_Amount))
print("End : " + requested_Currency.upper() + " : " + str(converted)) 