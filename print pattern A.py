#to print the pattern A
'''     * * *
     *         *
     *         *
     * * * * * *
     *         *
     *         *'''

for row in range(6):
    for col in range(5):
        if((col==0 or col==4) and (row!=0))or((row==0 or row==3)and(col>0 and col<4)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()




