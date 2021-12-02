import wx
import time
from myFrame.myWxFrame import myWxFrame
from myObserverPattern import myInfoObserver, myInfo
from myModel import myModel

class myFrame(myWxFrame, myInfoObserver):
    def __init__(self, oModel:myModel):
        myWxFrame.__init__(self, None)
        myInfoObserver.__init__(self)

        self.__m_oModel = oModel

        self.__m_vstrMessage = []
    # End of constructor

    def __close(self):
        self.__m_oModel.isRun = False
        time.sleep(1)
        self.Destroy()
    # End of myFrame::close

    def handleOnClose(self, event):
        self.__close()
    # End of myFrame::handeOnClose
    
    def handleOnUpdateUI(self, event):
        pass
    # End of myFrame

    def update(self, key: str, oInfo: myInfo):
        if "Message" == key:
            strMessage = oInfo.getParam(key)
            self.__m_vstrMessage.append(strMessage)
            if len(self.__m_vstrMessage) > 12:
                self.__m_vstrMessage.pop(0)
            # End of if-condition

            strText = ""
            for i in range(len(self.__m_vstrMessage)):
                strText += self.__m_vstrMessage[i]
            # End of for-loop
        elif "Event" == key:
            strMessage = oInfo.getParam(key)
            wx.MessageBox(strMessage, "Test")
        # End of if-condition
    # End of myFrame::update
# End of class myFrame