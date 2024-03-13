# მომხმარებელს ჯერ შემოატანინეთ ბიუჯეტი, შემდეგ კი ის თანხა, რომელიც სასურველი ნივთის საყიდლად სჭირდება. დაბეჭდეთ შეუძლია ყიდვა თუ არა.
user_budget = int(input("Enter your budget: "))
price = int(input("Enter price: "))
if user_budget >= price:
    print("You can buy a product")
else:
    print("Sorry you can't buy a product ")

# მომხმარებელს შეეკითხეთ წელი და და დაპრინტეთ ნაკიანია ის თუ არა.
user_age = int(input("Enter your age: "))
if user_age >= 18:
    print("You can take part in elections")
else:
    print("You can't")

# მომხმარებელს შეეკითხეთ for ციკლისთვის მინიმალური, მაქსიმალური მნიშვნელობები და step-ის რიცხვი. ამ მნიშვნელობებით მოახდინეთ ციკლის მუშაობა და დაპრინტეთ თითოეული რიცხვი.
min_num = int(input("Enter your number: "))
max_num = int(input("Enter your number: "))
step_num = int(input("Enter your number:"))
for i in range(min_num,max_num, step_num ):
    print(i)


#მომხმარებელს შემოატანინეთ რიცხვი და შეამოწმეთ თუ არის როგორც ორის, ასევე სამის ჯერადი. არსებობის შემთხვევაში დაპრინტეთ ეს რიცხვი, ხოლო თუ არ იქნება მაშინ თავიდან შეეკითხეთ (გამოიყენეთ while ციკლი).
num1 = int(input("Enter your number: "))
while num1 % 2 == 0 and num1 % 3 == 0:
    print(num1)
if num1  % 2 != 0 and num1 % 3 != 0:
    print(input("Try agin:"))


#მომხმარებელს შეეკითხეთ წელი და და დაპრინტეთ ნაკიანია ის თუ არა.
year = int(input("Enter yaer:"))
if year % 4 == 0:
    print(year)






