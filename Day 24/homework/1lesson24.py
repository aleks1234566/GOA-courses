#1)შექმენით 3 ფუნქცია თქვენი ფანტაზიით, გამოიყენეთ პარამეტრები და return keyword. (ძალიან მარტივები არ გინდათ, რაც უფრო რთულს გააკეთებთ თქვენი დონისთვის მით უფრო კარგი იქნებაA
#A) 
def Log_in(password, num ):
      while password !=  "Goa":
            if num == 0:
                  print("Too many wrong attempts, your account is blocked")
            else:
                  print("Wrong you have " + str(num) + " " + "chances left")
                  num -= 1
                  password = input("Try again: ")

Log_in(input("Please Enter your password: "), 2)



#B)
