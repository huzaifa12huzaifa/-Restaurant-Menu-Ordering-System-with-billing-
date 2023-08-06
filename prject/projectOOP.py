
#Declare class name which is taking name and menu as a parameter
class name:
    def __init__(self,name,menu):
        self.name=name           #Taking name
        self.menu=menu           #Taking menu name

class Starter(name):
    def __init__(self,name,menu):         #(this is the starter class that takes name,menu as a input)
        super().__init__(name,menu)
        self.starter_bill = 0          #Variable to store the value
        self.starter_items = []      # an empty list to append the value
    def starter(self):
        print("1. Classic Caesar Salad ----------- $8.99")
        print("2. Crispy Fried Calamari --------- $10.99")
        print("3. Garlic Parmesan Wings ---------- $9.99")
        print("4. Bruschetta --------------------- $7.99")
        print("5. Spinach and Artichoke Dip ------ $8.99")   #(this is the starter option the user can use)
        print("6. Buffalo Chicken Sliders ------- $11.99")
        print("7. Loaded Potato Skins ------------ $9.99")
        print("8. Caprese Skewers ---------------- $8.99")
        print("9. Mini Quesadillas --------------- $7.99")
        print("10. Shrimp Cocktail -------------- $12.99")

        self.star_choice = str(input("Enter the number of the cuisine you want to order: "))
       #this is the starter choice that inputs a value
        if self.star_choice == "1":
            print("Classic Caesar Salad")           #user choice and add the item and amount in the bill
            self.starter_bill += 8.99
            self.starter_items.append("Classic Caesar Salad")
        elif self.star_choice == "2":
            print("Crispy Fried Calamari")
            self.starter_bill += 10.99
            self.starter_items.append("Crispy Fried Calamari")
        elif self.star_choice == "3":
            print("Garlic Parmesan Wings")
            self.starter_bill += 9.99
            self.starter_items.append("Garlic Parmesan Wings")
        elif self.star_choice == "4":
            print("Bruschetta")
            self.starter_bill += 7.99
            self.starter_items.append("Bruschetta")
        elif self.star_choice == "5":
            print("Spinach and Artichoke Dip")
            self.starter_bill += 8.99
            self.starter_items.append("Spinach and Artichoke Dip")
        elif self.star_choice == "6":
            print("Buffalo Chicken Sliders")
            self.starter_bill += 11.99
            self.starter_items.append("Buffalo Chicken Sliders")
        elif self.star_choice == "7":
            print("Loaded Potato Skins")
            self.starter_bill += 9.99
            self.starter_items.append("Loaded Potato Skins")
        elif self.star_choice == "8":
            print("Caprese Skewers")
            self.starter_bill += 8.99
            self.starter_items.append("Caprese Skewers")
        elif self.star_choice == "9":
            print("Mini Quesadillas")
            self.starter_bill += 7.99
            self.starter_items.append("Mini Quesadillas")
        elif self.star_choice == "10":
            print("Shrimp Cocktail")
            self.starter_bill += 12.99
            self.starter_items.append("Shrimp Cocktail")
        else:
            print("Invalid choice. Please enter a valid number from the menu.")
            obj1.starter()         #recall the function if user enter wrong choice

