selected_starters = []
selected_main_courses = []
selected_drinks = []
selected_desserts = []
total_bill  =0
class Name:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f">>>>>>>>>>>> Welcome To <<<<<<<<<<<<<<\n{self.name}")


class Menu(Name):
    def __init__(self, name, menu):
        super().__init__(name)
        self.menu = menu

    def starter(self):
        print("\t\t", self.menu)
        print("1. Classic Caesar Salad ----------- $8.99")
        print("2. Crispy Fried Calamari --------- $10.99")
        print("3. Garlic Parmesan Wings ---------- $9.99")
        print("4. Bruschetta --------------------- $7.99")
        print("5. Spinach and Artichoke Dip ------ $8.99")
        print("6. Buffalo Chicken Sliders ------- $11.99")
        print("7. Loaded Potato Skins ------------ $9.99")
        print("8. Caprese Skewers ---------------- $8.99")
        print("9. Mini Quesadillas --------------- $7.99")
        print("10. Shrimp Cocktail -------------- $12.99")

        choice = int(input("\n\nPlease enter the choice of the starter you choose! "))
        global bill_starter  # Use global variable
        if choice == 1:
            print("Classic Caesar Salad")
            selected_starters.append("Classic Caesar Salad")
            bill_starter = 8.99
        elif choice == "2":
            print("Crispy Fried Calamari")
            selected_starters.append("Crispy Fried Calamari")
            bill_starter = 10.99
        elif choice == "3":
            print("Garlic Parmesan Wings")
            selected_starters.append("Garlic Parmesan Wings")
            bill_starter = 9.99
        elif choice == "4":
            print("Bruschetta")
            selected_starters.append("Bruschetta")
            bill_starter = 7.99
        elif choice == "5":
            print("Spinach and Artichoke Dip")
            selected_starters.append("Spinach and Artichoke Dip")
            bill_starter = 8.99
        elif choice == "6":
            print("Buffalo Chicken Sliders")
            selected_starters.append("Buffalo Chicken Sliders")
            bill_starter = 11.99
        elif choice == "7":
            print("Loaded Potato Skins")
            selected_starters.append("Loaded Potato Skins")
            bill_starter = 9.99
        elif choice == "8":
            print("Caprese Skewers")
            selected_starters.append("Caprese Skewers")
            bill_starter = 8.99
        elif choice == "9":
            print("Mini Quesadillas")
            selected_starters.append("Mini Quesadillas")
            bill_starter = 7.99
        elif choice == "10":
            print("Shrimp Cocktail")
            selected_starters.append("Shrimp Cocktail")
            bill_starter = 12.99
        else:
            print("Invalid choice!")
        starter_choice = input("You want to select more?  yes/no :")
        if starter_choice == "yes":
            print(object2.starter())
        if starter_choice == "no":
            print("OK")
        food_choice = input(("\nNow you want to see Main course of our Restaurent yes/no"))
        if food_choice == "yes":
            print(object1.main_course())
        if food_choice == "no":
            print(object1.print_name())


class Main_Course(Name):
    def __init__(self, name, menu):
        super().__init__(name)
        self.menu = menu

    def main_course(self):
        print("\t\tMain Course of the Restaurant")
        print("1. Grilled Chicken ------- $12.99")
        print("2. Beef Steak ------------ $16.99")
        print("3. Vegetarian Pasta ------ $10.99")
        print("4. Shrimp Scampi --------- $14.99")
        print("5. Margherita Pizza ------ $11.99")
        print("6. Salmon Fillet --------- $15.99")
        print("7. BBQ Ribs -------------- $17.99")
        print("8. Eggplant Parmesan ----- $10.99")
        print("9. Tandoori Chicken ------ $13.99")
        print("10. Sushi Platter -------- $18.99")

        choice = int(input("Please enter the choice of the main course you choose: "))
        global bill_main_course  # Use global variable
        if choice == 1:
            print("Grilled Chicken")
            selected_main_courses.append("Grilled Chicken")
            bill_main_course = 12.99
        elif choice == "2":
            print("Beef Steak")
            bill_main_course = 16.99
        elif choice == "3":
            print("Vegetarian Pasta")
            bill_main_course = 10.99
        elif choice == "4":
            print("Shrimp Scampi")
            bill_main_course = 14.99
        elif choice == "5":
            print("Margherita Pizza")
            bill_main_course = 11.99
        elif choice == "6":
            print("Salmon Fillet")
            bill_main_course = 15.99
        elif choice == "7":
            print("BBQ Ribs")
            bill_main_course = 17.99
        elif choice == "8":
            print("Eggplant Parmesan")
            bill_main_course = 10.99
        elif choice == "9":
            print("Tandoori Chicken")
            bill_main_course = 13.99
        elif choice == "10":
            print("Sushi Platter")
            bill_main_course = 18.99
        else:
            print("Invalid choice!")
        course_choice = input("You want to select more?  yes/no :")
        if course_choice == "yes":
            print(object1.main_course())
        if course_choice == "no":
            print("OK")
        drinks_choice = input(("\nNow you want to see Drinks of our Restaurent yes/no"))
        if drinks_choice == "yes":
            print(object3.drinks())
        if drinks_choice == "no":
            print(object1.print_name())


