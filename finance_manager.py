class FinanceManager:
    """Simple budget manager for monthly expenses and purchases."""

    def __init__(self):
        self.income = 0.0
        self.expenses = {}

    def add_expense(self, name: str, amount: float) -> None:
        """Add or update an expense."""
        self.expenses[name] = amount

    def remove_expense(self, name: str) -> None:
        """Remove an expense if it exists."""
        self.expenses.pop(name, None)

    def monthly_summary(self) -> tuple[float, float]:
        """Return total monthly expenses and leftover budget."""
        total = sum(self.expenses.values())
        leftover = self.income - total
        return total, leftover

    def check_purchase(self, cost: float) -> tuple[bool, float]:
        """Check if a purchase is affordable after expenses."""
        _, leftover = self.monthly_summary()
        remaining = leftover - cost
        return remaining >= 0, remaining


def main() -> None:
    manager = FinanceManager()
    manager.income = float(input("Enter your monthly income: "))

    while True:
        print("\nOptions:")
        print("1. Add or update an expense")
        print("2. Remove an expense")
        print("3. View summary")
        print("4. Can I afford a purchase?")
        print("5. Quit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            name = input("Expense name: ")
            amount = float(input("Monthly amount: "))
            manager.add_expense(name, amount)
            print(f"Added/updated expense '{name}' for ${amount:.2f} per month.")
        elif choice == "2":
            name = input("Expense name to remove: ")
            manager.remove_expense(name)
            print(f"Removed expense '{name}'.")
        elif choice == "3":
            total, leftover = manager.monthly_summary()
            print("\nCurrent expenses:")
            for n, amt in manager.expenses.items():
                print(f"- {n}: ${amt:.2f}")
            print(f"Total monthly expenses: ${total:.2f}")
            print(f"Leftover after expenses: ${leftover:.2f}")
        elif choice == "4":
            cost = float(input("How much does the item cost? "))
            can_buy, remaining = manager.check_purchase(cost)
            if can_buy:
                print(
                    f"You can buy it and will have ${remaining:.2f} left after expenses."
                )
            else:
                print(
                    f"You cannot buy it. You would be short ${-remaining:.2f} after expenses."
                )
        elif choice == "5":
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()