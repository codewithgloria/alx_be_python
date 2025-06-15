import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # let starting balance be $100

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    try:
        command, *params = sys.argv[1].split(':')
        amount = float(params[0]) if params else None
    except ValueError:
        print("Invalid input format. Please use <command>:<amount>")
        sys.exit(1)

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")

    elif command == "withdraw" and amount is not None:
        success = account.withdraw(amount)
        if not success:
            print("Insufficient funds.")
        else:
            print(f"Withdrew: ${amount:.2f}")

    elif command == "display":
        account.display_balance()

    else:
        print("Invalid command.")
        print("Available commands: deposit:<amount>, withdraw:<amount>, display")

if __name__ == "__main__":
    main()