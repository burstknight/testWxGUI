from typing import Tuple


class myInfo(object):
    """
    Description:    This class wrapped many importance datum for observer pattern.

    Programmer:     HONG-CING HUANG

    Date:           2020.05.26
    """
    
    def getParam(self, key:str):
        '''
		Description:
        =================================
        Obtain a data of the given key
        
        Param:
        ==================================
        - key:   ptype: str, the key is to obtain one of datum.
        
        Return:
        ==================================
        - rtype: Any, return the value of the given key.

        Programmer:     HONG-CING HUANG

        Date:       2020.05.26
		'''
        raise NotImplementedError("The method myInfo::getParam() is not implemented yet!")
    # End of myInfo::getParam

    def setParam(self, key:str, value):
        '''
		Description:
        ================
        Set a data
        
        Param:
        =================================
        - key:    ptype: str, the key is to set the data.
        - value:  ptype: Any, the value of set data.
        
        Return:
        ==============================================
        - rtype: bool, return True if the data is set, otherwise return False.

        Programmer:     HONG-CING HUANG

        Date:       2020.05.26
		'''
        raise NotImplementedError("The method myInfo::setParam() is not implemented yet!")
    # End of myInfo::setParam
# End of class myInfo