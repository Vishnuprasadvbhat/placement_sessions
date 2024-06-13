class BankAccount:
    def __init__(self):
        self.balance = 2000
        self.cash = 10000
        self.pin = 1234

    def check_pin(self):
        print('Welcome to SBI Banking Server')
        curr_pin = int(input("Please enter your 4 digit pin to continue: "))
        if curr_pin == self.pin:
            command = input('Choose the operation:\n'
                            'Withdrawal\n'
                            'Balance Enquiry\n'
                            'Deposit\n'
                            'Pin Change\n')
            command= command.lower()
            if command == 'withdrawal':
                amount = int(input('Enter the withdrawing amount'))
                self.withdraw(amount)
            elif command == 'deposit':
                amount = int(input('Enter the withdrawing amount'))
                self.deposit(amount)
            elif command == 'balance enquiry':
                self.balance_enq()
            else:
                print('Entered Invalid Choice')
                self.check_pin(curr_pin)
        else:
            print('Invalid PIN Entered')
            print("Forgot PIN",self.pin_change())

    def pin_change(self):
        new_pin = int(input('Enter the new pin: '))
        if new_pin == self.pin:
            print('Entered Old Pin, Please use new combination')
            return self.pin_change()

        elif len(str(new_pin))>4:
            print('Invalid format')
            print('Allowed 4 digits only')
            return self.pin_change()

        elif new_pin == 0:
            print('Invalid format')
            print('PIN must contain numbers from 1 to 9')
            self.pin_change()

        elif new_pin < 0:
            print('Invalid format')
            print('PIN must contain numbers from 1 to 9')
            self.pin_change()

        else:
            print('PIN changed successfully')
            self.pin = new_pin
            self.check_pin()

    def withdraw(self, amount):
        if amount%100 == 0:
            if amount <= self.cash:
                if amount <= self.balance:
                    self.balance = self.balance - amount
                    print("The Withdraw was successful, the current balance is: ",self.balance)
                else:
                  print('Insufficient Balance')
            else:
                print("Insufficient funds, Kindly try again later")
        else:
            print('Enter the amount in multiples of 100')

    def balance_enq(self):
        print('The current balance is: ',self.balance)

    def deposit(self, amount):
        if amount%100 == 0:
            self.balance = self.balance + amount
            print('The amount is deposited successfully, Updated Balance: ', self.balance)
        else:
            print('Exception occurred')
            print('Please enter the amount in multiples of 100')

acc = BankAccount()
acc.check_pin()



