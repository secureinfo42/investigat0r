###################################################################################################
#  _     _ _                    _
# | |   (_) |__  _ __ __ _ _ __(_) ___  ___
# | |   | | '_ \| '__/ _` | '__| |/ _ \/ __|
# | |___| | |_) | | | (_| | |  | |  __/\__ \
# |_____|_|_.__/|_|  \__,_|_|  |_|\___||___/
#
################################################################################################### 

from json import JSONDecoder as jsondecode

import requests
requests.packages.urllib3.disable_warnings()

import warnings
warnings.filterwarnings("ignore")

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

import sys
import re
import ssl
import OpenSSL
import json
import yaml
import socket
import pygeoip
import logging
import socket
import simplejson
import hashlib
import pprint

from time      import sleep
from bs4       import BeautifulSoup
from os        import popen, system, unlink, stat
from hashlib   import sha1,md5,sha256
from modules   import my_config

# from scapy.all import IP,ICMP,sr1,conf
# conf.verb = 0



###################################################################################################
#  _____                 _   _
# |  ___|   _ _ __   ___| |_(_) ___  _ __  ___
# | |_ | | | | '_ \ / __| __| |/ _ \| '_ \/ __|
# |  _|| |_| | | | | (__| |_| | (_) | | | \__ \
# |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
#
################################################################################################### 



###################################################################################################
# ┏━┓╻ ╻┏━┓╺┳╸┏━╸┏┳┓
# ┗━┓┗┳┛┗━┓ ┃ ┣╸ ┃┃┃
# ┗━┛ ╹ ┗━┛ ╹ ┗━╸╹ ╹
##

###################################################################################################
## Tools

def tool(exe):
  for path in my_config.PATHS:
    try:
      stat(path+'/'+exe)
      return(path+'/'+exe)
    except:
      pass



###################################################################################################
# ┏━╸┏┓╻┏━╸┏━┓╺┳┓┏━╸┏━┓┏━┓
# ┣╸ ┃┗┫┃  ┃ ┃ ┃┃┣╸ ┣┳┛┗━┓
# ┗━╸╹ ╹┗━╸┗━┛╺┻┛┗━╸╹┗╸┗━┛
##

###################################################################################################
## URL

def urlencode(url):
  url = url.replace(':','%3a')
  url = url.replace('?','%3f')
  url = url.replace('&','%26')
  url = url.replace('/','%2f')
  url = url.replace('.','%2e')
  url = url.replace('+','%2b')
  return(url)

def urldecode(url):
  url = url.replace('%3a',':')
  url = url.replace('%3f','?')
  url = url.replace('%26','&')
  url = url.replace('%2f','/')
  url = url.replace('%2e','.')
  url = url.replace('%2b','+')
  return(url)

###################################################################################################
## Json

def jsonencode(mixed):
  try:
    return( simplejson.dumps(mixed) )
  except:
    return( simplejson.dumps('-') )

def jsondecode(text):
  try:
    return( simplejson.loads(text) )
  except:
    return( {'-'} )


def json_to_yaml(filename):
  try:
    return( yaml.dump(json.load(open(filename)), default_flow_style=False) )
  except:
    return( {'-'} )



###################################################################################################
# ╺┳┓╻┏━┓┏━┓╻  ┏━┓╻ ╻
#  ┃┃┃┗━┓┣━┛┃  ┣━┫┗┳┛
# ╺┻┛╹┗━┛╹  ┗━╸╹ ╹ ╹ 
##

class colors:
  def __init__(self,nocolor=""):
    self.gray     = "\033[1;30m"
    self.red      = "\033[1;31m"
    self.green    = "\033[1;32m"
    self.yellow   = "\033[1;33m"
    self.blue     = "\033[1;34m"
    self.magenta  = "\033[1;35m"
    self.cyan     = "\033[1;36m"
    #---------------------------
    self.dred     = "\033[0;31m"
    self.dgreen   = "\033[0;32m"
    self.dyellow  = "\033[0;33m"
    self.dblue    = "\033[0;34m" # dark magenta
    self.dmagenta = "\033[0;35m" # dark magenta
    self.dcyan    = "\033[0;36m" # dark magenta
    #---------------------------
    self.reset    = "\033[0m"
    return
c = colors()

def sep(separator="-"):
  global c
  print("%s%s%s" % (c.gray,str(separator)*my_config.TERM_WIDTH,c.reset))

def perror(errtxt,errcode=""):
  msg = "Error: {}\n".format(errtxt)
  if my_config.DEBUG:
    try:
      open("/dev/stderr","wt").write(msg)
    except:
      print("{}".format(msg))
  if errcode:
    sys.exit(int(errcode))

