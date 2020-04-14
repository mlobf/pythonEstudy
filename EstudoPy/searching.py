shopping_list =["milk","pasta","eggs","spam","bread","rice"]

itenstofind = "spam"

found = None

for index in range(len(shopping_list)):
    if shopping_list[index] == itenstofind:
        found = index
        break

if found is not None:
    print("Item found at position {}".format(found))
else:
    print("{} not found".format(itenstofind))










