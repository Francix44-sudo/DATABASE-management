#write a true loop to control the user input 

#import the decision module to make the decision  based from the user input
import decisions

while True:
    try:
        print("---------SHOP MANAGEMENT---------")
        print("1. Add new item\n2. Look up an item\n3. Make an update\n4. Delete an item\n5. Close app")
        print()
        choice = int(input("Please enter your choice: "))
        print("---------------------------------")

        if not choice:
            print("Please at least enter an input to do some operation!!!!!")
        elif choice < 1 or choice >5:
            print("Sorry please enter an input within the range of (1-5)")
        elif choice == 5:
            print("Great job done!...Have a nice day dude!")
            break
        else:
            decisions.decision_maker(choice)

    except Exception as err:
        print(f"Sorry, an error occured in your input: {err}")