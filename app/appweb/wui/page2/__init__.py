import striga
from ... import SampleControllerBase

###

@striga.location('/page2')
class Page2Controller(SampleControllerBase): #(striga.controller):

	def OnGET(self, ctx, arg1):
		pass
