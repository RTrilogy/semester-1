
"""
    Portfolio Task - Week 4

    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.

    Name: Albert Costea
"""

def currency_converter(amount, from_currency, to_currency):

    conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }

    # your code here
    if to_currency == "inr":
        if from_currency == "gbp":
            amount = amount * 109.06
        elif from_currency == "cny":
            amount = amount * 11.81
        elif from_currency == "php":
            amount = amount * 1.45
        else:
            return "son"
    elif to_currency == "php":
        if from_currency == "gbp":
            amount = amount * 75.00
        elif from_currency == "cny":
            amount = amount * 8.12
        elif from_currency == "inr":
            amount = amount * 0.69
        else:
            return "son"
    elif to_currency == "cny":
        if from_currency == "gbp":
            amount = amount * 9.24
        elif from_currency == "php":
            amount = amount * 0.12
        elif from_currency == "inr":
            amount = amount * 0.09
        else:
            return "son"
    elif to_currency == "gbp":
        if from_currency == "cny":
            amount = amount * 0.11
        elif from_currency == "php":
            amount = amount * 0.01
        elif from_currency == "inr":
            amount = amount * 0.01
        else:
            return "son"
    if amount <= 0.00:
        return 0.0
    

    return str(round(amount, 2)) + " " + to_currency.upper()

# num = float(input("Enter num to convert: "))
# choice1 = input("Enter the currency it is: (gbp, cny, inr, php) ").lower()
# choice2 = input("Enter the currency to convert to: (gbp, cny, inr, php) ").lower()
print(currency_converter(101, "gbp", "php"))
print(currency_converter(1000, "cny", "gbp"))
print(currency_converter(20, "php", "inr"))
print(currency_converter(700, "inr", "cny"))
print(currency_converter(-20, "inr", "php"))

# Submit only this file currency_converter.py with the completed function.

# Remove any additional code you may have added during development and testing.
