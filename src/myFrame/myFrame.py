from typing import overload
import wx
import time
from myFrame.myWxFrame import myWxFrame
from myObserverPattern import myInfoObserver, myInfo
from myModel import myModel

EVT_MSG_ID = wx.NewId()
EVT_UPDATE_DATA = wx.NewId()

class myMsgBoxEvent(wx.PyEvent):
    """
    This event is degined for show message box
    """
    def __init__(self, strMessage:str, iEventType:int = EVT_MSG_ID):
        wx.PyEvent.__init__(self)
        self.SetEventType(iEventType)

        self.__m_strMessage = strMessage
    # End of myMsgBoxEvent

    @property
    def strMessage(self):
        return self.__m_strMessage
    # End of myMsgBoxEvent
# End of class myMsgBoxEvent

class myFrame(myWxFrame, myInfoObserver):
    def __init__(self, oModel:myModel):
        myWxFrame.__init__(self, None)
        myInfoObserver.__init__(self)

        self.__m_oModel = oModel

        self.Connect(-1, -1, EVT_MSG_ID, self.handleOnMsgEvent)
        self.Connect(-1, -1, EVT_UPDATE_DATA, self.handleOnMsgEvent)
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

    def handleOnClickedButton(self, event):
        if event.Id == self.m_oButton.GetId():
            self.__m_oModel.isEvent = True
        # End of if-condition
    # End of myFrame::handleOnClickedButton

    def handleOnMsgEvent(self, event:myMsgBoxEvent):
        if event.GetEventType() == EVT_MSG_ID:
            strMessage = event.strMessage
            wx.MessageBox(strMessage, "Test")
        elif event.GetEventType() == EVT_UPDATE_DATA:
            strText = ""
            for i in range(len(self.__m_vstrMessage)):
                strText += self.__m_vstrMessage[i]
            # End of for-loop

            self.m_oMessageTextField.SetValue(strText)
        # End of handleOnMsgEvent
    # End of myFrame::handleOnMsgEvent

    def update(self, key: str, oInfo: myInfo):
        if "Message" == key:
            strMessage = oInfo.getParam(key)
            self.__m_vstrMessage.append(strMessage)
            if len(self.__m_vstrMessage) > 12:
                self.__m_vstrMessage.pop(0)
            # End of if-condition

            """
            Send an event to update text field, but other thread cannot be blocked.
            """
            oEvent = myMsgBoxEvent("Test", EVT_UPDATE_DATA)
            wx.PostEvent(self.GetEventHandler(), oEvent)
        elif "Event" == key:
            strMessage = oInfo.getParam(key)

            """
            Send event to this class and block the sender.
            The sender will resume after the event is handled.
            """
            oEvent = myMsgBoxEvent(strMessage)
            self.ProcessEvent(oEvent)

            oEvent = myMsgBoxEvent("wx.PostEvent() cannot block sener!")
            wx.PostEvent(self.GetEventHandler(), oEvent)
        # End of if-condition
    # End of myFrame::update
# End of class myFrame