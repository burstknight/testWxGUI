import wx
from myFrame.myWxFrame import myWxFrame

class myFrame(myWxFrame):
    def __init__(self):
        super().__init__(None)
    # End of constructor

    def __close(self):
        self.Destroy()
    # End of myFrame::close

    def handleOnClose(self, event):
        self.__close()
    # End of myFrame::handeOnClose
    
    def handleOnUpdateUI(self, event):
        pass
    # End of myFrame
# End of class myFrame