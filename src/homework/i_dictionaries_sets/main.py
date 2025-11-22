from dictionary import add_inventory, remove_inventory_widget

def main():
    inventory = {}
    
    while True:
        print("\nInventory Menu")
        print("1-Add or Update Item")
        print("2-Delete Item")
        print("3-Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            widget_name = input("Enter widget name: ")
            quantity = int(input("Enter quantity: "))
            add_inventory(inventory, widget_name, quantity)
        elif choice == "2":
            widget_name = input("Enter widget name to remove: ")
            remove_inventory_widget(inventory, widget_name)
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()