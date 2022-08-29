###################################################################################################
#  _____                   _       __  __ _                
# |_   _| __ ___ _ __   __| |     |  \/  (_) ___ _ __ ___  
#   | || '__/ _ \ '_ \ / _` |_____| |\/| | |/ __| '__/ _ \ 
#   | || | |  __/ | | | (_| |_____| |  | | | (__| | | (_) |
#   |_||_|  \___|_| |_|\__,_|     |_|  |_|_|\___|_|  \___/ 
#                                                          
###################################################################################################

from modules import loader
from modules import my_config



class TrendMicro:

	"""
  Exemples 
  --------
  virustotal = my_VirusTotal.VirusTotal()
  ret = virustotal.do_query('df209aaa50b2d78f835c2314a056c0e3')
	"""

	## Init #########################################################################################

	def __init__(self,needle=""):

		self.http_headers = {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
      'Accept-Language': 'en-GB,en;q=0.7',
      'Cache-Control': 'max-age=0',
      'Connection': 'keep-alive',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': 'PHPSESSID=7tguc7c7qsal5ofmk4708g7096; region=ur5%2Fda2%2B; lan=uMA%3D; lz=uOCXn9Xlmw%3D%3D; remote_ip=pKpoYZ6mZKdkqqleZZ6p; AWSELB=5F195F2B1EBE45F9877305BAD66B2B750E9C58B51974AEA9720B9F59904ADE4D202E45605D8C94483595A1ECA8FDEC87DA5DCCF0A0B26EF4A89AEA96A16C78AD1577FAB53A; db_sampling_40=DB; _c1Ref=/result.php; utag_main=v_id:0182d55b16bd00027a572d9fa27004073003306b00ac8$_sn:1$_ss:0$_pn:7%3Bexp-session$_st:1661439508961$ses_id:1661436892861%3Bexp-session',
      'Origin': 'https://global.sitesafety.trendmicro.com',
      'Referer': 'https://global.sitesafety.trendmicro.com/result.php',
      'Sec-Fetch-Dest': 'document',
      'Sec-Fetch-Mode': 'navigate',
      'Sec-Fetch-Site': 'same-origin',
      'Sec-Fetch-User': '?1',
      'Sec-GPC': '1',
      'Upgrade-Insecure-Requests': '1',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36'
  	}

		try:
			self.base_url = my_config.API_KEYS['trendmicro']['base_url']
			self.module_enabled = True
		except:
			self.module_enabled = False
		if needle:
			self.needle = needle
		return

	## Getters ######################################################################################

	def do_query(self,needle=""):
		if not self.module_enabled: return False
		if not needle:
			needle = self.needle
		url = self.base_url

		ret = loader.post(url,{'urlname': needle, 'getinfo': 'Check+Now'}, headers=self.http_headers)
		buff = ret.text

		res = buff.split('<div class="titlerow whitebordertop" style="width:100%">Is it safe?</div>')[1].split('</div>')[1].split('>')[-1]
		cat = buff.split('How would you categorize this URL?')[1].split('<div class="labeltitlesmallresult">')[1].split('<div class="cleardiv"></div>')[0].split('</div>')[0]

		return( {'safety': res, 'category': cat} )

