# main-0.py
import sys
from bank_account import BankAccount

def main():
    # Change the initial balance here if you want another starting balance
    account = BankAccount(100.0)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>[:<amount>]")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = None
    if params and params[0] != '':
        try:
            amount = float(params[0])
        except ValueError:
            print("Error: amount must be numeric.")
            sys.exit(1)

    if command == "deposit" and amount is not None:
        try:
            account.deposit(amount)
            print(f"Deposited: ${amount}")
        except ValueError as e:
            print("Error:", e)
    elif command == "withdraw" and amount is not None:
        try:
            success = account.withdraw(amount)
            if success:
                print(f"Withdrew: ${amount}")
            else:
                print("Insufficient funds.")
        except ValueError as e:
            print("Error:", e)
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command or missing amount.")

if __name__ == "__main__":
    main()
Example runs:

shell
Copy code
python main-0.py deposit:50
# => Deposited: $50

python main-0.py withdraw:20
# => Withdrew: $20

python main-0.py withdraw:150
# => Insufficient funds.

python main-0.py display
# => Current Balance: $130.00  (depending on prior operations within this run)