#Main course that is subclass of starter class
class Main_course(Starter):
    def __init__(self, name, menu):
        super().__init__(name, menu)
        self.main_course_bill = 0         #reset the price when user choose an item
        self.main_course_items = []       #append user choice
    def main_course(self):

        print("\t\tMain Course of the Restaurant")
        print("1. Grilled Chicken ------- $12.99")    #Main course of the resturent
        print("2. Beef Steak ------------ $16.99")
        print("3. Vegetarian Pasta ------ $10.99")
        print("4. Shrimp Scampi --------- $14.99")
        print("5. Margherita Pizza ------ $11.99")
        print("6. Salmon Fillet --------- $15.99")
        print("7. BBQ Ribs -------------- $17.99")
        print("8. Eggplant Parmesan ----- $10.99")
        print("9. Tandoori Chicken ------ $13.99")
        print("10. Sushi Platter -------- $18.99")

        self.main_choice = str(input("Enter the number of the main course you want to order: "))

        if self.main_choice == "1":
            print("Grilled Chicken")
            self.main_course_bill += 12.99          # the instance variables store the value of the bill
            self.main_course_items.append("Grilled Chicken")
        elif self.main_choice == "2":
            print("Beef Steak")
            self.main_course_bill += 16.99
            self.main_course_items.append("Beef Steak")
        elif self.main_choice == "3":
            print("Vegetarian Pasta")
            self.main_course_bill += 10.99
            self.main_course_items.append("Vegetarian Pasta")
        elif self.main_choice == "4":
            print("Shrimp Scampi")
            self.main_course_bill += 14.99
            self.main_course_items.append("Shrimp Scampi")
        elif self.main_choice == "5":
            print("Margherita Pizza")
            self.main_course_bill += 11.99
            self.main_course_items.append("Margherita Pizza")
        elif self.main_choice == "6":
            print("Salmon Fillet")
            self.main_course_bill += 15.99
            self.main_course_items.append("Salmon Fillet")
        elif self.main_choice == "7":
            print("BBQ Ribs")
            self.main_course_bill += 17.99
            self.main_course_items.append("BBQ Ribs")
        elif self.main_choice == "8":
            print("Eggplant Parmesan")
            self.main_course_bill += 10.99
            self.main_course_items.append("Eggplant Parmesan")
        elif self.main_choice == "9":
            print("Tandoori Chicken")
            self.main_course_bill += 13.99
            self.main_course_items.append("Tandoori Chicken")
        elif self.main_choice == "10":
            print("Sushi Platter")
            self.main_course_bill += 18.99
            self.main_course_items.append("Sushi Platter")
        else:
            print("Invalid choice. Please enter a valid number from the menu.")
            obj2.main_course()          #recall the function if user input invalid choice

#Drink class which is inherit with Main course
class Drinks(Main_course):
    def __init__(self, name, menu):
        super().__init__(name, menu)
        self.drinks_bill = 0
        self.drinks_items = []          #append the item in this empty list

    def drinks(self):
        print("1. Cola ---------------- $2.99")
        print("2. Lemonade ------------ $3.99")
        print("3. Iced Tea ------------ $2.99")
        print("4. Orange Juice -------- $3.99")
        print("5. Strawberry Smoothie - $4.99")                #Drinks which are available
        print("6. Mango Lassi --------- $3.99")
        print("7. Cappuccino ---------- $3.99")
        print("8. Hot Chocolate ------- $3.99")
        print("9. Bottled Water -------- $1.99")
        print("10. Sparkling Water ---- $2.99")

        self.drink_choice = str(input("Enter the number of the drink you want to order: "))

        if self.drink_choice == "1":
            print("Cola")
            self.drinks_bill += 2.99
            self.drinks_items.append("Cola")
        elif self.drink_choice == "2":
            print("Lemonade")
            self.drinks_bill += 3.99
            self.drinks_items.append("Lemonade")
        elif self.drink_choice == "3":
            print("Iced Tea")
            self.drinks_bill += 2.99
            self.drinks_items.append("Iced Tea")
        elif self.drink_choice == "4":
            print("Orange Juice")
            self.drinks_bill += 3.99
            self.drinks_items.append("Orange Juice")
        elif self.drink_choice == "5":
            print("Strawberry Smoothie")
            self.drinks_bill += 4.99
            self.drinks_items.append("Strawberry Smoothie")
        elif self.drink_choice == "6":
            print("Mango Lassi")
            self.drinks_bill += 3.99
            self.drinks_items.append("Mango Lassi")
        elif self.drink_choice == "7":
            print("Cappuccino")
            self.drinks_bill += 3.99
            self.drinks_items.append("Cappuccino")
        elif self.drink_choice == "8":
            print("Hot Chocolate")
            self.drinks_bill += 3.99
            self.drinks_items.append("Hot Chocolate")
        elif self.drink_choice == "9":
            print("Bottled Water")
            self.drinks_bill += 1.99
            self.drinks_items.append("Bottled Water")
        elif self.drink_choice == "10":
            print("Sparkling Water")
            self.drinks_bill += 2.99
            self.drinks_items.append("Sparkling Water")
        else:
            print("Invalid choice. Please enter a valid number from the menu.")
            obj3.drinks()
