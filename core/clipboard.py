# from ..utils.editJson import editJson
import os

class clipboard :
    def __init__( self , editJson , clipboardPath ) :
        self.editJson = editJson
        self.clipboardPath = clipboardPath()
    
    def enterData (self,data) :
        oldData = self.editJson.readJson()
        oldData['count'] += 1
        oldData['data'].append(data)
    
    

filePath = os.path.join('data','clipboard')
print(filePath)