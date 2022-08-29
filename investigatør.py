#coding: utf-8

###################################################################################################
#  ___                     _   _             _             
# |_ _|_ ____   _____  ___| |_(_) __ _  __ _| |_ ___  _ __ 
#  | || '_ \ \ / / _ \/ __| __| |/ _` |/ _` | __/ _ \| '__|
#  | || | | \ V /  __/\__ \ |_| | (_| | (_| | || (_) | |   
# |___|_| |_|\_/ \___||___/\__|_|\__, |\__,_|\__\___/|_|   
#                                |___/                     
###################################################################################################

###################################################################################################
# ╻┏┳┓┏━┓┏━┓┏━┓╺┳╸┏━┓
# ┃┃┃┃┣━┛┃ ┃┣┳┛ ┃ ┗━┓
# ╹╹ ╹╹  ┗━┛╹┗╸ ╹ ┗━┛
###

from modules import APIVoid
from modules import BinaryEdge
from modules import IPInfo
from modules import SecurityTrails
from modules import Shodan
from modules import AbuseIPDB
from modules import Shodan
from modules import GetInfo
from modules import SSLinfos
from modules import HTMLinfos
from modules import TrendMicro
from modules import loader
# from modules import VulDB
# from modules import VirusTotal
from sys import argv,exit



###################################################################################################
# ┏━┓┏━┓┏━╸╻ ╻┏┳┓┏━╸┏┓╻╺┳╸┏━┓
# ┣━┫┣┳┛┃╺┓┃ ┃┃┃┃┣╸ ┃┗┫ ┃ ┗━┓
# ╹ ╹╹┗╸┗━┛┗━┛╹ ╹┗━╸╹ ╹ ╹ ┗━┛
###

# action = "print" # argv[1]
# target = "7580d3d305033fac91cca75ba5b0c4dc.json" # argv[2]
action = argv[1]
target = argv[2]



###################################################################################################
# ╺┳┓┏━┓╺┳╸┏━┓   ┏━╸┏━┓╻  ╻  ┏━╸┏━╸╺┳╸╻┏━┓┏┓╻
#  ┃┃┣━┫ ┃ ┣━┫   ┃  ┃ ┃┃  ┃  ┣╸ ┃   ┃ ┃┃ ┃┃┗┫
# ╺┻┛╹ ╹ ╹ ╹ ╹   ┗━╸┗━┛┗━╸┗━╸┗━╸┗━╸ ╹ ╹┗━┛╹ ╹
###

if action == 'scan':

	outfile = loader.md4(target)+'.json'
	url,proto,host,port,ip,email = loader.parse_url(target)

	## Objects ######################################################################################

	infos      = GetInfo.GetInfo()
	shodan     = Shodan.Shodan()
	ipinfo     = IPInfo.IPInfo()
	apivoid    = APIVoid.APIVoid()
	sectrails  = SecurityTrails.SecurityTrails()
	abuseipdb  = AbuseIPDB.AbuseIPDB()
	ssl_client = SSLinfos.SSLinfos()
	html_stats = HTMLinfos.HTMLinfos()
	trendmicro = TrendMicro.TrendMicro()

	result = {
		'target': {
			'url': url,
			'host': host,
			'ip': ip,
			'port': port
		},
		'infos':{},
		'ssl':{},
		'html':{},
		'shodan':{},
		'ip-info':{},
		'apivoid':{},
		'security-trails':{},
		'abuse':{},
		'trendmicro':{}
	}

	loader.print_status("infos")
	result["infos"]["whois"]      = infos.get_Whois(ip)
	result["infos"]["rev-dns"]    = infos.get_ReverseDNS(host,ip)
	result["infos"]["geo-ip"]     = infos.get_GeoIP(ip)
	result["infos"]["icmp"]       = infos.get_ICMPInfos(ip)
	result["infos"]["threats"]    = infos.get_ThreatInfo(ip,host) # Done by APIVoid
	# result["infos"]["verb"]       = infos.get_VerbStats(url,port)
	#------------------------------------------------------------------------------------------------
	loader.print_status("ssl")
	result["ssl"]["tls"]          = ssl_client.get_SSLProperties(host,ip,port)
	#------------------------------------------------------------------------------------------------
	loader.print_status("html")
	result["html"]["tags"]        = html_stats.get_TagsStats(url)
	result["html"]["href"]        = html_stats.get_External(url,['href'])
	result["html"]["src"]         = html_stats.get_External(url,['src'])
	#------------------------------------------------------------------------------------------------
	loader.print_status("infos")
	result["shodan"]["ip"]        = shodan.do_query(f"ip:{ip}")
	result["shodan"]["raw"]       = shodan.do_query(host)
	#------------------------------------------------------------------------------------------------
	loader.print_status("ip-info")
	result["ip-info"]             = ipinfo.get_ipinfo(ip)
	#------------------------------------------------------------------------------------------------
	loader.print_status("api-void")
	result["apivoid"]["email"]    = apivoid.get_Email_Verify(email)
	result["apivoid"]["urlrep"]   = apivoid.get_URL_reputation(loader.urlencode(url))
	#------------------------------------------------------------------------------------------------
	loader.print_status("abus-ipdb")
	result["abuse"]["ip"]         = abuseipdb.do_query(ip)
	#------------------------------------------------------------------------------------------------
	loader.print_status("security-trails")
	# result["security-trails"]["history-whois"] = sectrails.do_query(f'history/{host}/whois')
	result["security-trails"]["history-dns"]   = sectrails.do_query(f'/history/{host}/dns/a')

	## Report #######################################################################################

	loader.print_status("reporting")

	json_result = loader.jsonencode(result)
	open(outfile, "w").write(json_result)

	buff = ""
	try:
		buff = open("database.db","r").read()
	except:
		open("database.db","w").write("")

	if not target in buff:
		open("database.db","w").write(target+";"+outfile+"\n")

	# print_status("\nprocess terminated\n")
	print("[-] Report is: %s" % outfile)




