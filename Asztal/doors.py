#Creates a list with 100 elements. Default value is 0 (closed door).
list = [0] * 100

#For loop from 1 to 101 for rounds. In each round it checks the index.
#If the  remainder is 0 then it changes to door's value (open-close)
for korszam in range(1,101):  
    for index, lista_elem in enumerate(list):  
        if((index+1) % korszam == 0):
            if(lista_elem == 0):
                list[index] = 1
            elif(lista_elem == 1):
                list[index] = 0

#Printing the open doors:
print("The following doors are open: ", end="")
#If the door is open (1), then print its number
for index, lista_elem in enumerate(list):
    if(lista_elem == 1):
        print(index+1, end=", ")

#Just a linebreak
print()           