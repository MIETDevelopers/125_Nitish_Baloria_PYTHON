#Linear searh in python
myList = [1,2,3,4,5,6,7,8,9]
value = input("Enter the value:")
value = int(value)
for i in range(0, len(myList)):
    if myList[i] == value:
        print("Item found at : ",i )
        break
if myList[i] != value:
    print("Element not present in the list")
        

