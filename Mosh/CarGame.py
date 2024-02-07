flag = 0
while True:
    command = input('> ').lower()
    if command == 'help':
        print\
('''start - to start the car
stop - to stop the car
quit - to exit''')
    elif command == 'start':
        if flag == 5:
            print("Car is already started. Drive!")
        else:
            print("Car started... Ready to go!")
            flag = 5
    elif command == 'stop':
        if flag == 4:
            print("Car is already stopped. Can't Stop!")
        else:
            print('Car stopped.')
            flag = 4
    elif command == 'quit':
        break
    else:
        print("I don't understand that...")