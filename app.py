#Biweekly expenses
gasoline = 800
pc = 643
crunchyroll = 50
chatgpt = 500


def ask_payment(question):
    response = input(f"{question} (y/n): ").strip().lower()
    return response == "y"

def ask_current_debt():
    current_budget = input("How much do you have? \n")
    #640
    current_debt = input("How much do you have in debt? \n")
    #5246.22

    total = float(current_budget) - float(current_debt)
    if total < 0:
        total * -1

    if total >= 0:
        print(f"We are off to a great start, we currently have ${total} in positive numbers. Let's check if we paid our biweekly expenses.")
        return total
    else:
        print(f"Mala noticia mi gente. We have {total} in current debt. And we still need to check if we paid our biweekly expenses.")
        return total

def biweekly_expenses_payment(gasPayment, pcPayment, crunchyPayment, chatgptPayment, total):
    biweekly_expense = 0
    if not gasPayment:
        biweekly_expense += gasoline
    if not pcPayment:
        biweekly_expense += pc
    if not crunchyPayment:
        biweekly_expense += crunchyroll
    if not chatgptPayment:
        biweekly_expense += chatgpt

    if biweekly_expense == 0:
        return f"Congrats! You have paid your biweekly expenses. You still need ${total} to pay everything."
    else:
        return f"You haven't paid ${biweekly_expense} from your biweekly expenses. And you still have to pay ${total}. So you need to pay the grand total of ${(total + biweekly_expense)}"


#Ask the user
total = ask_current_debt()
print("Did you already pay the following expenses?")
gas_paid = ask_payment("Gasoline")
pc_paid = ask_payment("PC payment")
crunchy_paid = ask_payment("Crunchyroll")
chatgpt_paid = ask_payment("ChatGPT subscription")

#Result
result = biweekly_expenses_payment(gas_paid, pc_paid, crunchy_paid, chatgpt_paid, total)
print(result)



###The code is good, but for now is heavily oriented on if we have negative numbers, so there are some few things that could change to improve the code