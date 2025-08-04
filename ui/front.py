from tkinter import *
import pyperclip

class myUI :
    
    def __init__(self , clipboardArray ):
        self.window = Tk()
        self.window.title('ClipSaver')
        self.window.geometry('300x400')
        self.setupUi(clipboardArray)
    
    def setupUi (self , clipboardArray ) :
        Label(self.window,text="Clipboard",pady=25,font=("Arial",20,"bold")).pack()
        self.showClipboard(clipboardArray)
        
    def start (self) :
        self.window.mainloop()
    
    def copyText (self,myText) :
        pyperclip.copy(myText)
        print('printed the text : ' , myText)
    
    def copyButton (self,myText,window) :
        Button(window,text="Copy Text",command=lambda:self.copyText(myText)).pack()
    
    def deleteText (self,frame:Frame):
        frame.destroy()
    
    def deleteButton (self , frame , window) :
        Button(window,text="Delete Text",command=lambda:self.deleteText(frame)).pack()
    
    #  singleClip = {
    #         'time' : time.localtime()  ,
    #         'text' : data ,
    #         'isPinned' : False
    # }
    
    
    def showClipboard (self,clipboardArray) :
        for copyItem in clipboardArray :
            myFrame = Frame(self.window)
            myFrame.pack(pady=5)
            myLabel = Label(myFrame,text=copyItem['text'])
            myLabel.pack()
            self.copyButton(myText=copyItem['text'],window=myFrame)
            self.deleteButton(frame=myFrame,window=myFrame)

