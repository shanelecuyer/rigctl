import keyboard
import time

keys = 'abdefghijklmnopqrstuvwxyz'
#keys = keys.split()

try:
    while True:
        key = keyboard.read_key()
        #if not key == "c":
        if key in keys: 
            print("You pressed", key)
        time.sleep(0.1)

except KeyboardInterrupt:
    quit()

#while True:
#    if keyboard.is_pressed("q"):
#        print("You pressed q")
#        break
        
#keyboard.on_press_key("r", lambda _:print("You pressed r"))
