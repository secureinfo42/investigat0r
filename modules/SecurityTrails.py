###################################################################################################
#  ____                       _ _        _____          _ _     
# / ___|  ___  ___ _   _ _ __(_) |_ _   |_   _| __ __ _(_) |___ 
# \___ \ / _ \/ __| | | | '__| | __| | | || || '__/ _` | | / __|
#  ___) |  __/ (__| |_| | |  | | |_| |_| || || | | (_| | | \__ \
# |____/ \___|\___|\__,_|_|  |_|\__|\__, ||_||_|  \__,_|_|_|___/
#                                   |___/                       
###################################################################################################

from modules import loader
from modules import my_config



class SecurityTrails:

	## Init #########################################################################################

	def __init__(self,query=""):
		try:
			self.api_key  = my_config.API_KEYS['securitytrails']['key']
			self.base_url = my_config.API_KEYS['securitytrails']['base_url']
			self.module_enabled = True
		except:
			self.module_enabled = False
		if query:
			self.query = query
		return

	## Getters ######################################################################################

	def do_query(self,query=""):
		if not self.module_enabled: return my_config.ERROR_NO_API
		if not query:
			query = self.query
		url = self.base_url + f'{query}' 
		ret = loader.get(url,headers={'apikey': self.api_key})
		# return(ret.text)
		json_data = loader.jsondecode(ret.text)
		return(json_data)

