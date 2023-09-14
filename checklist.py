# checklist = list()
# print(checklist)

checklist = []

# say_this is a parameter or input
def my_fun_function(say_this):
    print(say_this)

my_fun_function("Hello World")

checklist = list()
checklist.append('Blue')
print(checklist)
checklist.append('Orange')
print(checklist)

#CREATE
def create(item):
    checklist.append(item)

checklist = ['Blue', 'Orange']
checklist[1] = 'Cats'
print(checklist)

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

checklist = ['Blue', 'Cats']
checklist.pop(1)
print(checklist)

# DESTROY
def destroy(index):
    checklist.pop(index)

# Initialize an empty list called checklist
checklist = []

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

# Test function to validate the CRUD operations
def test():
    # Test Create
    create("purple sox")
    create("red cloak")
    print("After create:", checklist)
    
    # Test Read
    print("Read index 0:", read(0))
    print("Read index 1:", read(1))
    
    # Test Update
    update(0, "purple socks")
    print("After update:", checklist)
    
    # Test Destroy
    destroy(1)
    print("After destroy:", checklist)

# Test the function to validate CRUD process
test()
