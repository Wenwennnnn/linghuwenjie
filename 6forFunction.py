isRunning = True
while  isRunning:
    temp = input("Input conversion temperature")
    C = int(temp)
    F = C*1.8+32
    print("degree centigrade ："+str(C)+"℃ = Fahrenheit degree："+str(F)+"F")
    message = input("Type Q to exit the program and enter another program to continue")
    if message == 'Q':
        isRunning = False
        print("Program exits")
