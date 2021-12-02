from myObserverPattern import myInfo

class myObservablePattern(myInfo):
    def __init__(self) -> None:
        super().__init__()
        self.__m_strMessage = ""
    # End of constructor

    def setParam(self, key: str, value):
        isSet = True
        if "Message" == key:
            self.__m_strMessage = value
        elif "Event" == key:
            self.__m_strMessage = value
        else:
            isSet = False
        # End of if-condition

        return isSet
    # End of myObservablePattern::setParam

    def getParam(self, key: str):
        if "Message" == key:
            return self.__m_strMessage
        elif "Event" == key:
            return self.__m_strMessage
        else:
            return None
        # End of if-condition
    # End of myObservablePattern::getParam
# End of class myObservablePattern