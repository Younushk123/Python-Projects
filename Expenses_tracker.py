import csv


class Transaction:
    def __init__(self, type, category, amount, date):
        self.type = type
        self.category = category
        self.amount = int(amount)
        self.date = date


class ExpenseTracker:
    def __init__(self):
        self.transactions = []

    def load_from_csv(self, filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transaction = Transaction(
                    row['type'],
                    row['category'],
                    row['amount'],
                    row['date']
                )
                self.transactions.append(transaction)

   

    def monthly_summary(self):
        income = 0
        expense = 0

        for t in self.transactions:
            if t.type == "Income":
                income += t.amount
            elif t.type == "Expense":
                expense += t.amount

        balance = income - expense
        saving = balance * 0.5  # Assuming 50% of the balance is saved

        print("Total Income:", income)
        print("Total Expense:", expense)
        print("Balance:", balance)
        print("Saving:", saving)
        


tracker = ExpenseTracker()
tracker.load_from_csv("file.csv") 

transactions = len(tracker.transactions)
print(f"Tansactions: {transactions}")
tracker.monthly_summary()