# A really basic text adventure game

def prompt(options):
    # Ask until a valid choice is entered
    while True:
        choice = input("> ").strip().lower()
        if choice in options:
            return choice
        print(f"Type one of: {', '.join(options)}")

def intro():
    print("Wake up in a small room with a wooden door to the north and a dark tunnel to the east.")
    print("What now? (north/east/look)")
    choice = prompt({"north", "east", "look"})
    if choice == "north":
        hall()
    elif choice == "east":
        tunnel()
    else:
        print("The room is bare: a dusty cot, a flickering lamp, and footprints leading north.")
        return intro()

def hall():
    print("Enter a stone hall. A guard naps by a lever. There’s a locked gate to the north.")
    print("Actions? (sneak/lever/back)")
    choice = prompt({"sneak", "lever", "back"})
    if choice == "sneak":
        print("Tiptoe past and slip a key from the guard’s belt.")
        print("Use key on gate? (yes/no)")
        if prompt({"yes", "no"}) == "yes":
            exit_gate()
        else:
            return hall()
    elif choice == "lever":
        print("Pull the lever. The gate unlocks with a clang.")
        exit_gate()
    else:
        intro()

def tunnel():
    print("Crawl into a damp tunnel. It splits ahead.")
    print("Which way? (left/right/back)")
    choice = prompt({"left", "right", "back"})
    if choice == "left":
        print("Find a rusty dagger. Might be useful.")
        print("Return to the start. (press enter)")
        input()
        intro()
    elif choice == "right":
        print("A pit! Manage to grab a ledge and scramble back, shaken.")
        tunnel()
    else:
        intro()

def exit_gate():
    print("Push through the gate into sunlight. Freedom!")
    print("Play again? (yes/no)")
    if prompt({"yes", "no"}) == "yes":
        print()
        main()
    else:
        print("Thanks for playing!")

def main():
    print("=== Tiny Adventure ===")
    intro()

if __name__ == "__main__":
    main()
