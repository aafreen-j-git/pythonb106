

#if __name__ == '__main__':


  # ''' DA is 40% of Basic pay and HRA is 10% of Basic pay
   # WAP to take a input of Basic pay from user and calculate DA
   # HRA and Gross pay'''
basic_pay=float(input("Enter basic salary of an employe :"))
da_perc=40
hra_perc=10
da=da_perc/100*basic_pay
hra=hra_perc/100*basic_pay
gross_pay=basic_pay+da+hra
print("DA % :",da)
print("HRA % :",hra)
print("gross pay :" ,gross_pay)

