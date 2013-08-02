from . import page1, page2

###

class SampleRouter(object): #(striga.router):

	def OnInit(self, app):
#		self.SessionHandler = striga.sessionhandler(sesid=app.config['SESSION_ID'], lifetime=app.config['SESSION_LIFE_TIME'])
#		self.UserHandler = striga.userhandler()
#		self.I18NHandler = striga.i18nhandler()
		pass


	def OnEntry(self, ctx):
		self.SessionHandler(ctx)
		self.UserHandler(ctx)
		self.self.I18NHandler(ctx)


	def OnDispatch(self, ctx):
		#TODO: Implementation of this ...
		if True:
			page1.Page1Controller()
		else:
			page2.Page2Controller()

