class Account:
    bank_name="Equity"
    def __init__(self,account_name,account_number,amount):
        self.account_name=account_name
        self.acount_number=account_number
        self.amount=amount
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0
    def bank_details(self):
        return f"Your account name is {self.account_name},{self.acount_number},has a balance of {self.amount}"
    def account_balance_after_deposit(self,deposit):
        new_balance=deposit+self.amount
        return f"Your new balance is {new_balance}"
    def account_balance_after_withdrawal(self,withdrawal):
        balance=self.amount-withdrawal
        return f"Your new balance is {balance}"
    def check_balance(self,deposit):
        self.deposit=deposit
        if amount <= 0:
          return "Invalid deposit amount"
        return f"{self.amount}+{self.deposit}-{self.withdrawal}"
    def borrow_loan(self, amount):
        if self.loan_balance > 0:
            return "Sorry, you have an outstanding loan. Please repay it first."
        elif amount < 100:
            return "Loan request declined. Minimum loan amount is KES 100."
        elif len(self.deposits) < 10:
            return "Loan request declined. Please make at least 10 deposits first."
        elif amount > (sum(transaction["amount"] for transaction in self.deposits)/3):
            return "Loan request declined. Maximum amount you can borrow is one-third of your total deposits."
        else:
            self.loan_balance += amount
            self.balance += amount
            return "You have successfully borrowed KES "+str(amount)+". Your new balance is KES "+str(self.balance)+"."

    def repay_loan(self, amount):
        if amount <= 0:
            return "Invalid repayment amount"
        elif amount > self.loan_balance:
            overpayment = amount - self.loan_balance
            self.loan_balance = 0
            self.balance += overpayment
            return "Thank you for repaying your loan. Your overpayment of KES "+str(overpayment)+" has been credited to your account. Your new balance is KES "+str(self.balance)+"."
        else:
            self.loan_balance -= amount
            self.balance -= amount
            return "Thank you for repaying your loan. Your new loan balance is KES "+str(self.loan_balance)+"."
    def transfer(self, amount, destination_account):
        if amount <= 0:
            return "Invalid transfer amount"
        elif amount > self.balance:
            return "Insufficient balance. Your current balance is KES "+str(self.balance)+"."
        else:
            self.balance -= amount
            destination_account.balance += amount
            return "You have transferred KES "+str(amount)+" from "+self.name+" account number "+str(self.account_number)+" to "+destination_account.name+" account number "+str(destination_account.account_number)+". Your new balance is KES "+str(self.balance)+"."
    
    
    
    