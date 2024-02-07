# ccode to start/stop/quit a car game

command = input(">")
while command.lower() != "quit":
    if command.lower() == "start":
        print("Car Started")
        command = input(">")
    elif command.lower() == "stop":
        print("Car Stopped")
        command = input(">")
    else:
        print("I don't understand that")
        command = input(">")