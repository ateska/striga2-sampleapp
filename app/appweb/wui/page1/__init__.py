import striga
from ... import SampleControllerBase

from . import view_1a, view_1b

###

@striga.location('/page1/{arg1}')
@striga.location('/page1alt/{arg1}')
class Page1Controller(SampleControllerBase):


	def on_get(self, ctx, arg1):
		if arg1 == 'a':
			return self.view(view_1a)
		else:
			return self.view(view_1b, view_arg1 = 'foo')


	@striga.action('register')
	def action_register(self, ctx, action, arg1):
		
		return self.redirect('/page1/{arg1}'.format(arg1='b'))
