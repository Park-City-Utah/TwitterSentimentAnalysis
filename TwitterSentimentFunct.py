def remove_all_values(myList, valueForRemoval):
    while(valueForRemoval in myList):
        myList.remove(valueForRemoval)
    return myList