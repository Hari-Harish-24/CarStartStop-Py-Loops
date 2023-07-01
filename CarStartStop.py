def run():
    command = True
    check1 = False
    while command:
        command = input("-> ").lower()
        if command == "start":
            if check1:
                print("The car is alrady started :( ")
            else:
                print("The car is started !!")
                check1 = True
        elif command == "stop":
            if check1:
                print("The car is stoped !!")
                check1 = False
            else:
                print("Start the car to stop :( , it's stop !!")
        elif command == "quit":
            command = False
        elif command == "help":
            print("""
    Start - to start the car
    Stop - to stop the car
    quit - to stop the Program
    help - to get info
            """)
        else:
            print("Invalid Command !?") 

run()           