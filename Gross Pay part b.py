''' write gross pay programe using user define function'''
def calculate_gross_pay(basic_pay,da_perc,hra_perc):
    da = da_perc / 100 * basic_pay
    hra = hra_perc / 100 * basic_pay
    gross_pay = basic_pay + da + hra
    return gross_pay
basic_pay=float(input("Enter basic salary of an employe :"))
da_perc=float(input("Enter DA percentage of an employe :"))
hra_perc=float(input("Enter HRA percentage of an employe :"))
gross_pay=calculate_gross_pay(basic_pay,da_perc,hra_perc)
print("DA % :",da_perc / 100 * basic_pay)
print("HRA % :",hra_perc / 100 * basic_pay)
print("gross pay :" ,gross_pay)

