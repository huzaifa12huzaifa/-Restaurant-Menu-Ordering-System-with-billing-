choice_starter = 0
bill_starter = 0
bill_drinks=0
bill_main_course=0
bill_dessert=0

class Bill:
    def bill_print(self):
        print("Bill for starters:", bill_starter)
        print("Bill for drinks:", bill_drinks)
        print("Bill for main course:", bill_main_course)
        print("Bill for dessert:", bill_dessert)


class Drinks:
    def beavreges(self):
        global bill_drinks
        print("11. Cola - $2.99")
        print("12. Lemonade - $3.99")
        print("13. Iced Tea - $2.99")
        print("14. Orange Juice - $3.99")
        print("15. Strawberry Smoothie - $4.99")
        print("16. Mango Lassi - $3.99")
        print("17. Cappuccino - $3.99")
        print("18. Hot Chocolate - $3.99")
        print("19. Bottled Water - $1.99")
        print("20. Sparkling Water - $2.99")
        choice = input("Please enter the choice of the beverage you choose: ")

        if choice == "11":
            print("Cola")
            bill_drinks = 2.99
        elif choice == "12":
            print("Lemonade")
            bill_drinks = 3.99
        elif choice == "13":
            print("Iced Tea")
            bill_drinks = 2.99
        elif choice == "14":
            print("Orange Juice")
            bill_drinks = 3.99
        elif choice == "15":
            print("Strawberry Smoothie")
            bill_drinks = 4.99
        elif choice == "16":
            print("Mango Lassi")
            bill_drinks = 3.99
        elif choice == "17":
            print("Cappuccino")
            bill_drinks = 3.99
        elif choice == "18":
            print("Hot Chocolate")
            bill_drinks = 3.99
        elif choice == "19":
            print("Bottled Water")
            bill_drinks = 1.99
        elif choice == "20":
            print("Sparkling Water")
            bill_drinks = 2.99
        else:
            print("Invalid choice!")


class Rating:
    def res_rating(self):
        pass
class Main_Course:
    def main_course(self):
        global bill_main_course

        print("21. Grilled Chicken - $12.99")
        print("22. Beef Steak - $16.99")
        print("23. Vegetarian Pasta - $10.99")
        print("24. Shrimp Scampi - $14.99")
        print("25. Margherita Pizza - $11.99")
        print("26. Salmon Fillet - $15.99")
        print("27. BBQ Ribs - $17.99")
        print("28. Eggplant Parmesan - $10.99")
        print("29. Tandoori Chicken - $13.99")
        print("30. Sushi Platter - $18.99")

        choice = input("Please enter the choice of the main course you choose: ")

        if choice == "21":
            print("Grilled Chicken")
            bill_main_course = 12.99
        elif choice == "22":
            print("Beef Steak")
            bill_main_course = 16.99
        elif choice == "23":
            print("Vegetarian Pasta")
            bill_main_course = 10.99
        elif choice == "24":
            print("Shrimp Scampi")
            bill_main_course = 14.99
        elif choice == "25":
            print("Margherita Pizza")
            bill_main_course = 11.99
        elif choice == "26":
            print("Salmon Fillet")
            bill_main_course = 15.99
        elif choice == "27":
            print("BBQ Ribs")
            bill_main_course = 17.99
        elif choice == "28":
            print("Eggplant Parmesan")
            bill_main_course = 10.99
        elif choice == "29":
            print("Tandoori Chicken")
            bill_main_course = 13.99
        elif choice == "30":
            print("Sushi Platter")
            bill_main_course = 18.99
        else:
            print("Invalid choice!")


class Deserts:
    def deserts(self):
        bill_dessert = 0

        print("31. Chocolate Cake - $6.99")
        print("32. Apple Pie - $5.99")
        print("33. Ice Cream Sundae - $4.99")
        print("34. Cheesecake - $7.99")
        print("35. Brownie - $4.99")
        print("36. Tiramisu - $8.99")
        print("37. Fruit Tart - $6.99")
        print("38. Panna Cotta - $5.99")
        print("39. Creme Brulee - $7.99")
        print("40. Churros - $4.99")

        choice = input("Please enter the choice of the dessert you choose: ")

        if choice == "31":
            print("Chocolate Cake")
            bill_dessert = 6.99
        elif choice == "32":
            print("Apple Pie")
            bill_dessert = 5.99
        elif choice == "33":
            print("Ice Cream Sundae")
            bill_dessert = 4.99
        elif choice == "34":
            print("Cheesecake")
            bill_dessert = 7.99
        elif choice == "35":
            print("Brownie")
            bill_dessert = 4.99
        elif choice == "36":
            print("Tiramisu")
            bill_dessert = 8.99
        elif choice == "37":
            print("Fruit Tart")
            bill_dessert = 6.99
        elif choice == "38":
            print("Panna Cotta")
            bill_dessert = 5.99
        elif choice == "39":
            print("Creme Brulee")
            bill_dessert = 7.99
        elif choice == "40":
            print("Churros")
            bill_dessert = 4.99
        else:
            print("Invalid choice!")




class Menu_starter:
    def starter_menu(self):
        global bill_starter  # Declare bill_starter as a global variable
        print("1. Classic Caesar Salad - $8.99 ")
        print("2. Crispy Fried Calamari - $10.99")
        print("3. Garlic Parmesan Wings - $9.99 ")
        print("4. Bruschetta - $7.99")
        print("5. Spinach and Artichoke Dip - $8.99")
        print("6. Buffalo Chicken Sliders - $11.99")
        print("7. Loaded Potato Skins - $9.99")
        print("8. Caprese Skewers - $8.99")
        print("9. Mini Quesadillas - $7.99")
        print("10. Shrimp Cocktail - $12.99")
        i = input("Please enter the choice of the starter you choose! ")

        if i == "1":
            print("Classic Caesar Salad")
            bill_starter = 8.99
        elif i == "2":
            print("Crispy Fried Calamari")
            bill_starter = 10.99
        elif i == "3":
            print("Garlic Parmesan Wings")
            bill_starter = 9.99
        elif i == "4":
            print("Bruschetta")
            bill_starter = 7.99
        elif i == "5":
            print("Spinach and Artichoke Dip")
            bill_starter = 8.99
        elif i == "6":
            print("Buffalo Chicken Sliders")
            bill_starter = 11.99
        elif i == "7":
            print("Loaded Potato Skins")
            bill_starter = 9.99
        elif i == "8":
            print("Caprese Skewers")
            bill_starter = 8.99
        elif i == "9":
            print("Mini Quesadillas")
            bill_starter = 7.99
        elif i == "10":
            print("Shrimp Cocktail")
            bill_starter = 12.99
        else:
            print("Invalid choice!")

print("**************** Welcome to Taste Junction!!! ********************")
res = Menu_starter()
bi=Bill()
dr=Drinks()
ra=Rating()
mc=Main_Course()
des=Deserts()
i = input("Enter your name: ")
menu1 = input("Please enter 1 to see our starter menu: ")
if menu1 == "1":
    res.starter_menu()
elif menu1=="2":
    mc.main_course()
elif menu1=="3":
    dr.beavreges()
elif menu1=="4":
    des.deserts()
elif menu1=="5":
    bi.bill_print()
else:
    print("invalid")
    

