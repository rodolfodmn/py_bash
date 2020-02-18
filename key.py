import keyboard

text_to_print='default_predefined_text'
shortcut = 'alt+x' #define your hot-key
shortcut_move_change = 'alt+q' #define your hot-key
print('Hotkey set as:', shortcut)
print('Hotkey move change set as:', shortcut_move_change)

def on_triggered(): #define your function to be executed on hot-key press
    print(text_to_print)

def change_move():
    print('change to wsd')
    
    keyboard.remap_key('w', 'up')
    keyboard.remap_key('s', 'down')
    keyboard.remap_key('d', 'right')
    keyboard.remap_key('a', 'left')

keyboard.add_hotkey(shortcut_move_change, change_move) #<-- attach the function to hot-key
keyboard.add_hotkey(shortcut, on_triggered) #<-- attach the function to hot-key

print("Press ESC to stop.")
keyboard.wait('esc')