def print_status(txt):
  txt = txt.upper()
  txt = f"[*] {txt} …"
  pdl = 42-len(txt)
  pad = " "*pdl
  txt = txt + pad
  # print(txt, file=sys.stderr, end="\r")
  print(txt, file=sys.stderr)
  sleep(.2)

def print_title(text):

  print("\n\n\033[1;32m")
  print("="*100)
  print(text.upper())
  print("="*100)
  print("\033[0m")

def print_section(text):

  print("\033[1;36m" + "=== " + text.upper() + "\033[0m")

def printable(mixed):
  ret=0
  if type(mixed) == str:  ret=1
  if type(mixed) == int:  ret=1
  if type(mixed) == bool: ret=1
  return ret

def dump(data,format=""):
  # TODO: find a better way to pretty print json
  global c # colors

  if type(data) == dict:
    if format == "":
      pp.pprint(data)

    if format == "table":
      for key in data:
        if type(data[key]) == str:
          print("%s%-20s%s %s%s%s %s" % (c.magenta,key,c.reset , c.gray,"|",c.reset , data[key]))
        if type(data[key]) == list:
          print("%s%-20s %s%s" % (c.magenta,key , ":", c.reset))
          for value in data[key]:
            if printable(value):
              print("%-20s %s%s%s %s" % (" " , c.magenta,"-",c.reset , value))
            else:
              for i in value:
                if type(value[i]) == str:
                  print("%-20s %s%-40s%s %s" % (" " , c.dblue,i+":",c.reset , value[i]))
          sep("-")

        if type(data[key]) == dict:
          print("%s%-20s %s%s" % (c.magenta,key , ":", c.reset))
          for index in data[key]:
            if type(data[key][index]) == dict:
              for index_deep in data[key][index]:
                if printable(data[key][index][index_deep]):
                  print("%-20s %s%s%s%s %s" % (" ", c.dred,index_deep,":",c.reset , data[key][index][index_deep]))
                if type(data[key][index][index_deep]) == dict:
                  for sub_key in data[key][index][index_deep]:
                    print("%-20s %s%s%s%s %s" % (" ", c.dcyan,sub_key,":",c.reset , data[key][index][index_deep][sub_key]))

                if type(data[key][index][index_deep]) == list:
                  for item in data[key][index][index_deep]:
                    if type(item) == str:
                      print("%-20s %s%s%s%s %s" % (" ", c.dred,index_deep,":",c.reset , item))
                    if type(item) == list:
                      for sub_item in item:
                        if printable(item):
                          print("%-20s %s%s%s%s %s" % (" ", c.dred," ",":",c.reset , item))
                      print()
                    if type(item) == dict:  
                      out = ""
                      for sub_item in item:
                        if printable(item[sub_item]):
                          out += "%s%s%s%s %s, " % (c.dred,sub_item,":",c.reset , item[sub_item])
                          # print("%-20s %s%s%s%s %s" % (" ", c.dred,sub_item,":",c.reset , item[sub_item]))
                      print("%-20s %s" % (" ",out))

            if type(data[key][index]) == list:
              for index_deep in data[key][index]:
                if type(index_deep) == dict:
                  out = ""
                  for index_deeper in index_deep:
                    out += c.dblue + index_deeper+": "+c.reset + str(index_deep[index_deeper]) + "\n" + " "*30 + " "
                  print("%-20s %s%s%s%s %s" % (" ", c.dyellow,index_deeper,":",c.reset , out))
            else:
              if printable(data[key][index]):
                print("%-20s %s%-40s%s %s" % (" " , c.dblue,index+":",c.reset , data[key][index]))
              if type(data[key][index]) == dict:
                for item in data[key][index]:
                  if printable(data[key][index][item]):
                    print("%-20s %s%-40s%s %s" % (" " , c.dblue,item+":",c.reset , data[key][index][item]))
              if type(data[key][index]) == list:
                for item in data[key][index]:
                  if printable(data[key][index][item]):
                    print("%-20s %s%-40s%s %s" % (" " , c.dblue,"-",c.reset , item))


          sep("-")
  else:
    print(data)

def pretty_print(data,format=""):
  pp = pprint.PrettyPrinter(indent=4)
  pp.pprint(data)



###################################################################################################
# ┏━╸┏━┓┏┓╻╻ ╻┏━╸┏━┓╺┳╸┏━╸┏━┓┏━┓
# ┃  ┃ ┃┃┗┫┃┏┛┣╸ ┣┳┛ ┃ ┣╸ ┣┳┛┗━┓
# ┗━╸┗━┛╹ ╹┗┛ ┗━╸╹┗╸ ╹ ┗━╸╹┗╸┗━┛
##

