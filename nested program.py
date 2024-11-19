# clothes sugggestion:
     
cloth_type1="western"
cloth_type2="desi"
fabric_1="silk"
fabric_2="cotton"

while True:
    cloth=input("Which type of cloth you want to wear?(western/desi)").lower()
    fabric=input("Which type of fabric you want to wear?(silk/cotton)").lower()
    if cloth==cloth_type1 or cloth==cloth_type2 and fabric==fabric_1 or fabric==fabric_2:
        if cloth==cloth_type1 and fabric==fabric_1:
            choice1=input("What category you want in western silk:(dresses/suits/coats)").lower()
            if choice1=="dresses":
                print("we have wide range of dresses in silk fabric")
                break
            elif choice1=="suits":
                print("We have wide range of ready suits but we can also make it on your own choice")
                break
            elif choice1=="coats":
                print("We have multiple colors in coats.")
                break
            else:
                print("Out of order")
                break
        elif cloth==cloth_type1 and fabric==fabric_2:
            choice2=input("What category you want in western cotton:(levis pants/denim jeans/shirts)").lower()
            if choice2=="levis pants":
                print("Your choice is good")
                break
            elif choice2=="denim jeans":
                print("That's the most famous brand.Good Choice Budddy")
                break
            elif choice2=="shirts":
                print("It is also good choice")
                break
            else:
                print("You may try something Desi")
                question=input("Do you want to try desi clothes:(yes/no)").lower()
                if question=="yes":
                    continue
                else:
                    print("Thank you")
                    break
        elif cloth==cloth_type2 and fabric==fabric_1:
            choice3=input("which type of clothes you want in desi silk:(sherwani/kurta/waistcoat)").lower()
            if choice3=="sherwani":
                print("Off white Sherwani will suit you.")
                break
            elif choice3=="kurta":
                print("you should try some light colours.")
                break
            elif choice3=="waistcoat":
                print("Your waistcoat must match your clothes")
                break
            else:
                print("You should try cotton fabric.")
                break
        elif cloth==cloth_type2 and fabric==fabric_2:
            choice4=input("Which type of clothes you want in fabric:(shalwar kameez/coat/kurta)").lower()
            if choice4=="shalwar kameez":
                print("You should buy unstitched clothes for your satisfaction")
                break
            elif choice4=="coat":
                print("match your coat with your clothes")
                break
            elif choice4=="kurta":
                print("Good Choice")
                break
            else:
                print("We don't have much varieties then.")
                break
    else:
        print("We don't have your choice")
        break
            
                    
                        