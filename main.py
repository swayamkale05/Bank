from .account import BankAccount
accounts = {}


def validate_name(name):
    name = name.strip()

    if not name or not name.isalpha():
        raise ValueError("Name must contain only letters (A-Z or a-z).")

    return name


def get_account(name):
    name = validate_name(name)

    if name not in accounts:
        raise KeyError("No such account")

    return accounts[name]


def main():
    while True:
        print("\nSelect the below option:")
        print("1. Open account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. List accounts")
        print("6. Quit")

        choice = input("Enter the choice: ")

        try:
            if choice == "1":
                name = validate_name(input("Enter your name: "))

                if name in accounts:
                    print("Account already exists")
                else:
                    accounts[name] = BankAccount(name, 0)
                    print("Account opened successfully")

            elif choice == "2":
                name = input("Enter account holder name: ")
                account = get_account(name)

                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
                print("Deposit successful")

            elif choice == "3":
                name = input("Enter account holder name: ")
                account = get_account(name)

                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
                print("Withdrawal successful")

            elif choice == "4":
                sender = input("Enter sender name: ")
                sender_account = get_account(sender)

                receiver = input("Enter receiver name: ")
                receiver_account = get_account(receiver)

                if sender_account is receiver_account:
                    print("Cannot transfer to the same account")
                    continue

                amount = float(input("Enter transfer amount: "))

                sender_account.withdraw(amount)
                try:
                    receiver_account.deposit(amount)
                except Exception:
                    sender_account.deposit(amount)

                print("Transfer successful")

            elif choice == "5":
                if not accounts:
                    print("No accounts available")
                else:
                    print("Account details:")
                    for name, account in accounts.items():
                        print(f"Owner: {name}, Balance: {account.balance}")

            elif choice == "6":
                print("Thank you for using the banking system")
                break

            else:
                print("Invalid choice. Please select 1 to 6.")

        except ValueError as e:
            print(e)

        except KeyError:
            print("No such account")


if __name__ == "__main__":
    main()
