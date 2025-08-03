# from utils.editJson import editJson
import os
import time

class clipboard :
    def __init__( self , editJson ) :
        self.editJson = editJson
    
    def enterData (self,data) :
        newData = self.editJson.readJson()
        
        singleClip = {
            'time' : time.localtime()  ,
            'text' : data ,
            'isPinned' : False
        }
        # print('old data : ' , newData)
        newData['count'] += 1
        newData['data'].append(singleClip)
        self.editJson.writeInJson(newData)
    
    def clearAll (self) :
        newData = self.editJson.readJson()
        newData['count'] = 0
        newData['data'] = []
        self.editJson.writeInJson(newData)
    
    def deleteOne ( self , id ) :
        newData = self.editJson.readJson()
        newData['count'] -= 1
        newData['data'] = [data for data in newData['data'] if data['id'] != id]
        self.editJson.writeInJson(newData)
    
    def togglePin ( self , id ) :
        newData = self.editJson.readJson()
        for data in newData['data'] :
            if data['id'] == id :
                data['isPinned'] = not data['isPinned']
                break
        self.editJson.writeInJson(newData)


# filePath = os.path.join('data','clipboard')
# print(filePath)