from myObserverPattern.myInfo import myInfo
class myInfoObserver(object):
    """
    Description:    This class is to monitor the new informations of the class myInfoSubject.

    Programmer:     HONG-CING HUANG

    Date:           2020.05.26
    """
    def update(self, key:str, oInfo:myInfo):
        '''
		Description:
        ==============================
        Update the new information.
        
        Param:
        ====================================
        - key:    ptype: str, the kind of the updated new information
        - oInfo:  ptype: myInfo, the new information can be obtain from this object.
        
        Return:
        ============================
        - Void

        Programmer:     HONG-CING HUANG

        Date:       2020.05.26
		'''
        raise NotImplementedError("The method myInfoObserver::update() is not implememented yet!")
    # End of myOnfoObserver::update
# End of class myInfoObserver