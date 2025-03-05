"""In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user 
inputs control-d. Then output the user's grocery list in all uppercase, sorted alphabetically by item, prefixing 
each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user's 
input case-insensitively."""

list = dict()
while True:
    try:
        item = input().upper()
    except EOFError:
        sorted_list = dict(sorted(list.items()))
        for x in sorted_list:
            print(sorted_list[x], x)
        break
    else:
        if item not in list:
            list[item] = 1
        else:
            list[item] += 1