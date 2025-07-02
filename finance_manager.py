class FinanceManager:
    """Simple manager to track monthly expenses."""

    def __init__(self):
        # Stores expenses as name -> details
        # details is a dict with keys 'amount' and optionally 'months_remaining'
        self.expenses = {}

    def add_expense(self, name, amount, months=None, end_date=None):
        """Add a new expense.

        Parameters
        ----------
        name: str
            Name of the expense.
        amount: float
            Monthly amount.
        months: int, optional
            Number of months this expense will last.
        end_date: datetime.date, optional
            Specific end date for the expense. If provided, ``months`` should be ``None``.
        """
        if months is not None and end_date is not None:
            raise ValueError("Provide either months or end_date, not both")
        details = {"amount": amount}
        if months is not None:
            details["months_remaining"] = int(months)
        if end_date is not None:
            details["end_date"] = end_date
        self.expenses[name] = details

    def advance_month(self, current_date=None):
        """Advance one month and remove expired temporary expenses."""
        from datetime import date, timedelta

        if current_date is None:
            current_date = date.today()
        to_remove = []
        for name, info in self.expenses.items():
            if "months_remaining" in info:
                info["months_remaining"] -= 1
                if info["months_remaining"] <= 0:
                    to_remove.append(name)
            elif "end_date" in info:
                if current_date > info["end_date"]:
                    to_remove.append(name)
        for name in to_remove:
            del self.expenses[name]

    def total_monthly_expenses(self):
        return sum(info["amount"] for info in self.expenses.values())