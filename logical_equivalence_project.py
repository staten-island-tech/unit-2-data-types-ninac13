y = ("Yes") 
y = True
x = ("No")
x = False
snow = input ("Is it snowing outside? ")

def truth_table (x,y):
    if  x != y:
        input("You should shovel. Do you have a shovel? ")
    elif x == y:
        print("Don't shovel")
truth_table (x,y)

