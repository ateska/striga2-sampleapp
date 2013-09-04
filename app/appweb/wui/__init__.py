import striga
from . import page1, page2

###

class SampleRouter(striga.router):

	def on_init(self, app):
		self.SessionHandler = striga.sessionhandler(sesid=app.config['SESSION_ID'], lifetime=app.config['SESSION_LIFE_TIME'])
		self.UserHandler = striga.userhandler()
		self.I18NHandler = striga.i18nhandler()

		self.auto_dispatch(
			page1.Page1Controller(),
			page2.Page2Controller()
		)


	def on_entry(self, ctx):
		self.SessionHandler(ctx)
		self.UserHandler(ctx)
		self.self.I18NHandler(ctx)


#Using auto-dispatch
#	def on_dispatch(self, ctx):
#		pass
