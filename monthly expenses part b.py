# WAP TO CALCUATE MOTHLY EXPENCES BY TAKING INPUT OF EXPENCES FROM
#USER INCLUDE A FUNCTION TO CHECK WHETHER U WILL HAVE SAVINGS OR
#BORROW MONEY PRINT APPROPRIATE MESSAGE,,,

###FUNCTION DEFINING
def check(month_income,monthly_expenses):
    if month_income > monthly_expenses:
        remaining_money = month_income - monthly_expenses
        print("you have savings of money:", remaining_money, "Rs")
    else:
        remaining_money = monthly_expenses - month_income
        print("you have to borrow money: ", remaining_money, "Rs")
    #TAKE INPUT FROM USER
month_income=float(input("Enter monthly inome: "))
rent=float(input("Enter monthly rent of house: "))
food=float(input("Enter monthly food expenes: "))
electricity=float(input("Enter monthly elecricity bill : "))
phone=float(input("Enter monthly phone bill: "))
cable_tv=float(input("Enter monthil cable tv bill: "))
monthly_expenses=rent+food+electricity+phone+cable_tv
###FUNCTION CALLING
check(month_income,monthly_expenses)





