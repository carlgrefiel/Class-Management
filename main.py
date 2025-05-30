from components.menu import showMenu, runFunction, pressEnterToContinue


while True:
    showMenu()
    try:
        selectMenu = int(input("\nPlease select and input number: ").strip())
        runFunction(selectMenu)
    except ValueError:
        print("Please enter a valid number.")
        pressEnterToContinue()
