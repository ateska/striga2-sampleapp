import striga
from .wui import SampleRouter
from .context import CustomContext

###

class SampleStrigaApplication(striga.application):

	def on_init(self):
		self.Router = SampleRouter(self)
		self.Frontend = striga.frontend.SCGI(self, self.Router, CustomContext)
