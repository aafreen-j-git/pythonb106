basic_pay=float(input("Enter basic salary of an employe :"))
da_perc=float(input("Enter DA percentage of an employe :"))
hra_perc=float(input("Enter HRA percentage of an employe :"))

da=da_perc/100*basic_pay
hra=hra_perc/100*basic_pay
gross_pay=basic_pay+da+hra
print("DA % :",da)
print("HRA % :",hra)
print("gross pay :" ,gross_pay)




