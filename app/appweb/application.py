#import striga
from .wui import SampleRouter

###

class SampleStrigaApplication(object): #(striga.application):

	def OnInit(self):
		self.Router = SampleRouter(self)
		#self.Frontend = striga.frontend.SCGI(self, self.Router)
