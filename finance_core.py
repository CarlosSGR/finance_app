"""Core business logic for the Personal Finance Tracker."""

# Default biweekly expenses
GASOLINE = 800
PC = 643
CRUNCHYROLL = 50
CHATGPT = 500


def calculate_net_budget(current_budget: float, current_debt: float) -> float:
    """Return the remaining balance after subtracting debt from the budget."""
    return float(current_budget) - float(current_debt)


def calculate_biweekly_outstanding(
    gas_paid: bool,
    pc_paid: bool,
    crunchy_paid: bool,
    chatgpt_paid: bool,
) -> float:
    """Return the amount of biweekly expenses that haven't been paid yet."""
    outstanding = 0
    if not gas_paid:
        outstanding += GASOLINE
    if not pc_paid:
        outstanding += PC
    if not crunchy_paid:
        outstanding += CRUNCHYROLL
    if not chatgpt_paid:
        outstanding += CHATGPT
    return outstanding


def summarize_payments(
    gas_paid: bool,
    pc_paid: bool,
    crunchy_paid: bool,
    chatgpt_paid: bool,
    total: float,
) -> str:
    """Return a human readable summary of the payment situation."""
    outstanding = calculate_biweekly_outstanding(
        gas_paid, pc_paid, crunchy_paid, chatgpt_paid
    )
    if outstanding == 0:
        return (
            f"Congrats! You have paid your biweekly expenses. You still need ${total} to pay everything."
        )
    return (
        f"You haven't paid ${outstanding} from your biweekly expenses. And you still have to pay ${total}. So you need to pay the grand total of ${(total + outstanding)}"
    )