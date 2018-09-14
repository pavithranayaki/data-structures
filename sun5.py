initial_bal=0
class InSufficientBalanceException(Exception):
    def pop_1(self):
        print("INSUFFICIENT BALANCE")
class InSufficientFundsException(Exception):
    def pop_2(self):
        print("INSUFFICIENT FUND")
dep_amount=int(input("ENTER THE DEPOSIT AMOUNT:"))
with_draw_amount=int(input("ENTER WITHDRAW AMOUNT:"))
bal=dep_amount-with_draw_amount
try:
    if bal<500:
        raise InSufficientBalanceException
except InSufficientBalanceException as er1:
    er1.pop_1()
try:
    if with_draw_amount>bal:
        raise InSufficientFundsException
except InSufficientFundsException as er2:
    er2.pop_2()
else:
    print(dep_amount-with_draw_amount)
