import striga
from ... import SampleControllerBase
#TODO: This: from . import view_1a, view_1b

###

@striga.location('/page1/{arg1}')
@striga.location('/page1alt/{arg1}')
class Page1Controller(SampleControllerBase): #(striga.controller):


	def OnGET(self, ctx, arg1):
		pass


	@striga.action('register')
	def ActionREGISTER(self, ctx, action, arg1):
		pass