class Drinks(Name):
    def __init__(self, name, menu):
        super().__init__(name)
        self.menu = menu

    def drinks(self):
        print("1. Cola ---------------- $2.99")
        print("2. Lemonade ------------ $3.99")
        print("3. Iced Tea ------------ $2.99")
        print("4. Orange Juice -------- $3.99")
        print("5. Strawberry Smoothie - $4.99")
        print("6. Mango Lassi --------- $3.99")
        print("7. Cappuccino ---------- $3.99")
        print("8. Hot Chocolate ------- $3.99")
        print("9. Bottled Water --------$1.99")
        print("10. Sparkling Water ---- $2.99")

        choice = int(input("Please enter the choice of the beverage you choose: "))
        global bill_drinks  # Use global variable
        if choice == 1:
            print("Cola")
            selected_drinks.append("Cola")
            bill_drinks = 2.99
        elif choice == "2":
            print("Lemonade")
            bill_drinks = 3.99
        elif choice == "3":
            print("Iced Tea")
            bill_drinks = 2.99
        elif choice == "4":
            print("Orange Juice")
            bill_drinks = 3.99
        elif choice == "5":
            print("Strawberry Smoothie")
            bill_drinks = 4.99
        elif choice == "6":
            print("Mango Lassi")
            bill_drinks = 3.99
        elif choice == "7":
            print("Cappuccino")
            bill_drinks = 3.99
        elif choice == "8":
            print("Hot Chocolate")
            bill_drinks = 3.99
        elif choice == "9":
            print("Bottled Water")
            bill_drinks = 1.99
        elif choice == "10":
            print("Sparkling Water")
            bill_drinks = 2.99
        else:
            print("Invalid choice!")
        course_choice = input("You want to select more?  yes/no :")
        if course_choice == "yes":
            print(object3.drinks())
        if course_choice == "no":
            print("OK")
        drinks_choice = input(("\nNow you want to see Desert of our Restaurent yes/no"))
        if drinks_choice == "yes":
            print(object4.desert())
        if drinks_choice == "no":
            print(object1.print_name())


class Deserts(Name):
    def __init__(self, name, menu):
        super().__init__(name)
        self.menu = menu

    def desert(self):
        print("Our Desert hope you like it")
        print("1. Chocolate Cake ------- $6.99")
        print("2. Apple Pie ------------ $5.99")
        print("3. Ice Cream Sundae ----- $4.99")
        print("4. Cheesecake ----------- $7.99")
        print("5. Brownie -------------- $4.99")
        print("6. Tiramisu ------------- $8.99")
        print("7. Fruit Tart ----------- $6.99")
        print("8. Panna Cotta ---------- $5.99")
        print("9. Creme Brulee --------- $7.99")
        print("10. Churros -------------- $4.99")

        choice = int(input("Please enter the choice of the dessert you choose: "))
        global bill_dessert  # Use global variable
        if choice == 1:
            print("Chocolate Cake")
            selected_desserts.append("Chocolate Cake")
            bill_dessert = 6.99
        elif choice == "2":
            print("Apple Pie")
            bill_dessert = 5.99
        elif choice == "3":
            print("Ice Cream Sundae")
            bill_dessert = 4.99
        elif choice == "4":
            print("Cheesecake")
            bill_dessert = 7.99
        elif choice == "5":
            print("Brownie")
            bill_dessert = 4.99
        elif choice == "6":
            print("Tiramisu")
            bill_dessert = 8.99
        elif choice == "7":
            print("Fruit Tart")
            bill_dessert = 6.99
        elif choice == "8":
            print("Panna Cotta")
            bill_dessert = 5.99
        elif choice == "9":
            print("Creme Brulee")
            bill_dessert = 7.99
        elif choice == "10":
            print("Churros")
            bill_dessert = 4.99
        else:
            print("Invalid choice!")
        course_choice = input("You want to select more?  yes/no :")
        if course_choice == "yes":
            print(object4.desert())
        if course_choice == "no":
            print("OK")
        drinks_choice = input(("\nNow you want to see your bill  yes/no"))
        if drinks_choice == "yes":
            print(object5.bill())
        if drinks_choice == "no":
            print(object1.print_name())


class Bill(Name):
    def __init__(self, name, menu):
        super().__init__(name)
        self.menu = menu

    def bill(self):
        total_bill = bill_starter + bill_main_course + bill_drinks + bill_dessert

    print("__________________Taste Junction________________|")
    print("|----------------------------------------------|")
    print("_______________  Your BILL ____________________|")
    print("|----------------------------------------------|")
    # Display selected items in each category
    print("| Starters      >>>>>> ",selected_starters)
    print("| Main Course  >>>>>> ",selected_main_courses)
    print("| Drinks  >>>>>",selected_drinks)
    print("| Desserts >>>>>>>>>>",selected_desserts)
    print("|----------------------------------------------|")
    print("| Total: $", total_bill)
    print("|----------------------------------------------|")
    print("|----------------------------------------------|")
    print("|----------------------------------------------|")


name = "****************************** \n*       Taste Junction       *\n******************************"
menu = "Menu of the Restaurant"

object1 = Main_Course(name, menu)
object2 = Menu(name, menu)
object3 = Drinks(name, menu)
object4 = Deserts(name, menu)
object5 = Bill(name, menu)

object1.print_name()

while True:
    print("Press\n1. For See Starter\n2. For See Main Course\n3. For see Drinks\n4. For see Dessert\n0. To Exit")
    menu_choice = int(input("Enter your choice here: "))

    if menu_choice == 1:
        object2.starter()
    elif menu_choice == 2:
        object1.main_course()
    elif menu_choice == 3:
        object3.drinks()
    elif menu_choice == 4:
        object4.desert()
    elif menu_choice == 0:
        break
    else:
        print("Invalid choice!")
    

