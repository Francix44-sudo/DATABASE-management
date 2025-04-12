#A function to perform the neccesary actions on the database, based on the input from the user, taken as an 
#argument

#import the sqlite module to make the necessary CRUD actions
import sqlite3

def decision_maker(choice_made):
    try:
        # Make a connection to the database
        connection = sqlite3.connect("shopquery.db")
        cursor = connection.cursor()

        if choice_made == 1:
            print("Please enter the information about the new item:")
            new_item_name = input("Enter the name of the new item: ").strip()

            # Check if the new item is already available in the database
            cursor.execute('''SELECT Item FROM ShopItems WHERE Item = ?''', (new_item_name,))
            data_fetched = cursor.fetchall()

            if data_fetched:
                print("Sorry, the item already exists in the database. Try updating the price or stock.")
            else:
                try:
                    new_item_price = float(input("Enter the price of the new item: "))
                    new_item_stock = int(input("Enter the stock of the new item: "))

                    # Insert the new item into the database
                    cursor.execute('''INSERT INTO ShopItems (Item, Price, Stock) VALUES (?, ?, ?)''',
                                   (new_item_name, new_item_price, new_item_stock))
                    connection.commit()
                    print("Great! Your new item has been saved successfully to the database.")
                except ValueError:
                    print("Invalid input. Please enter numeric values for price and stock.")

        elif choice_made == 2:
            item_to_search_name = input("Enter the name of the item you want to search for: ").strip()
            cursor.execute('''SELECT * FROM ShopItems WHERE Item LIKE ?''', (f"%{item_to_search_name}%",))
            data_fetched = cursor.fetchall()

            if not data_fetched:
                print("Sorry, no item matching the data you entered was found!")
            else:
                for row in data_fetched:
                    print(f"Item ID: {row[0]},\nItem Name: {row[1]},\nItem Price:\n{row[2]},\nItem Stock: {row[3]}")

        elif choice_made == 3:
            item_to_update = input("Please enter the name of the item you want to update: ").strip()
            cursor.execute('''SELECT Item FROM ShopItems WHERE Item = ?''', (item_to_update,))
            data_fetched = cursor.fetchall()

            if not data_fetched:
                print("No item matches the data you have entered!")
            else:
                try:
                    update_price = float(input(f"Enter the new price of {item_to_update}: "))
                    update_stock = int(input(f"Enter the new stock of {item_to_update}: "))
                    cursor.execute('''UPDATE ShopItems SET Price = ?, Stock = ? WHERE Item = ?''',
                                   (update_price, update_stock, item_to_update))
                    connection.commit()
                    print("The update has been successfully applied.")
                except ValueError:
                    print("Invalid input. Please enter numeric values for price and stock.")

        elif choice_made == 4:
            item_to_delete = input("Enter the item name to delete from the database: ").strip()
            cursor.execute('''SELECT Item FROM ShopItems WHERE Item = ?''', (item_to_delete,))
            data_fetched = cursor.fetchall()

            if not data_fetched:
                print("Sorry, no item was found in the database matching what you entered.")
            else:
                cursor.execute('''DELETE FROM ShopItems WHERE Item = ?''', (item_to_delete,))
                connection.commit()
                print(f"{item_to_delete} has been successfully deleted from the database.")

        else:
            print("Invalid choice. Please select a valid option.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        # Ensure the connection is closed
        if 'connection' in locals():
            connection.close()