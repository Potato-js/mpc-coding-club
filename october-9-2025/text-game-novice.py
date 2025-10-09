while True:
    print("You wake up in a room, what do you do?")
    print("(Exit the room/Look Around)")
    answer = input("> ")

    if answer.lower() == "exit the room":
        print("Hey look you exited")
        break
    elif answer.lower() == "look around":
        print("There is nothing around you other than a bed")
        answer = input(">")
    else:
        print("Enter a vaild option")
        answer = input(">")
