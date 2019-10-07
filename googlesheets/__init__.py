__version__ = '0.1.0'
def printn():
    a = input("What would you like to print: ")
    print(a)

def helper():
    print("This is a list of commands")

    
#Include help in commands
commands = {"help":helper, "print":printn}

while True:

    print("What would you like to do?")
    userChoice = input().lower()
    print()

    #Takes commands and returns output if it is recognized, otherwise shows error prompt
    if userChoice in commands:
        #Call function
        print("Called {}".format(userChoice))
        commands[userChoice]()
        print("Command executed")
    elif userChoice == "exit":
        break

    else:
        print("Command not found, enter \"Help\" for a list of commands")

    print()

    #Exit prompt
    print("To exit, enter \"EXIT\", to enter another command, press ENTER")
    userChoice = input().lower()

    if userChoice == "exit":
        break
    elif userChoice == "HELP":
        print(commands)
    else:
        print("New instance")
        print()

