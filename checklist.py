import os

checklist = []

# List of functions:

# Create function
def create(item):
    if not item:
        print("Error: Item cannot be empty.")
        return
    checklist.append(item)

# Read function
def read(index):
    try:
        return checklist[index]
    except IndexError:
        return "Error: Invalid index."

# Update function
def update(index, item):
    try:
        if not item:
            print("Error: Item cannot be empty.")
            return
        checklist[index] = item
    except IndexError:
        print("Error: Invalid index.")

# Destroy function
def destroy(index):
    try:
        checklist.pop(index)
    except IndexError:
        print("Error: Invalid index.")

# List all items along with their index

def list_all_items():
    if not checklist:
        print("The list is empty.")
        return
    index = 0
    for list_item in checklist:
        print(f"{index} {list_item}")
        index += 1

# mark_completed
def mark_completed(index):
    try:
        checklist[index] = f"√ {checklist[index]}"
    except IndexError:
        print("Error: Invalid index.")

# User input function
def user_input(prompt):
    return input(prompt)

# function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to receive input from user
def select(function_code):
    function_code = function_code.upper()
    if function_code == "C":
        create(input("Enter the item: "))
    elif function_code == "R":
        index = int(input("Which index to read? "))
        print(read(index))
    elif function_code == "P":
        list_all_items()
    elif function_code == "Q":
        return False
    else:
        print("Unknown option was chosen.")
    return True

# Test function to validate the CRUD operations
def test():
    # Test Create
    create("purple sox")
    create("red cloak")
    # print("After create:", checklist)
    
    # Test Read
    print("Read index 0:", read(0))
    print("Read index 1:", read(1))
    
    # Test Update
    update(0, "purple socks")
    print("After update:", checklist)
    
    # Test Destroy
    destroy(1)
    print("After destroy:", checklist)

    # Test List All Items
    list_all_items()

    # Test mark as completed
    mark_completed(0)
    list_all_items()

# Test the function to validate CRUD process
test()

# Entire program loop
running = True
while running:
    clear_screen()
    selection = user_input("Press C to add to list, R to read from list, P to display the list, and Q to quit: ")
    running = select(selection)