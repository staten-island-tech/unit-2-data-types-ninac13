def sent():
    sentence=input("Write a sentence: ")
    broken=sentence.split()
    print(len(broken))

sent()



def num():
    number=input("Write a number: ")
    if int(number) % 2:
        print("This number is odd")
    else:
        print("This number is even")

num()



def bill():
    service=input("Was the service good, bad, okay, or great?: ")
    if service == ("good"):
        print("Pay a tip of 20%")
    elif service == ("bad"):
        print("Pay a tip of 0%")
    elif service == ("okay"):
        print("Pay a tip of 15%")
    elif service == ("great"):
        print("Pay a tip of 25%")

bill()



def factors(): 
    number = int(input ("Please write a number: "))
    for i in range(1,number+1):
        if number % i == 0:
            print(i)
    
factors()



def gcf(num1, num2):
    if num1 > num2:
        num = num1
    else:
        num = num2
    for i in range (1, num + 1):
        if ((num1 % i == 0) and (num2 % i == 0)):
             gcd = i
    return gcd
firstnum = int(input("Write a number: "))
secondnum = int(input ("Write another number: "))

print (f"The GCF of {firstnum} and {secondnum} is: ", end="")
print (gcf(firstnum, secondnum))