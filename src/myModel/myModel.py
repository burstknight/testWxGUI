import time
from myObserverPattern import *
from threading import Thread
from random import randint

class myModel(myInfoSubject, Thread):
    def __init__(self):
        myInfoSubject.__init__(self, myObservableInfo())
        Thread.__init__(self, name="Model", daemon=True)

        self.__m_isRun = True
        self.__m_isEvent = False
    # End of constructor

    @property
    def isRun(self):
        return self.__m_isRun
    # End of myModel::isRun

    @isRun.setter
    def isRun(self, isRun:bool):
        self.__m_isRun = isRun
    # End of myModel::isRun

    @property
    def isEvent(self):
        return self.__m_isEvent
    # End of myModel::isEvent

    @isEvent.setter
    def isEvent(self, isEvent:bool):
        self.__m_isEvent = isEvent
    # End of myModel::isEvent

    def run(self) -> None:
        print("Run model!")

        while(True):
            if(False == self.isRun):
                break
            # End of if-condition

            if(True == self.isEvent):
                self.notifyObserver("Event", "Button is clicked!")
                self.isEvent = False
            # End of if-condition

            iData = randint(0, 9999)
            print("Generate Data: %d" %(iData))
            self.notifyObserver("Message", "Generate data: %d\n" %(iData))

            time.sleep(1)
        # End of while-loop

        print("Stop model!")
    # End of myModel::run

    def notifyObserver(self, key: str, value) -> None:
        if True == self.m_oInfo.setParam(key, value):
            for i in range(len(self.m_oObserverList)):
                self.m_oObserverList[i].update(key, self.m_oInfo)\
            # End of for-loop
        # End of if-condition
    # End of myModel::notifyObserver

    def registerObserver(self, oObserver: myInfoObserver) -> None:
        if oObserver not in self.m_oObserverList:
            self.m_oObserverList.append(oObserver)
        # End of if-condition
    # End of myModel::registerObserver

    def removeObserver(self, oObserver: myInfoObserver) -> None:
        if oObserver in self.m_oObserverList:
            index = self.m_oObserverList.index(oObserver)
            self.m_oObserverList.pop(index)
        # End of if-condition
    # End of myModel::removeObserver
# End of class myModel