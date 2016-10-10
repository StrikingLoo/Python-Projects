import wx

#colours go with a string or a  hash and code
def createOpposite(sArg):#takes a hash followed by a 6-char colour code  and makes it into the opposite one
	sArg=str(sArg)
	if len(sArg)!=7:
		return '#000000'
	else:
		sArg=[sArg[1:3],sArg[3:5],sArg[5:7]]
		smallD={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
		rv =[]
		for i in sArg:
			try: a = int(i[0])*16
			except: a = 16*smallD[i[0].upper()]
			try: rv.append(a+int(i[1]))
			except: rv.append(a+smallD[i[1].upper()])
		sArg=''
		for j in rv:
			tp = ([(255-j)//16,(255-j)%16])
			oDict={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}#the inverse of the other transformation
			for k in tp:
				if k>9:
					k=oDict[k]
				sArg+=str(k)
		return '#'+sArg

class MyWindows(wx.Frame):
	def __init__(self,*args,**kwargs):
		wx.Frame.__init__(self,size= (418,480),*args,**kwargs)
		self.BasicGUI()
		
	def BasicGUI(self):
		panel = wx.Panel(self)
		
		menuBar = wx.MenuBar()
		
		fileButton = wx.Menu()
		editButton = wx.Menu()
		
		exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'messages go here')
		editItem = editButton.Append(wx.ID_EDIT, 'Edit','some other msg')
		menuBar.Append(fileButton, '&File')
		menuBar.Append(editButton,'&Edit')
		self.SetMenuBar(menuBar)
		self.Bind(wx.EVT_MENU,self.Quit,exitItem)
		
		self.SetTitle('Epic Window')		
		self.Center()	
		self.Show()
		#YND = wx.MessageDialog(None,'Liking the program huh?','button',wx.YES_NO)
		#YesNoAnswer = YND.ShowModal()
		#YND.Destroy()
		#TED = wx.TextEntryDialog(None,'How old are you?','Age questions','age here plz')
		#if TED.ShowModal()==wx.ID_OK:
		#	age = TED.GetValue()
		SCD  = wx.SingleChoiceDialog(None,'title','question?',['#FF0000','#FF00FA','#FF0F05','#000F0A'])
		if SCD.ShowModal()==wx.ID_OK:
			color = SCD.GetStringSelection()
		else:
			color = '#0000FF'
			#####HERE BE THE PANEL'S CHILDREN AND KINNE
		st1 = wx.StaticText(panel, -1, 'Some String',pos=(50,15))
		btn1 = wx.Button(panel, wx.ID_ANY, 'does this go here?', pos=(420,10))
		tc1 = wx.TextCtrl(panel, value="don't believe his lies -->", size=(200,400), pos=(0,36))
		tc2 = wx.TextCtrl(panel,value='you may delete me',size=(200,400), pos=(200,36))
		self.st1 = wx.StaticText(panel, -1, 'Some String',pos=(50,15))
		self.st1.SetBackgroundColour(color)
		self.st1.SetForegroundColour(createOpposite(color)) #REMEMBER THE DARN HASH
		exxitItem = wx.MenuItem(fileButton,wx.ID_EXIT,'wtv')
		exxitItem.SetBitmap(wx.Bitmap('sd.png'))
		self.Bind(wx.EVT_BUTTON,self.OnClicking,btn1)
		fileButton.AppendItem(exxitItem)
		fonty = wx.Font(25,wx.DEFAULT,wx.SLANT,wx.BOLD)
		self.st1.SetFont(fonty)
		tc1.SetPosition((0,72))
		tc2.SetPosition((200,72))
	def Quit(self, e):
		self.SetTitle('Not so Epic tho')		
		self.Close()
	def OnClicking(self,e):
		newDialog = wx.TextEntryDialog(None,'text entry dialog','what do you want st1 to say?','default')
		if newDialog.ShowModal()==wx.ID_OK:
			self.st1.SetLabel( newDialog.GetValue())
			
			
		
		
		
		

app = wx.App()

fr1 = MyWindows(None)

app.MainLoop()