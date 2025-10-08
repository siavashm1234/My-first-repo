car_status= "stopped"
while True:
    command=input("type your command or type help to see the commands")
    if command.lower() =="help":
     print(f'''stat-start the car
stop-stop the car
quit-quit the game
help-see commands''')
    elif command.lower() == f"start":
     if car_status== "stopped":
       print(f"car started")
       car_status = "started"
     else:
       print(f"car already started")
    elif command.lower() == f"stop":
        if car_status == "started":
         print(f"car stopped")
         car_status = "stopped"
        else:
         print(f"car already stopped")
    elif command.lower()== f"quit":
      print(f"good bye!")
      break
    else:
      print("can you say that again")