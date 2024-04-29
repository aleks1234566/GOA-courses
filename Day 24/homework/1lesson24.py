#შექმენით 3 ფუნქცია თქვენი ფანტაზიით, გამოიყენეთ პარამეტრები და return keyword. (ძალიან მარტივები არ გინდათ, რაც უფრო რთულს გააკეთებთ თქვენი დონისთვის მით უფრო კარგი იქნებაA
#1) 
def Log_in(password, num ):
      while password !=  "Goa":
            if num == 0:
                  print("Too many wrong attempts, your account is blocked")
            else:
                  print("Wrong you have " + str(num) + " " + "chances left")
                  num -= 1
                  password = input("Try again: ")

Log_in(input("Please Enter your password: "), 2)



#2)
def game_record() :
   records = [0]
   num = 0 
   for i in records:
      new_record = int(input("Please enter your record: "))
      num += new_record
       
      if num > 0 : 
             
            print("Congratulations your new record is ", new_record)
            records.append(new_record)
            print(records)
      else: 
          return ("Try again")
game_record()
