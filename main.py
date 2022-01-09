import matplotlib.pyplot as plt
import numpy as np


class Mortgage:
    # Initializing all class attributes
    def __init__(self, loan, years, interest, r_frequency):
        self.loan = loan
        self.years = years
        self.interest = interest/100
        self.r_frequency = r_frequency

    # Method to calculate repayments
    def repayments(self):
        p0 = (self.loan * ((1 + self.interest/365) ** (365 * self.years)) *
              (((1 + self.interest/365) ** self.r_frequency) - 1) /
              (((1 + self.interest/365) ** (365 * self.years)) - 1))
        return p0

    # Method to calculate Remaining Principal Balance
    def balance_after(self, n):
        p0 = self.repayments()
        bn = (self.loan * ((1 + self.interest/365) ** (365 * n)) -
              p0 * (((1 + self.interest/365) ** (365 * n) - 1) /
                    (((1 + self.interest/365) ** self.r_frequency) - 1)))
        return bn

    # Printing everything
    def print(self):
        print()
        print(f'Loan Amount: {self.loan:.1f} $')
        print(f'Loan Term (Years): {self.years}')
        print(f'Interest: {self.interest*100}%')
        print(f'Fortnightly Repayments: {self.repayments():.2f}')
        print()

    # Method to draw graph using matplotlib
    def draw_balance_graph(self):
        balance = [self.balance_after(i) for i in range(1, int(self.years)+1)]  # Calculating balance for each year.
        years = [i for i in range(1, int(self.years)+1)]    # List of all years
        # plotting balance and years values,
        # here marker='o' are just points you'll see in graph
        plt.plot(years, balance, marker="o")
        plt.xticks(np.arange(min(years), max(years) + 1, 1.0))   # Writing each year in graph. (can be seen on x-axis)
        plt.yticks(np.arange(min(balance), max(balance) + 10000, 10000))
        plt.xlabel("Years")
        plt.ylabel("Balance")
        plt.title("Mortgage Balance by Years")
        plt.show()


# Main function
def main():
    # This loop and try-except block will take care of errors, i.e Invalid values
    while True:
        try:
            l = float(input("Enter the loan amount: "))
            break
        except ValueError:
            print("\nNot a valid value please try again...\n")

    while True:
        try:
            y = float(input("Enter loan term (Years): "))
            break
        except ValueError:
            print("\nNot a valid value please try again...\n")

    while True:
        try:
            p = float(input("Enter interest rate(%): "))
            break
        except ValueError:
            print("\nNot a valid value please try again...\n")

    while True:
        try:
            k = float(input("Enter repayment frequency (7/14/30, Weekly/Fortnightly/Monthly): "))
            break
        except ValueError:
            print("\nNot a valid value please try again...\n")

    a = Mortgage(l, y, p, k)
    a.print()
    a.draw_balance_graph()


main()
