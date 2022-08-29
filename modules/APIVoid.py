###################################################################################################
#     _    ____ _____     __    _     _ 
#    / \  |  _ \_ _\ \   / /__ (_) __| |
#   / _ \ | |_) | | \ \ / / _ \| |/ _` |
#  / ___ \|  __/| |  \ V / (_) | | (_| |
# /_/   \_\_|  |___|  \_/ \___/|_|\__,_|
#                                       
###################################################################################################

from modules import loader
from modules import my_config



class APIVoid:

	## Init #########################################################################################

	def __init__(self):
		self.version  = 'v1/pay-as-you-go/'
		try:
			self.api_key  = my_config.API_KEYS['apivoid']['key']
			self.base_url = my_config.API_KEYS['apivoid']['base_url']
			self.module_enabled = True
		except:
			self.module_enabled = False

	## Getters ######################################################################################

	def get_URL_reputation(self,needle):
		if not self.module_enabled: return my_config.ERROR_NO_API
		url = self.base_url + f'urlrep/{self.version}' + f'?key={self.api_key}&url={needle}'
		ret = loader.get(url)
		json_data = loader.jsondecode(ret.text)
		return(json_data)

	def get_Email_Verify(self,needle):
		if not self.module_enabled: return my_config.ERROR_NO_API
		url = self.base_url + f'emailverify/{self.version}' + f'?key={self.api_key}&email={needle}'
		ret = loader.get(url)
		json_data = loader.jsondecode(ret.text)
		return(json_data)

