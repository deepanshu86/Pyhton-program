while True:
    print("Main Menu")
    print("1.Simple Calculator")
    print("2.Area finder calculator")
    print("3.Volume finder calculator ")
    print("4.exit")
    user=int(input("Please choose your option :- "))
    if user==1:
        print("a.ADD")
        print("b.SUBTRACT")
        print("c.MULTIPLY")
        print("d.DIVIDE")
        user=input("Please choose your option :- ")
    if (user=="a"):
        user1=int(input("Please enter your first value:- "))
        user2=int(input("Please enter your second value:- "))
        print("The sum is:-",user1+user2)
        user=input("Please choose your option :- ")
    if (user=="b"):
        user1=int(input("Please enter your first value:-  "))
        user2=int(input("Please enter your second value:- "))
        print("The sum is :-  ",user1-user2)
        user=input("Please choose your option :- ")
    if (user=="c"):
        user1=int(input("Please enter your first value:-  "))
        user2=int(input("Please enter your second value:-  "))
        print("The sum is :- ",user1*user2)
        user=input("Please choose your option :- ")
    if (user=="d"):
        user1=int(input("Please enter your first value:-  "))
        user2=int(input("Please enter your second value:-  "))
        print("The sum is :- ",user1/user2)
        user=input("Please choose your option :- ")
    if  user==2:
        print("a.Area of rectangle")
        print("b.Area of circle")
        print("c.Area of square")
        print("d.Area of triangle ")
        user=input("Please choose your option :- ")
    if (user=="a"):
        user1=float(input("Please enter length value:-  "))
        user2=float(input("Please enter  breadth value:-  "))
        print("The area is :- ", user1*user2)
        user=input("Please choose your option :- ")
    if (user=="b"):
        user1=float(input("Please enter radius value:-  "))
        print("The area is :- ",3.14*user1**2)
        user=input("Please choose your option :- ")
    if (user=="c"):
        user1=float(input("Please enter side value:-  "))
        print("The area is :- ", user1**2)
        user=input("Please choose your option :- ")
    if (user=="d"):
        user1=float(input("Please enter length value:-  "))
        user2=float(input("Please enter  breadth value:-  "))
        user3=float(input("Please enter  height value:-  "))
        print("The area is :- ", 1/2*user1*user2*user3)
        user=input("Please choose your option :- ")
    if  user==3:
        print("a.Volume  of sphere")
        print("b.volume of cylinder")
        print("c.Volume  of cone ")
    if (user=="a"):
        user1=float(input("Please enter side value:-  "))
        print("The volume is :- ",user1)
