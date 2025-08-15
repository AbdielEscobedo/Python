class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, category_to_transfer):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category_to_transfer.name}")
            category_to_transfer.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            description = item["description"][:23].ljust(23)
            amount = f"{item['amount']:.2f}".rjust(7)
            items += f"{description}{amount}\n"
            total += item["amount"]
        output = title + items + f"Total: {total:.2f}"
        return output

def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    total_spent = 0
    category_withdrawals = {}

    for category in categories:
        spent_in_category = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent_in_category += abs(item["amount"])
        category_withdrawals[category.name] = spent_in_category
        total_spent += spent_in_category

    percentages = {}
    for name, spent in category_withdrawals.items():
        if total_spent == 0:  # Avoid division by zero
            percentages[name] = 0
        else:
            percentages[name] = int((spent / total_spent) * 100)

    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for category in categories:
            if percentages[category.name] >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    # Corrected line calculation: 3 hyphens per category + 1 for the initial space + 1 for the last space
    chart += "    -" + "---" * len(categories) + "\n"

    max_name_length = 0
    for category in categories:
        if len(category.name) > max_name_length:
            max_name_length = len(category.name)

    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += f"{category.name[i]}  "
            else:
                chart += "   "
        if i < max_name_length -1:
            chart += "\n"

    return chart.rstrip('\n')