###################################################################################################
## IP -> number

def ip2long(ip):
  ip    = [int(x) for x in ip.split(".")]
  long  = (ip[0] << 24)
  long += (ip[1] << 16)
  long += (ip[2] << 8)
  long += ip[3]
  return(long)

def ip2long_rev(ip):
  ip    = [int(x) for x in ip.split(".")]
  long  = (ip[3] << 24)
  long += (ip[2] << 16)
  long += (ip[1] << 8)
  long += ip[0]
  return(long)

def ip2hex(ip):
  ip = ["0"*(4-len(hex(int(x))))+hex(int(x)) for x in ip.split(".")]
  hx = ''.join(ip)
  hx = "0x"+hx.replace("0x","")
  return(hx)
 
###################################################################################################
## number -> IP

def long2ip(long):
  long = int(long)
  ip = [0,0,0,0]
  ip[0] = (long & 0xFF000000) >> 24
  ip[1] = (long & 0x00FF0000) >> 16
  ip[2] = (long & 0x0000FF00) >> 8
  ip[3] = (long & 0x000000FF)
  ip = [str(x) for x in ip]
  ip = '.'.join(ip)
  return(ip)

def long2ip_rev(long):
  long = int(long)
  ip = [0,0,0,0]
  ip[3] = (long & 0xFF000000) >> 24
  ip[2] = (long & 0x00FF0000) >> 16
  ip[1] = (long & 0x0000FF00) >> 8
  ip[0] = (long & 0x000000FF)
  ip = [str(x) for x in ip]
  ip = '.'.join(ip)
  return(ip)



###################################################################################################
# ╻ ╻┏━┓┏━┓╻ ╻┏━╸┏━┓┏━┓
# ┣━┫┣━┫┗━┓┣━┫┣╸ ┣┳┛┗━┓
# ╹ ╹╹ ╹┗━┛╹ ╹┗━╸╹┗╸┗━┛
##

###################################################################################################
## IP -> number

def md4(data):
  cmd = f'echo {data}|openssl dgst -md4'
  ret = popen(cmd).read().strip()
  md4 = ret.split('= ')[1]
  return(md4)

def md5(data):
  md5 = hashlib.sha1(data.encode()).hexdigest()
  return(md5)



###################################################################################################
# ╻ ╻┏━╸┏┓ 
# ┃╻┃┣╸ ┣┻┓
# ┗┻┛┗━╸┗━┛
##

###################################################################################################
## Get

def get(url,headers={}):

  current_headers = my_config.HEADERS
  current_headers.update(headers)
  s = requests.session()
  r = ''
  try:
    r = s.get(url,headers=current_headers,verify=False,allow_redirects=False)
    pass
  except Exception as e:
    raise
  return(r)

###################################################################################################
## Post

def post(url,post_data,headers={}):
  current_headers = my_config.HEADERS
  current_headers.update(headers)
  s = requests.session()
  r = ''
  try:
    r = s.post(url,post_data,headers=current_headers,verify=False,allow_redirects=False)
    pass
  except Exception as e:
    raise
  return(r)

###################################################################################################
## TCP

def send_tcp_pkt(host,port,verb):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  p = verb.encode() + b" / HTTP/1.1\r\n"
  r = b''
  try:
    c = s.connect((host,port))
    s.send(p)
    r = s.recv(65535)
    s.close()
  except:
    pass
  return(r)

###################################################################################################
## Parse

def parse_url(url):
  rgx = r"^(\w+)://([a-zA-Z0-9-_\.]+):?(\d*)/?"
  if not 'http' in url and not '://' in url:
    url = 'https://{}/'.format(url)
  rgx = re.compile(rgx)
  ret = re.findall(rgx,url)
  try:
    proto = ret[0][0]
    host  = ret[0][1]
    port  = ret[0][2]
  except IndexError:
    perror("unable to parse URL : `{}`".format(url),1)
  if not port:
    if proto == 'https': port = 443
    if proto == 'http':  port = 80
    if proto == 'ftp':   port = 21
    if proto == 'ftps':  port = 990
    if proto == 'rtsp':  port = 554
  if ret:
    try:
      ip = socket.gethostbyname(host)
    except socket.error:
      perror("unable to resolve host `{}`\n".format(host))
      sys.exit()
    ip = str(ip)
  email = 'contact@'+host
  return(url,proto,host,port,ip,email)

