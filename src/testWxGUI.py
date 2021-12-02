import wx
from myFrame import myFrame

def main():
    oApp = wx.App()
    oFrame = myFrame()
    oFrame.Show()
    oApp.MainLoop()
# End of main

if "__main__" == __name__:
    main()
# End of if-condition