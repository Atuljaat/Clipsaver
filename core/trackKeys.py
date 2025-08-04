import pyperclip
import keyboard
import threading
import time
# from clipboard import clipboard

class keyboardListener :
    def __init__(self , clipboard):
        keyboard.add_hotkey('ctrl+c',self.copyClipboard)
        self.myClipboard = clipboard
        self.thread = threading.Thread(target=self.start,daemon=True)
        self.thread.start()
    
    def copyClipboard (self) :
        time.sleep(0.1)
        currentData = pyperclip.paste()
        self.myClipboard.enterData(currentData)
            
    def start (self) :
        keyboard.wait()


# d = keyboardListener()
# d.start()