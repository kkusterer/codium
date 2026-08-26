import keyboard
import threading
import time

# Run with:
# sudo ./venv/bin/python key_thing.py

running = False
program_open = True

# Text to type
key_sequence = [
    "w","e",","," ","t","h","e"," ","p","e","o","p","l","e"," ",
    "o","f"," ","t","h","e"," ","u","n","i","t","e","d"," ",
    "s","t","a","t","e","s",","," ","i","n"," ","o","r","d",
    "e","r"," ","t","o"," ","f","o","r","m"," ","a"," ","m",
    "o","r","e"," ","p","e","r","f","e","c","t"," ","u","n",
    "i","o","n",","," ","e","s","t","a","b","l","i","s","h"," ",
    "j","u","s","t","i","c","e",","," ","i","n","s","u","r","e"," ",
    "d","o","m","e","s","t","i","c"," ","t","r","a","n","q","u",
    "i","l","i","t","y",","," ","p","r","o","v","i","d","e"," ",
    "f","o","r"," ","t","h","e"," ","c","o","m","m","o","n"," ",
    "d","e","f","e","n","s","e",","," ","p","r","o","m","o","t",
    "e"," ","t","h","e"," ","g","e","n","e","r","a","l"," ",
    "w","e","l","f","a","r","e",","," ","a","n","d"," ","s","e",
    "c","u","r","e"," ","t","h","e"," ","b","l","e","s","s","i",
    "n","g","s"," ","o","f"," ","l","i","b","e","r","t","y"," ",
    "t","o"," ","o","u","r","s","e","l","v","e","s"," ","a","n",
    "d"," ","o","u","r"," ","p","o","s","t","e","r","i","t","y",
    ","," ","d","o"," ","o","r","d","a","i","n"," ","a","n","d",
    " ","e","s","t","a","b","l","i","s","h"," ","t","h","i","s",
    " ","c","o","n","s","t","i","t","u","t","i","o","n"," ","f",
    "o","r"," ","t","h","e"," ","u","n","i","t","e","d"," ",
    "s","t","a","t","e","s"," ","o","f"," ","a","m","e","r","i",
    "c","a","."
]

def automation():
    global running

    while program_open:

        if running:

            print("Typing started...\n")

            # Run through sequence ONCE
            for key in key_sequence:

                if not running or not program_open:
                    break

                print(f"Typing: {key}")

                keyboard.write(key)

                # Delay between keys
                time.sleep(0.03)

            running = False
            print("\nSequence complete")

        else:
            time.sleep(0.01)

# Start background thread
threading.Thread(target=automation, daemon=True).start()

print("Controls:")
print("ENTER = START")
print("F7    = STOP")
print("ESC   = EXIT")

while program_open:

    # START
    if keyboard.is_pressed("enter"):

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