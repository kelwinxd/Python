typing=" "
started=False


while True:
    typing=input("> ").lower()
    
    
   
    if typing=="start":
        if started:
             print("Your is already started")
        else:
            started=True
            print("starting your car")
        
       
    elif typing=="help":
        print("""
start - to start the car
stop - stop the car 
quit - quit program""")

        
    elif typing=="stop":
          if not started:
             print("Your is already stopped bitch")
          else:
            started=False
            print("Stopping the car")
    elif typing=="quit":
        print("quitting program....")
        break
