from utils.editJson import editJson
from core.clipboard import clipboard
import os
import time
from core.trackKeys import keyboardListener
from ui.front import myUI

path = os.path.join('.','data','clipboard.json')

# mydata = {
#     "time" : time.localtime(),
#     "text" : 'hello'
# }

jsonObj = editJson(path)
clipboardObj = clipboard(jsonObj)
d = keyboardListener(clipboardObj)
jsonData = (jsonObj.readJson())['data']
print(jsonData)
myui = myUI(jsonData)
# d.start()
myui.start()
# clipboardObj.enterData(mydata)