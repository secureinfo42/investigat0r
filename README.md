# investigat0r

> Note: this is still a draft.

## Wtf is it ?

This script is intended to gather as much information as it can thanks to some API.

## How to use it ?

```
python investigatør.py scan 'https://www.exemple.com/html/'
```

This will return with the MD5 of the given URL in argument :

```
[*] INFOS …
[*] SSL …
[*] HTML …
[*] INFOS …
[*] IP-INFO …
[*] API-VOID …
[*] ABUS-IPDB …
[*] SECURITY-TRAILS …
[*] REPORTING …
[-] Report is: 7580d3d305033fac91cca75ba5b0c4dc.json
```

All scanned sites/URL are stored in `database.db`

## How to display result ?

There are 3 ways to print result : in `json`, in `yaml` or in `table` format.

### json

```sh
jq < 7580d3d305033fac91cca75ba5b0c4dc.json
```

Result :

```json
{
  "target": {
    "url": "https://www.google.com/",
    "host": "www.google.com",
    "ip": "142.250.179.68",
    "port": 443
  },
  "infos": {
    "whois": [
      {
        "refer": "whois.arin.net"
      },
      {
        "inetnum": "142.0.0.0 - 142.255.255.255",
        "organisation": "Administered by ARIN",
        "status": "LEGACY"
      },
      {
        "whois": "whois.arin.net"
      },
      {
        "changed": "1993-05",
        "source": "IANA"
      },
      {
        "NetRange": "142.250.0.0 - 142.251.255.255",
        "CIDR": "142.250.0.0/15",
        "NetName": "GOOGLE",
        "NetHandle": "NET-142-250-0-0-1",
        "Parent": "NET142 (NET-142-0-0-0-0)",
        "NetType": "Direct Allocation",
        "OriginAS": "AS15169",
        "Organization": "Google LLC (GOGL)",
        "RegDate": "2012-05-24",
        "Updated": "2012-05-24",
        "Ref": "https //rdap.arin.net/registry/ip/142.250.0.0"
      },
      {
        "OrgName": "Google LLC",
        "OrgId": "GOGL",
        "Address": "1600 Amphitheatre Parkway",
        "City": "Mountain View",
        "StateProv": "CA",
        "PostalCode": "94043",
        "Country": "US",
        "RegDate": "2000-03-30",
        "Updated": "2019-10-31",
        "Ref": "https //rdap.arin.net/registry/entity/GOGL"
      },
      {
        "OrgTechHandle": "ZG39-ARIN",
        "OrgTechName": "Google LLC",
        "OrgTechPhone": "+1-650-253-0000",
        "OrgTechEmail": "arin-contact@google.com",
        "OrgTechRef": "https //rdap.arin.net/registry/entity/ZG39-ARIN"
      },
      {
        "OrgAbuseHandle": "ABUSE5250-ARIN",
        "OrgAbuseName": "Abuse",
        "OrgAbusePhone": "+1-650-253-0000",
        "OrgAbuseEmail": "network-abuse@google.com",
        "OrgAbuseRef": "https //rdap.arin.net/registry/entity/ABUSE5250-ARIN"
      }
    ],
    "rev-dns": [
      "par21s19-in-f4.1e100.net",
      "68.179.250.142.in-addr.arpa",
      "142.250.179.68"
    ],
    "geo-ip": "US",
    "icmp": {
      "icmp": {
        "ttl": 114,
        "guessed-os": "Windows",
        "distance": "14"
      }
    },
    "threats": [
      {
        "rules.emergingthreats.net": "False"
      },
      {
        "cybercrime-tracker.net": "False"
      },
      {
        "easylist.to": "True"
      },
      {
        "github:vaseem-khan-URLcheck": "False"
      },
      {
        "github:marcobrandobh_IOCs": "False"
      },
      {
        "zonefiles.io:domains": "False"
      },
      {
        "zonefiles.io:ips": "False"
      },
      {
        "urlhaus.abuse.ch": "False"
      }
    ]
  },
  "ssl": {
    "tls": {
      "is_expired": false,
      "not-before": "2022/08/08@08:25",
      "not-after": "2022/10/31@08:25",
      "subject": "/CN=www.google.com",
      "altnames": [
        "www.google.com"
      ]
    }
  },
  "html": {
    "tags": {
      "a": 18,
      "b": 1,
      "body": 1,
      "br": 5,
      "center": 1,
      "div": 13,
      "form": 1,
      "head": 1,
      "html": 1,
      "img": 1,
      "input": 10,
      "meta": 2,
      "nobr": 2,
      "p": 1,
      "script": 8,
      "span": 8,
      "style": 3,
      "table": 1,
      "td": 3,
      "title": 1,
      "tr": 1,
      "u": 1,
      "#Total": 84
    },
    "href": [
      "https://www.google.fr/imghp?hl=fr&tab=wi",
      "https://maps.google.fr/maps?hl=fr&tab=wl",
      "https://play.google.com/?hl=fr&tab=w8",
      "https://www.youtube.com/?tab=w1",
      "https://news.google.com/?tab=wn",
      "https://mail.google.com/mail/?tab=wm",
      "https://drive.google.com/?tab=wo",
      "https://www.google.fr/intl/fr/about/products?tab=wh",
      "http://www.google.fr/history/optout?hl=fr",
      "/preferences?hl=fr",
      "https://accounts.google.com/ServiceLogin?hl=fr&passive=true&continue=https://www.google.com/&ec=GAZAAQ",
      "/advanced_search?hl=fr&authuser=0",
      "https://www.google.com/setprefs?sig=0_zGenCZBnn1lZ5gO2iPtxE2oL1Gc%3D&hl=en&source=homepage&sa=X&ved=0ahUKEwidlL7vpOz5AhUBuRoKHZSGCAgQ2ZgBCAU",
      "/services/",
      "/intl/fr/about.html",
      "https://www.google.com/setprefdomain?prefdom=FR&prev=https://www.google.fr/&sig=K_A9ocA4gSno7LdKqcAwZfrBfcJm0%3D",
      "/intl/fr/policies/privacy/",
      "/intl/fr/policies/terms/"
    ],
    "src": [
      "/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png"
    ]
  },
  "shodan": {
    "ip": "Error: no valid authentication",
    "raw": "Error: no valid authentication"
  },
  "ip-info": {
    "ip": "142.250.179.68",
    "hostname": "par21s19-in-f4.1e100.net",
    "city": "Paris",
    "region": "Île-de-France",
    "country": "FR",
    "loc": "48.8534,2.3488",
    "org": "AS15169 Google LLC",
    "postal": "75000",
    "timezone": "Europe/Paris",
    "readme": "https://ipinfo.io/missingauth"
  },
  "apivoid": {
    "email": {
      "elapsed_time": "0.00",
      "error": "API key is not valid"
    },
    "urlrep": {
      "elapsed_time": "0.00",
      "error": "API key is not valid"
    }
  },
  "security-trails": {
    "history-dns": {
      "message": "Invalid authentication credentials"
    }
  },
  "abuse": {
    "ip": {
      "ip": "142.250.179.68",
      "found": "found",
      "reports": "4",
      "confidence": "0%"
    }
  },
  "trendmicro": {}
}

```


