# create a new empty list named shopping_list
shopping_list = []

def show_help():
    print("What should we pick up from the store?: ")
    print("""
    Enter "DONE" to stop adding items.
    Enter "HELP" for this help.
    Enter "SHOW" to see your list.
    """)
    
# create a function named add_to_list that declares a parameter named item
  # add the item to the list
def add_to_list(item):
    shopping_list.append(item)
    # notify the user that the item wa added and state the number of items on the list currently
    print(f"Added! List has {len(shopping_list)} items!")

# define a function named show_list that prints all the items int the list
def show_list():
    print("Here's your list: ")
    for item in shopping_list:
        print(item)

show_help()
while True:
    new_item  = input("> ")
  
    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
    elif new_item == "SHOW":
        show_list()
        continue
  
    # call add_to_list with new_item as an arguement
    add_to_list(new_item)
    
show_list()