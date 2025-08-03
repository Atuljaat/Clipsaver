from utils.editJson import editJson
from core.clipboard import clipboard
import os
import time
from core.trackKeys import keyboardListener

path = os.path.join('.','data','clipboard.json')

# mydata = {
#     "time" : time.localtime(),
#     "text" : 'hello'
# }

jsonObj = editJson(path)
clipboardObj = clipboard(jsonObj)
d = keyboardListener(clipboardObj)
d.start()
# clipboardObj.enterData(mydata)