### yaml


```sh
python investigatør.py to-yaml 7580d3d305033fac91cca75ba5b0c4dc.json
```

Result :

```yaml
abuse:
  ip:
    confidence: 0%
    found: found
    ip: 142.250.179.68
    reports: '4'
apivoid:
  email:
    elapsed_time: '0.00'
    error: API key is not valid
  urlrep:
    elapsed_time: '0.00'
    error: API key is not valid
html:
  href:
    - https://www.google.fr/imghp?hl=fr&tab=wi
    - https://maps.google.fr/maps?hl=fr&tab=wl
    - https://play.google.com/?hl=fr&tab=w8
    - https://www.youtube.com/?tab=w1
    - https://news.google.com/?tab=wn
    - https://mail.google.com/mail/?tab=wm
    - https://drive.google.com/?tab=wo
    - https://www.google.fr/intl/fr/about/products?tab=wh
    - http://www.google.fr/history/optout?hl=fr
    - /preferences?hl=fr
    - https://accounts.google.com/ServiceLogin?hl=fr&passive=true&continue=https://www.google.com/&ec=GAZAAQ
    - /advanced_search?hl=fr&authuser=0
    - https://www.google.com/setprefs?sig=0_zGenCZBnn1lZ5gO2iPtxE2oL1Gc%3D&hl=en&source=homepage&sa=X&ved=0ahUKEwidlL7vpOz5AhUBuRoKHZSGCAgQ2ZgBCAU
    - /services/
    - /intl/fr/about.html
    - https://www.google.com/setprefdomain?prefdom=FR&prev=https://www.google.fr/&sig=K_A9ocA4gSno7LdKqcAwZfrBfcJm0%3D
    - /intl/fr/policies/privacy/
    - /intl/fr/policies/terms/
  src:
    - /images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png
  tags:
    '#Total': 84
    a: 18
    b: 1
    body: 1
    br: 5
    center: 1
    div: 13
    form: 1
    head: 1
    html: 1
    img: 1
    input: 10
    meta: 2
    nobr: 2
    p: 1
    script: 8
    span: 8
    style: 3
    table: 1
    td: 3
    title: 1
    tr: 1
    u: 1
infos:
  geo-ip: US
  icmp:
    icmp:
      distance: '14'
      guessed-os: Windows
      ttl: 114
  rev-dns:
    - par21s19-in-f4.1e100.net
    - 68.179.250.142.in-addr.arpa
    - 142.250.179.68
  threats:
    - rules.emergingthreats.net: 'False'
    - cybercrime-tracker.net: 'False'
    - easylist.to: 'True'
    - github:vaseem-khan-URLcheck: 'False'
    - github:marcobrandobh_IOCs: 'False'
    - zonefiles.io:domains: 'False'
    - zonefiles.io:ips: 'False'
    - urlhaus.abuse.ch: 'False'
  whois:
    - refer: whois.arin.net
    - inetnum: 142.0.0.0 - 142.255.255.255
      organisation: Administered by ARIN
      status: LEGACY
    - whois: whois.arin.net
    - changed: 1993-05
      source: IANA
    - CIDR: 142.250.0.0/15
      NetHandle: NET-142-250-0-0-1
      NetName: GOOGLE
      NetRange: 142.250.0.0 - 142.251.255.255
      NetType: Direct Allocation
      Organization: Google LLC (GOGL)
      OriginAS: AS15169
      Parent: NET142 (NET-142-0-0-0-0)
      Ref: https //rdap.arin.net/registry/ip/142.250.0.0
      RegDate: '2012-05-24'
      Updated: '2012-05-24'
    - Address: 1600 Amphitheatre Parkway
      City: Mountain View
      Country: US
      OrgId: GOGL
      OrgName: Google LLC
      PostalCode: '94043'
      Ref: https //rdap.arin.net/registry/entity/GOGL
      RegDate: '2000-03-30'
      StateProv: CA
      Updated: '2019-10-31'
    - OrgTechEmail: arin-contact@google.com
      OrgTechHandle: ZG39-ARIN
      OrgTechName: Google LLC
      OrgTechPhone: +1-650-253-0000
      OrgTechRef: https //rdap.arin.net/registry/entity/ZG39-ARIN
    - OrgAbuseEmail: network-abuse@google.com
      OrgAbuseHandle: ABUSE5250-ARIN
      OrgAbuseName: Abuse
      OrgAbusePhone: +1-650-253-0000
      OrgAbuseRef: https //rdap.arin.net/registry/entity/ABUSE5250-ARIN
ip-info:
  city: Paris
  country: FR
  hostname: par21s19-in-f4.1e100.net
  ip: 142.250.179.68
  loc: 48.8534,2.3488
  org: AS15169 Google LLC
  postal: '75000'
  readme: https://ipinfo.io/missingauth
  region: "Île-de-France"
  timezone: Europe/Paris
security-trails:
  history-dns:
    message: Invalid authentication credentials
shodan:
  ip: 'Error: no valid authentication'
  raw: 'Error: no valid authentication'
ssl:
  tls:
    altnames:
      - www.google.com
    is_expired: false
    not-after: 2022/10/31@08:25
    not-before: 2022/08/08@08:25
    subject: /CN=www.google.com
target:
  host: www.google.com
  ip: 142.250.179.68
  port: 443
  url: https://www.google.com/
trendmicro: {}

```

