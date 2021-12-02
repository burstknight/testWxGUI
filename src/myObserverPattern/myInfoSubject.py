from myObserverPattern.myInfo import myInfo
from myObserverPattern.myInfoObserver import myInfoObserver

class myInfoSubject(object):
    """
    Description:    This class is to update the new infomations to class myInfoObserver for observer pattern

    Programmer:     HONG-CING HUANG

    Date:           2020.05.26
    """
    def __init__(self, oInfo:myInfo):
        if oInfo is None:
            raise RuntimeError("The object oInfo of class myInfo is None in myInfoSubject constructor!")
        # End of if-condition
        self.__m_oInfo = oInfo
        self.__m_oObserverList = []
    # End of constructor

    @property
    def m_oObserverList(self):
        '''
		Description: The getter of the field m_oObserverList

        Programmer:     HONG-CING HUANG

        Date:       2020.05.27
		'''
        return self.__m_oObserverList
    # End of myInfoSubject::m_oObserverList getter

    @property
    def m_oInfo(self):
        '''
		Description: The getter of the field m_oInfo

        Programmer:     HONG-CING HUANG

        Date:       2020.05.27
		'''
        return self.__m_oInfo
    # End of myInfoSubject::m_oInfo

    def registerObserver(self, oObserver:myInfoObserver) -> None:
        '''
		Description:
        ==============================
        Register the observer
        
        Param:
        ====================================
        - oObserver:   ptype: myInfoObserver, the object can be notified.
        
        Return:
        ===============================
        - Void

        Programmer:     HONG-CING HUANG

        Date:       2020.05.26
		'''
        raise NotImplementedError("The method myInfoSubject::registerObserver() is not implemented yet!")
    # End of myInfoSubject::registerObserver

    def removeObserver(self, oObserver:myInfoObserver) -> None:
        '''
		Description:
        ==================================
        Remove the observer from the list.
        
        Param:
        =====================================
        - oObserver:   ptype: myInfoObserver, the object will be removed
        
        Return:
        ===============================
        - Void

        Programmer:     HONG-CING HUANG

        Date:       2020.05.26
		'''
        raise NotImplementedError("The method myInfoSubject::removeObserver() is not implemented yet!")
    # End of myInfoSubject::removeObserver

    def notifyObserver(self, key:str, value) -> None:
        '''
		Description:
        ===========================================
        When this class has new information, this method  will notify all observer.
        
        Param:
        ===================================
        - key:    ptype: str, the type of the updated information
        - value:  ptype: Any, the updated information
        
        Return:
        ======================================
        - Void

        Programmer:     HONG-CING HUANG

        Date:       2020.05.26
		'''
        raise NotImplementedError("The method myInfoSubject::notifyObserver() is not implemented yet!")
    # End of myInfoSubject::notifyObserver
# End of class myInfoSubject