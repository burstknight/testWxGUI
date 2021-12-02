# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class myWxFrame
###########################################################################

class myWxFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Test", pos = wx.DefaultPosition, size = wx.Size( 835,410 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_oMessageTextField = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_oMessageTextField, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_oButton = wx.Button( self, wx.ID_ANY, u"Click me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_oButton.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微軟正黑體" ) )

		bSizer1.Add( self.m_oButton, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.handleOnClose )
		self.m_oMessageTextField.Bind( wx.EVT_UPDATE_UI, self.handleOnUpdateUI )
		self.m_oButton.Bind( wx.EVT_BUTTON, self.handleOnClickedButton )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def handleOnClose( self, event ):
		event.Skip()

	def handleOnUpdateUI( self, event ):
		event.Skip()

	def handleOnClickedButton( self, event ):
		event.Skip()