### table

```sh
python investigatør.py table 7580d3d305033fac91cca75ba5b0c4dc.json
```

```

====================================================================================================
TARGET
====================================================================================================

url                  | https://www.google.com/
host                 | www.google.com
ip                   | 142.250.179.68



====================================================================================================
IP-INFO
====================================================================================================

ip                   | 142.250.179.68
hostname             | par21s19-in-f4.1e100.net
city                 | Paris
region               | Île-de-France
country              | FR
loc                  | 48.8534,2.3488
org                  | AS15169 Google LLC
postal               | 75000
timezone             | Europe/Paris
readme               | https://ipinfo.io/missingauth



====================================================================================================
SSL
====================================================================================================

not-before           | 2022/08/08@08:25
not-after            | 2022/10/31@08:25
subject              | /CN=www.google.com
altnames             :
                     - www.google.com
----------------------------------------------------------------------------------------------------



====================================================================================================
HTML
====================================================================================================

tags                 :
                     a:                                       18
                     b:                                       1
                     body:                                    1
                     br:                                      5
                     center:                                  1
                     div:                                     13
                     form:                                    1
                     head:                                    1
                     html:                                    1
                     img:                                     1
                     input:                                   10
                     meta:                                    2
                     nobr:                                    2
                     p:                                       1
                     script:                                  8
                     span:                                    8
                     style:                                   3
                     table:                                   1
                     td:                                      3
                     title:                                   1
                     tr:                                      1
                     u:                                       1
                     #Total:                                  84
----------------------------------------------------------------------------------------------------
href                 :
                     - https://www.google.fr/imghp?hl=fr&tab=wi
                     - https://maps.google.fr/maps?hl=fr&tab=wl
                     - https://play.google.com/?hl=fr&tab=w8
                     - https://www.youtube.com/?tab=w1
                     - https://news.google.com/?tab=wn
                     - https://mail.google.com/mail/?tab=wm
                     - https://drive.google.com/?tab=wo
                     - https://www.google.fr/intl/fr/about/products?tab=wh
                     - http://www.google.fr/history/optout?hl=fr
                     - /preferences?hl=fr
                     - https://accounts.google.com/ServiceLogin?hl=fr&passive=true&continue=https://www.google.com/&ec=GAZAAQ
                     - /advanced_search?hl=fr&authuser=0
                     - https://www.google.com/setprefs?sig=0_zGenCZBnn1lZ5gO2iPtxE2oL1Gc%3D&hl=en&source=homepage&sa=X&ved=0ahUKEwidlL7vpOz5AhUBuRoKHZSGCAgQ2ZgBCAU
                     - /services/
                     - /intl/fr/about.html
                     - https://www.google.com/setprefdomain?prefdom=FR&prev=https://www.google.fr/&sig=K_A9ocA4gSno7LdKqcAwZfrBfcJm0%3D
                     - /intl/fr/policies/privacy/
                     - /intl/fr/policies/terms/
----------------------------------------------------------------------------------------------------
src                  :
                     - /images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png
----------------------------------------------------------------------------------------------------



====================================================================================================
INFOS
====================================================================================================

whois                :
                     refer:                                   whois.arin.net
                     inetnum:                                 142.0.0.0 - 142.255.255.255
                     organisation:                            Administered by ARIN
                     status:                                  LEGACY
                     whois:                                   whois.arin.net
                     changed:                                 1993-05
                     source:                                  IANA
                     NetRange:                                142.250.0.0 - 142.251.255.255
                     CIDR:                                    142.250.0.0/15
                     NetName:                                 GOOGLE
                     NetHandle:                               NET-142-250-0-0-1
                     Parent:                                  NET142 (NET-142-0-0-0-0)
                     NetType:                                 Direct Allocation
                     OriginAS:                                AS15169
                     Organization:                            Google LLC (GOGL)
                     RegDate:                                 2012-05-24
                     Updated:                                 2012-05-24
                     Ref:                                     https //rdap.arin.net/registry/ip/142.250.0.0
                     OrgName:                                 Google LLC
                     OrgId:                                   GOGL
                     Address:                                 1600 Amphitheatre Parkway
                     City:                                    Mountain View
                     StateProv:                               CA
                     PostalCode:                              94043
                     Country:                                 US
                     RegDate:                                 2000-03-30
                     Updated:                                 2019-10-31
                     Ref:                                     https //rdap.arin.net/registry/entity/GOGL
                     OrgTechHandle:                           ZG39-ARIN
                     OrgTechName:                             Google LLC
                     OrgTechPhone:                            +1-650-253-0000
                     OrgTechEmail:                            arin-contact@google.com
                     OrgTechRef:                              https //rdap.arin.net/registry/entity/ZG39-ARIN
                     OrgAbuseHandle:                          ABUSE5250-ARIN
                     OrgAbuseName:                            Abuse
                     OrgAbusePhone:                           +1-650-253-0000
                     OrgAbuseEmail:                           network-abuse@google.com
                     OrgAbuseRef:                             https //rdap.arin.net/registry/entity/ABUSE5250-ARIN
----------------------------------------------------------------------------------------------------
rev-dns              :
                     - par21s19-in-f4.1e100.net
                     - 68.179.250.142.in-addr.arpa
                     - 142.250.179.68
----------------------------------------------------------------------------------------------------
geo-ip               | US
icmp                 :
                     ttl: 114
                     guessed-os: Windows
                     distance: 14
                     ttl:                                     114
                     guessed-os:                              Windows
                     distance:                                14
----------------------------------------------------------------------------------------------------
threats              :
                     rules.emergingthreats.net:               False
                     cybercrime-tracker.net:                  False
                     easylist.to:                             True
                     github:vaseem-khan-URLcheck:             False
                     github:marcobrandobh_IOCs:               False
                     zonefiles.io:domains:                    False
                     zonefiles.io:ips:                        False
                     urlhaus.abuse.ch:                        False
----------------------------------------------------------------------------------------------------



====================================================================================================
APIVOID
====================================================================================================




====================================================================================================
ABUSE-IP-DATABASE
====================================================================================================

ip                   :
                     ip:                                      142.250.179.68
                     found:                                   found
                     reports:                                 4
                     confidence:                              0%
----------------------------------------------------------------------------------------------------



====================================================================================================
SECURITY-TRAILS
====================================================================================================

history-dns          :
                     message:                                 Invalid authentication credentials
----------------------------------------------------------------------------------------------------
```



