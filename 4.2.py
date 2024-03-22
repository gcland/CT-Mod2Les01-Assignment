#APY = (deposit(1 + (rate))^years)

deposit = input("Enter your deposit amount: ")
deposit = int(deposit)

rate = input("Enter your interest rate: ")
rate = int(rate)

years = input("Enter the number of years since deposit: ")
years = int(years)

savings = (deposit*(1+(rate/100))**years)
print(savings)