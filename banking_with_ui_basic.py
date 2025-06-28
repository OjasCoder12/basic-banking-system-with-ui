# banking system with a simple UI using tkinter
import tkinter as tk
from tkinter import messagebox
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance
class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking System")
        self.account = BankAccount("123456789")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Account Number:").grid(row=0, column=0)
        tk.Label(self.root, text=self.account.account_number).grid(row=0, column=1)

        tk.Label(self.root, text="Balance:").grid(row=1, column=0)
        self.balance_label = tk.Label(self.root, text=f"${self.account.get_balance():.2f}")
        self.balance_label.grid(row=1, column=1)

        tk.Label(self.root, text="Amount:").grid(row=2, column=0)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=2, column=1)

        tk.Button(self.root, text="Deposit", command=self.deposit).grid(row=3, column=0)
        tk.Button(self.root, text="Withdraw", command=self.withdraw).grid(row=3, column=1)

    def deposit(self):
        amount = self.get_amount()
        if amount is not None and self.account.deposit(amount):
            messagebox.showinfo("Success", f"Deposited ${amount:.2f}")
            self.update_balance()
        else:
            messagebox.showerror("Error", "Invalid deposit amount")

    def withdraw(self):
        amount = self.get_amount()
        if amount is not None and self.account.withdraw(amount):
            messagebox.showinfo("Success", f"Withdrew ${amount:.2f}")
            self.update_balance()
        else:
            messagebox.showerror("Error", "Invalid withdrawal amount or insufficient funds")

    def get_amount(self):
        try:
            return float(self.amount_entry.get())
        except ValueError:
            return None

    def update_balance(self):
        self.balance_label.config(text=f"${self.account.get_balance():.2f}")
def main():
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()
# This code creates a simple banking system with a UI using tkinter.