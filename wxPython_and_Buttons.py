import wx

class DaWindow(wx.Frame):
	def __init__(self,*args,**kwargs):
		wx.Frame.__init__(self,size= (720,360),*args,**kwargs)
		self.StartGUI()
		self.Show()
	def StartGUI(self):
		self.menuBar = wx.MenuBar()
		self.QuitMenu = wx.Menu()
		QuitBtn = self.QuitMenu.Append(wx.ID_EXIT,'Quit')
		self.menuBar.Append(self.QuitMenu, 'Wanna quit?')
		self.Bind(wx.EVT_MENU,self.Quitting,QuitBtn)
		self.SetMenuBar(self.menuBar)
		self.panel = wx.Panel(self)
		self.btn1 = wx.Button(self.panel,wx.ID_ANY,'+',pos=(100,100))
		self.btn2 = wx.Button(self.panel,wx.ID_ANY,'-',pos=(100,200))
		self.Statext = wx.StaticText(self.panel,wx.ID_ANY,str(0),pos=(140,140))
		self.LabelNumba = 0
		font = wx.Font(26,wx.DEFAULT,wx.NORMAL,wx.BOLD)
		self.Statext.SetFont(font)
		self.Statext.SetForegroundColour('#FF0000')
		self.btn1.Bind(wx.EVT_BUTTON,lambda uppity: self.ChangeNumba(self,1))
		self.btn2.Bind(wx.EVT_BUTTON,lambda downitty: self.ChangeNumba(self,-1))
		
	def Quitting(self,e):
		self.Close()
	def ChangeNumba(self,e,NumArg):
		self.LabelNumba+=NumArg
		self.Statext.SetLabel(str(self.LabelNumba))
		
muhapp = wx.App()
fr1 = DaWindow(None)
muhapp.MainLoop()