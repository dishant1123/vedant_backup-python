# nested match : 

print("WELCOME TO MY SHOP")
print("1.FRIUTS")
print("2.VEGETABLES")

choice =int(input("ENTER YOUR CHOICE : "))
match choice :
    case 1 : 
        print("FRUITS ARE :") 
        print("1.APPLE RS :150 ")
        print("2.BANANA RS :50 ")
        print("3.ORANGE RS :100")
        subchoice =int(input("enter the subchoice : "))
        match subchoice :
            case 1:
                print("you selected apple")
                qty =int(input("ENTER THE QUANTITY : "))
                price =150 
                total = qty * price
                print("TOTAL AMOUNT :",total)
            case 2:
                print("you selected banana")
                qty =int(input("ENTER THE QUANTITY : "))
                price =50 
                total = qty * price
                print("TOTAL AMOUNT :",total)
            case 3:
                print("you selected orange")
                qty =int(input("ENTER THE QUANTITY : "))
                price =100 
                total = qty * price
                print("TOTAL AMOUNT :",total)
    case 2 :
        print("VEGETABLES ARE :")
        print("1.CARROT RS :50 ")
        print("2.POTATO RS :60 ")
        print("3.ONION RS :40 ")
        subchoice =int(input("enter the subchoice : "))
        match subchoice :
            case 1 :
                print("you selected carrot")
                qty =int(input("ENTER THE QUANTITY : "))
                price= 50 
                total = qty * price
                print("TOTAL AMOUNT :",total)
            case 2 :
                print("you selected potato")
                qty =int(input("ENTER THE QUANTITY : "))
                price= 60 
                total = qty * price
                print("TOTAL AMOUNT :",total)
            case 3 :
                print("you selected onion")
                qty =int(input("ENTER THE QUANTITY : "))
                price= 40
                total = qty * price
                print("TOTAL AMOUNT :",total)
    case _ :
        print("INVALID CHOICE")
        

        