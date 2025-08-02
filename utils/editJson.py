import json
# import os

class editJson () :
    def __init__(self,filePath):
        self.filePath = filePath
    
    def readJson (self):
        with open(self.filePath,'r') as file :
            data = json.load(file)
        return data
    
    def editJsonProperty (self,property,newValue) :
        with open(self.filePath,'r') as file :
            data = json.load(file)
            data[property] = newValue
            
        with open(self.filePath,'w') as file:
            json.dump(data,file,indent=4)
            return True
    
    def getJsonProperty (self,property) :
        with open(self.filePath,'r') as file :
            data = json.load(file)
            return data[property]
    
    def writeInJson (self,data) :
        with open(self.filePath,'w') as file :
            json.dump(data,file,indent=4)

# filepath = 'data\clipboard'
# d = editJson('/data/clipboard.json')
# print(d.readJson())


# import os
# currentFile = os.path.abspath(__file__)
# parentDir = os.path.dirname(currentFile)
# grandParentDir = os.path.dirname(parentDir)
# full = os.path.join(grandParentDir,'data','clipboard.json')

# d = editJson(full)
# print(d.readJson())
