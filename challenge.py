# def sent():
#     sentence=input("Write a sentence: ")
#     broken=sentence.split()
#     print(len(broken))

# sent()

# def num():
#     number=input("Write a number: ")
#     if int(number) % 2:
#         print("This number is odd")
#     else:
#         print("This number is even")

# num()

# def bill():
#     service=input("Was the service good, bad, okay, or great?: ")
#     if service == ("good"):
#         print("Pay a tip of 20%")
#     elif service == ("bad"):
#         print("Pay a tip of 0%")
#     elif service == ("okay"):
#         print("Pay a tip of 15%")
#     elif service == ("great"):
#         print("Pay a tip of 25%")

# bill()

# def factors(): 
#     number = int(input ("Please write a number: "))
#     for i in range(1,number+1):
#         if number % i == 0:
#             print(i)
    
# factors()

def gcf ():
    number1 = int(input ("Write a number: "))
    number2 = int (input ("Write another number: "))
    for i in range (1, number1 + 1):
        x=number1 % i
    for i in range (1, number2 + 1):
        y=number2 % i 
        if x == y:
            print (x and y)
gcf()