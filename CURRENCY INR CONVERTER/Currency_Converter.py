with open('CurrencyData.txt') as file:
    lines=file.readlines()

currencyDict={}
for line in lines:
    parsed=line.split("\t")
    currencyDict[parsed[0]]=parsed[1]
amount=int(input("Enter the amount you want to convert from INR:"))
print("Enter the name of the currency you want to convert:\n")
for i, item in enumerate(currencyDict.keys(), start=1):
    print(f"{i}. {item}")
currency = input("please input:\n")
print(f"{amount} INR is equal to {amount*float(currencyDict[currency])} {currency} ")