inventory = []
def add_item(item):
    inventory.append(item) 
    
def count_items(item):
    if not item:
        return 0
    else:
        return 1 + count_items(item[1:])
count_items(inventory)

def main():
    add_item("dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")
main()
print(inventory)