import wx
from myFrame import myFrame
from myModel import myModel

def main():
    oApp = wx.App()
    oModel = myModel()
    oFrame = myFrame(oModel)
    oModel.registerObserver(oFrame)
    oFrame.Show()
    oModel.start()
    oApp.MainLoop()

    oModel.join()
# End of main

if "__main__" == __name__:
    main()
# End of if-condition