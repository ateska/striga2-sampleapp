import striga
from ... import SampleControllerBase
from . import view_2

###

@striga.location('/page2')
class Page2Controller(striga.controller):

	def on_get(self, ctx, arg1):
		return self.view(view_2)
