# Initialize an empty list called checklist
checklist = []

# List of functions:

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

# List all items along with their index

def list_all_items():
    index = 0
    for list_item in checklist:
        print(f"{index} {list_item}")
        index += 1

# mark_completed
def mark_completed(index):
    checklist[index] = f"√ {checklist[index]}"

# User input function
def user_input(prompt):
    return input(prompt)

# Function to receive input from user
def select(function_code):
    if function_code == "C":
        create (input("Enter the item: "))
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
    selection = user_input("Press C to add to list, R to read from list, P to display the list, and Q to quit: ")
    running = select(selection)