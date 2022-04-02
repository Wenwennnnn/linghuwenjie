isRunning = True
while isRunning:
    message = input("Please enter any character")
    if message == 'q':
        isRunning = False
        print("Enter the letter 'q', isrunning from ture to false, and the program exits")
    elif message =='Q':
        break
        print("Enter 'Q' to exit the program, isRunning remains true")
    else:
        print("To continue, type Q or q to exit the program")
