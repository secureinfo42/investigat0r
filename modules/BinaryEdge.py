###################################################################################################
#  ____  _                        _____    _            
# | __ )(_)_ __   __ _ _ __ _   _| ____|__| | __ _  ___ 
# |  _ \| | '_ \ / _` | '__| | | |  _| / _` |/ _` |/ _ \
# | |_) | | | | | (_| | |  | |_| | |__| (_| | (_| |  __/
# |____/|_|_| |_|\__,_|_|   \__, |_____\__,_|\__, |\___|
#                           |___/            |___/      
###################################################################################################

from modules import loader
from modules import my_config



class BinaryEdge:

	## Init #########################################################################################

	def __init__(self):
		try:
			self.api_key  = my_config.API_KEYS['binaryedge']['key']
			self.base_url = my_config.API_KEYS['binaryedge']['base_url']
			self.module_enabled = True
		except:
			self.module_enabled = False

	## Getters ######################################################################################

	def get_URL_reputation(self,needle):
		if not self.module_enabled: return my_config.ERROR_NO_API
		url = self.base_url + 'urlrep/' + f'?key={self.api_key}&email={needle}'
		ret = loader.get(url)
		json_data = loader.jsondecode(ret.text)
		return(json_data)

	def get_Email_Verify(self,needle):
		if not self.module_enabled: return my_config.ERROR_NO_API
		url = self.base_url + 'emailverify/' + f'?key={self.api_key}&email={needle}'
		ret = loader.get(url,headers={'X-Key': self.api_key})
		json_data = loader.jsondecode(ret.text)
		return(json_data)


