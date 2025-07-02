"""Command line interface for the Personal Finance Tracker."""

from finance_core import calculate_net_budget, summarize_payments


def ask_payment(question):
    response = input(f"{question} (y/n): ").strip().lower()
    return response == "y"

def ask_current_debt():
    current_budget = float(input("How much do you have? \n"))
    current_debt = float(input("How much do you have in debt? \n"))

    total = calculate_net_budget(current_budget, current_debt)

    if total >= 0:
        print(
            f"We are off to a great start, we currently have ${total} in positive numbers. Let's check if we paid our biweekly expenses."
        )
    else:
        print(
            f"Mala noticia mi gente. We have {total} in current debt. And we still need to check if we paid our biweekly expenses."
        )
    return total



#Ask the user
total = ask_current_debt()
print("Did you already pay the following expenses?")
gas_paid = ask_payment("Gasoline")
pc_paid = ask_payment("PC payment")
crunchy_paid = ask_payment("Crunchyroll")
chatgpt_paid = ask_payment("ChatGPT subscription")

#Result
result = summarize_payments(gas_paid, pc_paid, crunchy_paid, chatgpt_paid, total)
print(result)