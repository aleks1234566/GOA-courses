# 1) შექმენით ფუნქცია სახელად manual_reverse, რომელიც მიიღებს დალაგებულ კოლექციას. თქვენი დავალებაა, რომ შეაბრუნოთ ეს კოლექცია და დააბრუნოთ ამ სახით.
def manual_reverse(list):
    new_list = []
    for i in range(len(list) -1):
        new_list.append(i)
        return new_list



print(manual_reverse(["lUKA", "aLEQSANDRE", "NIKA"]))