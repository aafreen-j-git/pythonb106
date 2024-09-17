### WAP to print Fizz if the number is divisible by 3,Buz if
### divisible by 5 ,if tey are divisible by both print FizzBuz''''''


for n in range(0,100):
   # n = int(input("enter a nomber : "))
  if (n % 3 == 0) and (n % 5 == 0):
        print("FizzBuzz")

  elif (n % 3==0):
        print("Fizz")
  elif (n % 5==0):
       print("Buzz")
  else:
      print(n)



