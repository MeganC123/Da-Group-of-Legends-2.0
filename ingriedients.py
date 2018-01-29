while True:
    option=input("would you like to know the ingreidents to make something")
    if option=="yes":
            print("ok then ")
            print("what would you like to make?")
            choice=input("a.sponge cake b.toasted sandwhich c.omlette")
            if choice=="a":
                print("ok the ingriedents are")
                print( "butter")
                print("milk")
                print("eggs")
                print("flower(not in fridge)")
                print("baking powder(not in fridge)")
                print ("sugar(not in fridge)")
                break


            elif choice=="b":
                print("ok you need")
                print ("cheese")
                print("ham")
                print("butter")
                print("bread(not in fridge)")
                break

            elif choice=="c":
                print("alright you'll need")
                print("eggs")
                print("butter")
                print("milk OR water")
                print("black peeper(not kept in a fridge)")
                break



    elif option=="no":
            ("ok")
            break
