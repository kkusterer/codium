from pynput import keyboard
import time

# Store press times
pressed_keys = {}

def on_press(key):
    try:
        key_name = key.char
    except AttributeError:
        key_name = str(key)

    # Only record first press
    if key_name not in pressed_keys:
        pressed_keys[key_name] = time.time()
        print(f"{key_name} pressed")

def on_release(key):
    try:
        key_name = key.char
    except AttributeError:
        key_name = str(key)

    if key_name in pressed_keys:
        held_time = time.time() - pressed_keys[key_name]
        print(f"Held for: {held_time:.2f} seconds\n")

        del pressed_keys[key_name]

    # ESC quits
    if key == keyboard.Key.esc:
        print("Exiting...")
        return False

print("Keyboard monitor started")
print("Press ESC to quit\n")

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()