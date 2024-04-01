#1) შექმენით სია სადაც გექნებათ მოცემული 5 სახელი, index ების გამოყენებით დაბეჭდეთ ცალცალკე, dont use for cycle
names = ["Gio", "Nika", "Luka", "Gabo", "Ioane"]
print(names[0], names[1], names[2], names[3], names[4])

#2) შექმენით სია სადაც გექნებათ მოცემული 5 სახელი, for ციკლის გამოყენებით კი დაბეჭდეთ თითოეული
usernames = ["Aleqsandre", "Mari", "Lazare", "Anri", "Elene"]
for i in range(0, len(usernames)):
    print(usernames[i])

#3) შექმენით სია სადაც გექნებათ 1-10 ჩათვლი რიცხვები, for ციკლის გამოყენებით დაბეჭდეთ არ რიცხვების ჯამი ცალკე და ნამრავლი ცალკე

#4) შექმენით სტრინგი და გამოიტანეთ for ციკლის მეშვეობით ყველა სიმბოლო
info = "Goa"
for i in  range(0, len(info)):
    print(info[i])
    
#5) შექმენით სტრინგი  და for ციკლის გამოყენებით შეართეთ მხოლოდ ის სიმბოლოები რომლებიც არიან ლუწ ინდექსებზე
user_name = "Aleqsandre"
for i in range(0, len(user_name), 2):
    print(user_name[i])
    