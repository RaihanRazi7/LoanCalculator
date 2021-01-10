import pyttsx3

engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()


# Calculations and Input Variables
totalAmount = int(input("What is the total amount that you are paying? "))
months = int(input(f"What is the term you want to take to pay {totalAmount}? "))
depositPrompt = input("Do you want a deposit? (y/n)")
monthsInYears = int((months / 12))
if depositPrompt == 'n':
    monthlyPayment = int((totalAmount / months))
    print(f"You have to pay {monthlyPayment} per month for {months} months or {monthsInYears} years.")
    talk(f"You have to pay {monthlyPayment} per month for {months} months or {monthsInYears} years.")

if depositPrompt == 'y':
    deposit = int(input("What is the deposit amount? "))
    totalAmount -= deposit
    monthlyPayment = int((totalAmount / months))
    print(f"You have to pay {monthlyPayment} per month for {months} months or {monthsInYears} years.")
    talk(f"You have to pay {monthlyPayment} per month for {months} months or {monthsInYears} years.")