#Deserts class that inherit with Drinks class
class Desserts(Drinks):

    def __init__(self, name, menu):
        super().__init__(name, menu)
        self.desserts_bill = 0
        self.desserts_items = []            #empty list to store the item


    def desserts(self):
        print("Our Desserts, hope you like them!")
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

        self.dessert_choice = str(input("Enter the number of the dessert you want to order: "))

        if self.dessert_choice == "1":
            print("Chocolate Cake")
            self.desserts_bill += 6.99
            self.desserts_items.append("Chocolate Cake")          #append the item in the list
        elif self.dessert_choice == "2":
            print("Apple Pie")
            self.desserts_bill += 5.99
            self.desserts_items.append("Apple Pie")
        elif self.dessert_choice == "3":
            print("Ice Cream Sundae")
            self.desserts_bill += 4.99
            self.desserts_items.append("Ice Cream Sundae")
        elif self.dessert_choice == "4":
            print("Cheesecake")
            self.desserts_bill += 7.99
            self.desserts_items.append("Cheesecake")
        elif self.dessert_choice == "5":
            print("Brownie")
            self.desserts_bill += 4.99
            self.desserts_items.append("Brownie")
        elif self.dessert_choice == "6":
            print("Tiramisu")
            self.desserts_bill += 8.99
            self.desserts_items.append("Tiramisu")
        elif self.dessert_choice == "7":
            print("Fruit Tart")
            self.desserts_bill += 6.99
            self.desserts_items.append("Fruit Tart")
        elif self.dessert_choice == "8":
            print("Panna Cotta")
            self.desserts_bill += 5.99
            self.desserts_items.append("Panna Cotta")
        elif self.dessert_choice == "9":
            print("Creme Brulee")
            self.desserts_bill += 7.99
            self.desserts_items.append("Creme Brulee")
        elif self.dessert_choice == "10":
            print("Churros")
            self.desserts_bill += 4.99
            self.desserts_items.append("Churros")
        else:
            print("Invalid choice. Please enter a valid number from the menu.")
            obj4.desserts()


class Bill():
    def __init__(self, starter,main_course,drinks,desserts):
        self.starter = starter
        self.main_course = main_course
        self.drinks = drinks                      #instant variables that store classes
        self.desserts = desserts


                     #Bill function for print the bill........
    def bill(self):
        print("__________________Taste Junction________________|")
        print("|----------------------------------------------|")
        print("_______________  Your BILL ____________________|")
        print("|----------------------------------------------|")
        # Display selected items in each category
        print("| Starters      >>>>>> ", self.starter.starter_items)
        print("| Main Course   >>>>>> ", self.main_course.main_course_items)
        print("| Drinks        >>>>>> ", self.drinks.drinks_items)
        print("| Desserts      >>>>>> ", self.desserts.desserts_items)
        print("|----------------------------------------------|")
        print("| Total: $", (self.starter.starter_bill + self.main_course.main_course_bill + self.drinks.drinks_bill + self.desserts.desserts_bill))
        print("|----------------------------------------------|")
        print("|----------------------------------------------|")
        print("|----------------------------------------------|")




name="****************************** \n*   Taste Junction  *\n******************************"    #Name
print("Welcome to Taste Junction how can we help u!!!!")
menu="Menu of the Resturant"       #Menu
obj1=Starter(name,menu)        #For Starter class
obj2=Main_course(name,menu)    #For Main course class
obj3=Drinks(name,menu)         #For Drink class
obj4=Desserts(name,menu)       #For Desert class
obj5=Bill(obj1,obj2,obj3,obj4)
while(True):
    i=str(input("enter 1 to see the menu!!"))
    if i=="1":
        print("Press\n1.Starter\n2.Main Course\n3.Drinks\n4.Dessert\n5.Bill")
        m_choice=str(input("enter the number u wana select"))
        if m_choice=="1":
            obj1.starter()
        if m_choice=="2":
            obj2.main_course()
        if m_choice=="3":
            obj3.drinks()
        if m_choice=="4":
            obj4.desserts()
        if m_choice=="5":
            obj5.bill()

    else:
        print("invalid")


