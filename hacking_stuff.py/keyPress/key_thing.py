import keyboard
import threading
import time

# Run with:
# sudo ./venv/bin/python key_thing.py

running = False
program_open = True

# Text to type
start_key_sequence =[
    "ctrl+alt+t",
]

key_sequence = [
    #"ctrl+alt+t",
    #"l","s",
    #"enter",
    "t","o","u","c","h"," ", "t","e","s","t","1",
    "enter",
    "n","v","i","m"," ","t","e","s","t","1",
    "enter",
    "e",
    "i",
    "y","o","u"," ","a","r","e"," ","b","a","i","n","g"," ","h","a","c","k","e","d",
    "esc",
    "shift+;",
    "w","q",
    "enter",
    "c","a","t"," ","t","e","s","t","1",
    "enter",

    
]

def automation():
    global running

    while program_open:

        if running:

            print("Typing started...\n")
            
            for key in start_key_sequence:

                if not running or not program_open:
                    break

                print(f"Typing: {key}")

                keyboard.press_and_release(key)

                # Delay between keys
                time.sleep(1)

            # Run through sequence ONCE
            for key in key_sequence:

                if not running or not program_open:
                    break

                print(f"Typing: {key}")

                keyboard.press_and_release(key)

                # Delay between keys
                time.sleep(0.05)

            running = False
            print("\nSequence complete")

        else:
            time.sleep(0.01)

# Start background thread
threading.Thread(target=automation, daemon=True).start()

print("Controls:")
print(" -=- = START")
print("F7    = STOP")
print("ESC   = EXIT")

while program_open:

    # START
    if keyboard.is_pressed("="):

        if not running:
            running = True
            print("STARTED")

        time.sleep(0.5)

    # STOP
    if keyboard.is_pressed("f7"):

        running = False
        print("STOPPED")

        time.sleep(0.5)

    # EXIT
    if keyboard.is_pressed("esc"):

        running = False
        program_open = False

        print("EXITING")
        break

    time.sleep(0.05)

print("Program closed")