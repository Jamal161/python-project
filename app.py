command = ""
while command != "quit":
    command = input(">").lower()
    if command == "start":
        print("Car started...")
    elif command =="stop":
        print("Car stopped.")
    elif command == "help":
        print("""
               start- to the car
               stop-to stop the car
               quit-to quit
               """)
    else:
          print("sorry ! i don't understand that")
