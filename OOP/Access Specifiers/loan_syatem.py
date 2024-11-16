class LoanTransaction:
    def __init__(self):
        self.__loan_amount = 0
        self.__acc_src = 0
        self.__acc_dest = 0
        self.__total_deb=0
        self.__total_ben=0
    def set_loanamt(self, amt):
        self.__loan_amount = amt
    
    def set_acc_src(self, acc1):
        self.__acc_src = acc1

    def set_acc_dest(self, acc2):
        self.__acc_dest = acc2

    def set_total_deb(self, deb):
        self.__total_deb = deb

    def set_total_ben(self, ben):
        self.__total_ben = ben

    def debit_loan(self, min_bal):
        if self.__total_deb-self.__loan_amount < min_bal:
            print("Insufficient balance")
        else:
            self.__total_deb-=self.__loan_amount

    def credit_loan(self):
        self.__total_ben+=self.__loan_amount

    def get_total_deb(self):
        return self.__total_deb
    
    def get_total_ben(self):
        return self.__total_ben
    

lo = LoanTransaction()

total_deb=int(input("Enter Total Amount In Debiter's Account: "))
total_ben=int(input("Enter Total Amount In Debiter's Account: "))

amt=int(input("Enter Loan Amount: "))
min_bal=int(input("Enter Minimum Balance In Debiter's Account: "))

acc1=input("Enter Debiter's Account No.: ")
acc2=input("Enter Beneficary Account No.: ")

lo.set_loanamt(amt)
lo.set_acc_src(acc1)
lo.set_acc_dest(acc2)
lo.set_total_deb(total_deb)
lo.set_total_ben(total_ben)

lo.debit_loan(min_bal)
lo.credit_loan()

print("Amount Left In Defiter's Account: ",acc1, " : ", lo.get_total_deb())
print("Amount Left In Beneficiary's Account:", acc2, " : ",lo.get_total_ben())