###################################################################################################
# ╺┳┓┏━┓╺┳╸┏━┓   ╺┳┓╻┏━┓┏━┓╻  ┏━┓╻ ╻
#  ┃┃┣━┫ ┃ ┣━┫    ┃┃┃┗━┓┣━┛┃  ┣━┫┗┳┛
# ╺┻┛╹ ╹ ╹ ╹ ╹   ╺┻┛╹┗━┛╹  ┗━╸╹ ╹ ╹ 
###

if action == 'table':

	data   = open(target,"r").read()
	result = loader.jsondecode(data)

	title = "target"
	loader.print_title(title)
	loader.dump(result[title],format="table")

	title = "ip-info"
	loader.print_title(title)
	loader.dump(result[title],format="table")

	title = "ssl"
	loader.print_title(title)
	loader.dump(result[title]["tls"],format="table")

	title = "html"
	loader.print_title(title)
	loader.dump(result[title],format="table")

	title = "infos"
	loader.print_title("infos")
	loader.dump(result[title],format="table")

	title = "apivoid"
	loader.print_title("apivoid")
	if "data" in result[title]["urlrep"]:
		loader.dump(result[title]["email"],format="table")
		loader.dump(result[title]["urlrep"]["data"]["report"],format="table")

	title = "abuse"
	loader.print_title("abuse-ip-database")
	loader.dump(result[title],format="table")

	title = "security-trails"
	loader.print_title("security-trails")
	loader.dump(result[title],format="table")


if action == 'print':

	data   = open(target,"r").read()
	result = loader.jsondecode(data)
	loader.pretty_print(result)



if action == 'to-yaml':

	result = loader.json_to_yaml(target)
	print(result)


exit()

	# for title in result:
	# 	loader.print_title(title)

	# 	for section in result[title]:
	# 		loader.print_section(section)

	# 		if result[title][section]:
	# 			loader.dump(result[title][section])


				# for data in result[title][section]:
				# 	# print(type(data))
				# 	if type(data) == str:
				# 		print(data)
				# 	if type(data) == dict:
				# 		pp.pprint(data)




	# print_status("infos")
	# result["infos"]["whois"]      = infos.get_Whois(ip)
	# result["infos"]["rev-dns"]    = infos.get_ReverseDNS(host,ip)
	# result["infos"]["geo-ip"]     = infos.get_GeoIP(ip)
	# result["infos"]["icmp"]       = infos.get_ICMPInfos(ip)
	# result["infos"]["threats"]    = infos.get_ThreatInfo(ip,host) # Done by APIVoid
	# # result["infos"]["verb"]       = infos.get_VerbStats(url,port)
	# #------------------------------------------------------------------------------------------------
	# print_status("ssl")
	# result["ssl"]["tls"]          = ssl_client.get_SSLProperties(host,ip,port)
	# #------------------------------------------------------------------------------------------------
	# print_status("html")
	# result["html"]["tags"]        = html_stats.get_TagsStats(url)
	# result["html"]["href"]        = html_stats.get_External(url,['href'])
	# result["html"]["src"]         = html_stats.get_External(url,['src'])
	# #------------------------------------------------------------------------------------------------
	# print_status("infos")
	# result["shodan"]["ip"]        = shodan.do_query(f"ip:{ip}")
	# result["shodan"]["raw"]       = shodan.do_query(host)
	# #------------------------------------------------------------------------------------------------
	# print_status("ip-info")
	# result["ip-info"]             = ipinfo.get_info(ip)
	# #------------------------------------------------------------------------------------------------
	# print_status("api-void")
	# result["apivoid"]["email"]    = apivoid.get_Email_Verify(email)
	# result["apivoid"]["urlrep"]   = apivoid.get_URL_reputation(loader.urlencode(url))
	# #------------------------------------------------------------------------------------------------
	# print_status("abus-ipdb")
	# result["abuse"]["ip"]         = abuseipdb.do_query(ip)
	# #------------------------------------------------------------------------------------------------
	# print_status("security-trails")
	# result["security-trails"]["history-whois"] = sectrails.do_query(f'history/{host}/whois')
	# result["security-trails"]["history-dns"]   = sectrails.do_query(f'history/{host}/dns')

	# ## Report #######################################################################################

	# print_status("reporting")

	# json_result = loader.jsonencode(result)
	# open(outfile, "w").write(json_result)
	# buff = open("database.db","r").read()

	# if not target in buff:
	# 	open("database.db","w").write(target+";"+outfile+"\n")

	# # print_status("\nprocess terminated\n")
	# print("[-] Report is: %s" % outfile)

