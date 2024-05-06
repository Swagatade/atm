class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 5000
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f'Deposit: +${amount}')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f'Withdrawal: -${amount}')
        else:
            print("Insufficient funds!")

    def transfer(self, recipient, amount):
        if amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f'Transfer: -${amount} to {recipient.user_id}')
            recipient.transaction_history.append(f'Transfer: +${amount} from {self.user_id}')
        else:
            print("Insufficient funds!")

    def get_transaction_history(self):
        return self.transaction_history


class ATM:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, pin):
        if user_id not in self.users:
            self.users[user_id] = User(user_id, pin)
            print("User added successfully!")
        else:
            print("User already exists!")

    def authenticate_user(self, user_id, pin):
        if user_id in self.users:
            if self.users[user_id].pin == pin:
                print("Authentication successful!")
                return True
            else:
                print("Invalid PIN!")
        else:
            print("User not found!")
        return False

    def display_menu(self):
        print("1. Transactions History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Quit")

    def start(self):
        print("Welcome to the ATM!")
        user_id = input("Enter User ID: ")
        pin = input("Enter PIN: ")

        if self.authenticate_user(user_id, pin):
            user = self.users[user_id]
            while True:
                self.display_menu()
                choice = input("Enter your choice: ")
                if choice == '1':
                    print("Transaction History:")
                    for transaction in user.get_transaction_history():
                        print(transaction)
                elif choice == '2':
                    amount = float(input("Enter amount to withdraw: "))
                    user.withdraw(amount)
                elif choice == '3':
                    amount = float(input("Enter amount to deposit: "))
                    user.deposit(amount)
                elif choice == '4':
                    recipient_id = input("Enter recipient's User ID: ")
                    if recipient_id in self.users:
                        recipient = self.users[recipient_id]
                        amount = float(input("Enter amount to transfer: "))
                        user.transfer(recipient, amount)
                    else:
                        print("Recipient not found!")
                elif choice == '5':
                    print("Thank you for using the ATM!")
                    break
                else:
                    print("Invalid choice!")


if __name__ == "__main__":
    atm = ATM()
    atm.add_user("user1", "1234")  # Adding a user for testing
    atm.start()
