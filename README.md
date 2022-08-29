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
python investigatør.py print 7580d3d305033fac91cca75ba5b0c4dc.json
```

Result :

```json
{   'abuse': {   'ip': {   'confidence': '-',
                           'found': 'not found',
                           'ip': '146.59.151.177',
                           'reports': '-'}},
    'apivoid': {   'email': {   'elapsed_time': '0.00',
                                'error': 'API key is not valid'},
                   'urlrep': {   'elapsed_time': '0.00',
                                 'error': 'API key is not valid'}},
    'html': {   'href': [   'favicon.png',
                            'css/font.css',
                            'css/main.css',
                            'css/hr.css',
                            'css/views.css',
                            'css/table.css',
                            'css/search.css',
                            'css/footer-distributed-with-address-and-phones.css',
                            'css/font-awesome.min.css',
                            'css/news.css',
                            'css/resources.css',
                            'css/hacking.css',
                            'css/maps.css',
                            'css/blog.css',
                            'css/home.css',
                            'css/articles.css',
                            'css/mobile.css',
                            'css/overflow.css',
                            'https://www.exemple.com/html/index.php',
                            'https://www.exemple.com/html/articles.php',
                            'https://www.exemple.com/html/news.php',
                            'https://www.exemple.com/html/vulns.php',
                            'https://www.exemple.com/html/resources.php',
                            'https://www.exemple.com/html/blog.php',
                            'seek.php',
                            'https://www.exemple.com/html/articles.php?d=3',
                            'article.php?id=1908',
                            'article.php?id=1901',
                            'article.php?id=1899',
                            'article.php?id=1898',
                            'https://www.exemple.com/html/news.php',
                            'https://www.exemple.com/html/blog.php?year=2020',
                            'https://www.exemple.com/banned.php',
                            'index.php',
                            'seek.php',
                            'blog.php',
                            'concepts.php',
                            'news.php',
                            'mailto:contact@exemple.com',
                            'mailto:contact@exemple.com',
                            'https://www.youtube.com/channel/UCoA5WtYlz11fprxNoU8-Rsw',
                            'https://twitter.com/exemple42',
                            'https://github.com/exemple42'],
                'src': [   'img/NavTop/index_green.png',
                           'img/NavTop/articles_green.png',
                           'img/NavTop/news_green.png',
                           'img/NavTop/vulns_green.png',
                           'img/NavTop/resources_green.png',
                           'img/NavTop/blog_green.png',
                           'img/Home/search_grey.png',
                           'pictures/sudomy.png',
                           'pictures/nmap-faster.jpg',
                           'pictures/keyboard_alt.jpg',
                           'img/NavTop/index_grey.png'],
                'tags': {   '#Total': 233,
                            'a': 38,
                            'b': 7,
                            'body': 1,
                            'br': 47,
                            'center': 4,
                            'div': 41,
                            'footer': 1,
                            'form': 2,
                            'h2': 1,
                            'h3': 4,
                            'head': 1,
                            'header': 1,
                            'hr': 23,
                            'html': 1,
                            'i': 14,
                            'img': 11,
                            'input': 2,
                            'link': 18,
                            'meta': 3,
                            'p': 7,
                            'span': 2,
                            'style': 3,
                            'title': 1}},
    'infos': {   'geo-ip': 'NO',
                 'icmp': {   'icmp': {   'distance': '18',
                                         'guessed-os': 'Linux',
                                         'ttl': 46}},
                 'rev-dns': [   'vps-b5d0b791.vps.ovh.net',
                                '177.151.59.146.in-addr.arpa',
                                '146.59.151.177'],
                 'threats': [   {'rules.emergingthreats.net': 'False'},
                                {'cybercrime-tracker.net': 'False'},
                                {'easylist.to': 'False'},
                                {'github:vaseem-khan-URLcheck': 'False'},
                                {'github:marcobrandobh_IOCs': 'False'},
                                {'zonefiles.io:domains': 'False'},
                                {'zonefiles.io:ips': 'False'},
                                {'urlhaus.abuse.ch': 'False'}],
                 'whois': [   {'refer': 'whois.arin.net'},
                              {   'inetnum': '146.0.0.0 - 146.255.255.255',
                                  'organisation': 'Administered by ARIN',
                                  'status': 'LEGACY'},
                              {'whois': 'whois.arin.net'},
                              {'changed': '1993-05', 'source': 'IANA'},
                              {   'CIDR': '146.59.0.0/16',
                                  'NetHandle': 'NET-146-59-0-0-1',
                                  'NetName': 'RIPE-ERX-146-59-0-0',
                                  'NetRange': '146.59.0.0 - 146.59.255.255',
                                  'NetType': 'Early Registrations, Transferred '
                                             'to RIPE NCC',
                                  'Organization': 'RIPE Network Coordination '
                                                  'Centre (RIPE)',
                                  'Parent': 'NET146 (NET-146-0-0-0-0)',
                                  'Ref': 'https '
                                         '//rdap.arin.net/registry/ip/146.59.0.0',
                                  'RegDate': '2004-02-04',
                                  'Updated': '2004-02-04'},
                              {'ResourceLink': 'whois.ripe.net'},
                              {   'Address': 'P.O. Box 10096',
                                  'City': 'Amsterdam',
                                  'Country': 'NL',
                                  'OrgId': 'RIPE',
                                  'OrgName': 'RIPE Network Coordination Centre',
                                  'PostalCode': '1001EB',
                                  'Ref': 'https '
                                         '//rdap.arin.net/registry/entity/RIPE',
                                  'Updated': '2013-07-29'},
                              {   'ReferralServer': 'whois //whois.ripe.net',
                                  'ResourceLink': 'https '
                                                  '//apps.db.ripe.net/search/query.html'},
                              {   'OrgAbuseEmail': 'abuse@ripe.net',
                                  'OrgAbuseHandle': 'ABUSE3850-ARIN',
                                  'OrgAbuseName': 'Abuse Contact',
                                  'OrgAbusePhone': '+31205354444',
                                  'OrgAbuseRef': 'https '
                                                 '//rdap.arin.net/registry/entity/ABUSE3850-ARIN'},
                              {   'OrgTechEmail': 'hostmaster@ripe.net',
                                  'OrgTechHandle': 'RNO29-ARIN',
                                  'OrgTechName': 'RIPE NCC Operations',
                                  'OrgTechPhone': '+31 20 535 4444',
                                  'OrgTechRef': 'https '
                                                '//rdap.arin.net/registry/entity/RNO29-ARIN'},
                              {   'admin-c': 'OTC2-RIPE',
                                  'country': 'FR',
                                  'created': '2020-09-24T08 00 10Z',
                                  'geoloc': '50.98721 2.120542',
                                  'inetnum': '146.59.150.0 - 146.59.151.255',
                                  'last-modified': '2020-09-24T08 00 10Z',
                                  'mnt-by': 'OVH-MNT',
                                  'netname': 'VPS-GRA8',
                                  'org': 'ORG-OS3-RIPE',
                                  'source': 'RIPE',
                                  'status': 'LEGACY',
                                  'tech-c': 'OTC2-RIPE'},
                              {   'abuse-c': 'AR15333-RIPE',
                                  'address': 'FRANCE',
                                  'admin-c': 'GM84-RIPE',
                                  'country': 'FR',
                                  'created': '2004-04-17T11 23 17Z',
                                  'last-modified': '2020-12-16T10 24 51Z',
                                  'mnt-by': 'OVH-MNT',
                                  'mnt-ref': 'RIPE-NCC-HM-MNT',
                                  'org-name': 'OVH SAS',
                                  'org-type': 'LIR',
                                  'organisation': 'ORG-OS3-RIPE',
                                  'phone': '+33972101007',
                                  'source': 'RIPE # Filtered'},
                              {   'abuse-mailbox': 'abuse@ovh.net',
                                  'address': 'France',
                                  'admin-c': 'OK217-RIPE',
                                  'created': '2004-01-28T17 42 29Z',
                                  'last-modified': '2014-09-05T10 47 15Z',
                                  'mnt-by': 'OVH-MNT',
                                  'nic-hdl': 'OTC2-RIPE',
                                  'role': 'OVH Technical Contact',
                                  'source': 'RIPE # Filtered',
                                  'tech-c': 'SL10162-RIPE'},
                              {   'created': '2020-09-03T12 57 00Z',
                                  'last-modified': '2020-09-03T12 57 00Z',
                                  'mnt-by': 'OVH-MNT',
                                  'origin': 'AS16276',
                                  'route': '146.59.0.0/16',
                                  'source': 'RIPE'}]},
    'ip-info': {   'city': 'Paris',
                   'country': 'FR',
                   'hostname': 'vps-b5d0b791.vps.ovh.net',
                   'ip': '146.59.151.177',
                   'loc': '48.8534,2.3488',
                   'org': 'AS16276 OVH SAS',
                   'postal': '75000',
                   'readme': 'https://ipinfo.io/missingauth',
                   'region': 'Île-de-France',
                   'timezone': 'Europe/Paris'},
    'security-trails': {   'history-dns': {   'message': 'Invalid '
                                                         'authentication '
                                                         'credentials'}},
    'shodan': {   'ip': 'Error: no valid authentication',
                  'raw': 'Error: no valid authentication'},
    'ssl': {   'tls': {   'altnames': ['www.exemple.com'],
                          'is_expired': False,
                          'not-after': '2022/09/28@19:34',
                          'not-before': '2022/06/30@19:34',
                          'subject': '/CN=www.exemple.com'}},
    'target': {   'host': 'www.exemple.com',
                  'ip': '146.59.151.177',
                  'port': 443,
                  'url': 'https://www.exemple.com/html/'},
    'trendmicro': {}}

```


### yaml


```sh
python investigatør.py to-yaml 7580d3d305033fac91cca75ba5b0c4dc.json
```

Result :

```yaml
abuse:
  ip:
    confidence: '-'
    found: not found
    ip: 146.59.151.177
    reports: '-'
apivoid:
  email:
    elapsed_time: '0.00'
    error: API key is not valid
  urlrep:
    elapsed_time: '0.00'
    error: API key is not valid
html:
  href:
  - favicon.png
  - css/font.css
  - css/main.css
  - css/hr.css
  - css/views.css
  - css/table.css
  - css/search.css
  - css/footer-distributed-with-address-and-phones.css
  - css/font-awesome.min.css
  - css/news.css
  - css/resources.css
  - css/hacking.css
  - css/maps.css
  - css/blog.css
  - css/home.css
  - css/articles.css
  - css/mobile.css
  - css/overflow.css
  - https://www.secureinfo.eu/html/index.php
  - https://www.secureinfo.eu/html/articles.php
  - https://www.secureinfo.eu/html/news.php
  - https://www.secureinfo.eu/html/vulns.php
  - https://www.secureinfo.eu/html/resources.php
  - https://www.secureinfo.eu/html/blog.php
  - seek.php
  - https://www.secureinfo.eu/html/articles.php?d=3
  - article.php?id=1908
  - article.php?id=1901
  - article.php?id=1899
  - article.php?id=1898
  - https://www.secureinfo.eu/html/news.php
  - 'https://www.01net.com/actualites/android-le-cheval-de-troie-bancaire-cerberus-regagne-en-intensite-1977482.html         '
  - https://www.ssi.gouv.fr/actualite/securite-et-infogerance-du-nouveau-pour-le-futur-referentiel-pams-de-lanssi/
  - https://www.datasecuritybreach.fr/securiser-active-directory/
  - https://www.fredzone.org/amelia-elizabeth-dyer-ou-lhistoire-de-la-terrible-ogresse-de-reading-988#utm_source=feed&utm_medium=feed&utm_campaign=feed
  - http://www.globalsecuritymag.fr/Rampant-Kitten-a-Six-year-Iranian,20200918,102889.html
  - https://korben.info/milkytracker-tracker-xm.html
  - https://www.laquadrature.net/2020/09/15/usa-lettre-ouverte-contre-la-censure-de-media-anarchistes/
  - https://www.lemonde.fr/emploi/article/2020/09/18/quand-amazon-recrutait-des-analystes-en-renseignements-pour-eviter-la-syndicalisation_6052669_1698637.html
  - https://www.usine-digitale.fr/article/leocare-leve-2-2-millions-d-euros-pour-devenir-l-assureur-de-toute-la-famille.N1006604
  - https://vigilance.fr/vulnerabilite/PHP-multiples-vulnerabilites-31183
  - https://www.zataz.com/pirates-malaisiens-arretes-les-complices-chinois-dans-la-nature/
  - https://www.secureinfo.eu/html/blog.php?year=2020
  - https://www.secureinfo.eu/banned.php
  - index.php
  - seek.php
  - blog.php
  - concepts.php
  - news.php
  - mailto:contact@secureinfo.eu
  - mailto:contact@secureinfo.eu
  - https://www.youtube.com/channel/UCoA5WtYlz11fprxNoU8-Rsw
  - https://twitter.com/secureinfo42
  - https://www.root-me.org/Saelyx-1610?lang=fr#76bf5ab6ad60bc1802de9a0b5d2b2cb9
  - https://github.com/secureinfo42
  src:
  - img/NavTop/index_green.png
  - img/NavTop/articles_green.png
  - img/NavTop/news_green.png
  - img/NavTop/vulns_green.png
  - img/NavTop/resources_green.png
  - img/NavTop/blog_green.png
  - img/Home/search_grey.png
  - pictures/sudomy.png
  - pictures/nmap-faster.jpg
  - pictures/keyboard_alt.jpg
  - img/NavTop/index_grey.png
  tags:
    '#Total': 233
    a: 38
    b: 7
    body: 1
    br: 47
    center: 4
    div: 41
    footer: 1
    form: 2
    h2: 1
    h3: 4
    head: 1
    header: 1
    hr: 23
    html: 1
    i: 14
    img: 11
    input: 2
    link: 18
    meta: 3
    p: 7
    span: 2
    style: 3
    title: 1
infos:
  geo-ip: 'NO'
  icmp:
    icmp:
      distance: '18'
      guessed-os: Linux
      ttl: 46
  rev-dns:
  - vps-b5d0b791.vps.ovh.net
  - 177.151.59.146.in-addr.arpa
  - 146.59.151.177
  threats:
  - rules.emergingthreats.net: 'False'
  - cybercrime-tracker.net: 'False'
  - easylist.to: 'False'
  - github:vaseem-khan-URLcheck: 'False'
  - github:marcobrandobh_IOCs: 'False'
  - zonefiles.io:domains: 'False'
  - zonefiles.io:ips: 'False'
  - urlhaus.abuse.ch: 'False'
  whois:
  - refer: whois.arin.net
  - inetnum: 146.0.0.0 - 146.255.255.255
    organisation: Administered by ARIN
    status: LEGACY
  - whois: whois.arin.net
  - changed: 1993-05
    source: IANA
  - CIDR: 146.59.0.0/16
    NetHandle: NET-146-59-0-0-1
    NetName: RIPE-ERX-146-59-0-0
    NetRange: 146.59.0.0 - 146.59.255.255
    NetType: Early Registrations, Transferred to RIPE NCC
    Organization: RIPE Network Coordination Centre (RIPE)
    Parent: NET146 (NET-146-0-0-0-0)
    Ref: https //rdap.arin.net/registry/ip/146.59.0.0
    RegDate: '2004-02-04'
    Updated: '2004-02-04'
  - ResourceLink: whois.ripe.net
  - Address: P.O. Box 10096
    City: Amsterdam
    Country: NL
    OrgId: RIPE
    OrgName: RIPE Network Coordination Centre
    PostalCode: 1001EB
    Ref: https //rdap.arin.net/registry/entity/RIPE
    Updated: '2013-07-29'
  - ReferralServer: whois //whois.ripe.net
    ResourceLink: https //apps.db.ripe.net/search/query.html
  - OrgAbuseEmail: abuse@ripe.net
    OrgAbuseHandle: ABUSE3850-ARIN
    OrgAbuseName: Abuse Contact
    OrgAbusePhone: '+31205354444'
    OrgAbuseRef: https //rdap.arin.net/registry/entity/ABUSE3850-ARIN
  - OrgTechEmail: hostmaster@ripe.net
    OrgTechHandle: RNO29-ARIN
    OrgTechName: RIPE NCC Operations
    OrgTechPhone: +31 20 535 4444
    OrgTechRef: https //rdap.arin.net/registry/entity/RNO29-ARIN
  - admin-c: OTC2-RIPE
    country: FR
    created: 2020-09-24T08 00 10Z
    geoloc: 50.98721 2.120542
    inetnum: 146.59.150.0 - 146.59.151.255
    last-modified: 2020-09-24T08 00 10Z
    mnt-by: OVH-MNT
    netname: VPS-GRA8
    org: ORG-OS3-RIPE
    source: RIPE
    status: LEGACY
    tech-c: OTC2-RIPE
  - abuse-c: AR15333-RIPE
    address: FRANCE
    admin-c: GM84-RIPE
    country: FR
    created: 2004-04-17T11 23 17Z
    last-modified: 2020-12-16T10 24 51Z
    mnt-by: OVH-MNT
    mnt-ref: RIPE-NCC-HM-MNT
    org-name: OVH SAS
    org-type: LIR
    organisation: ORG-OS3-RIPE
    phone: '+33972101007'
    source: 'RIPE # Filtered'
  - abuse-mailbox: abuse@ovh.net
    address: France
    admin-c: OK217-RIPE
    created: 2004-01-28T17 42 29Z
    last-modified: 2014-09-05T10 47 15Z
    mnt-by: OVH-MNT
    nic-hdl: OTC2-RIPE
    role: OVH Technical Contact
    source: 'RIPE # Filtered'
    tech-c: SL10162-RIPE
  - created: 2020-09-03T12 57 00Z
    last-modified: 2020-09-03T12 57 00Z
    mnt-by: OVH-MNT
    origin: AS16276
    route: 146.59.0.0/16
    source: RIPE
ip-info:
  city: Paris
  country: FR
  hostname: vps-b5d0b791.vps.ovh.net
  ip: 146.59.151.177
  loc: 48.8534,2.3488
  org: AS16276 OVH SAS
  postal: '75000'
  readme: https://ipinfo.io/missingauth
  region: "\xCEle-de-France"
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
    - www.secureinfo.eu
    is_expired: false
    not-after: 2022/09/28@19:34
    not-before: 2022/06/30@19:34
    subject: /CN=www.secureinfo.eu
target:
  host: www.secureinfo.eu
  ip: 146.59.151.177
  port: 443
  url: https://www.secureinfo.eu/html/
trendmicro: {}
```

### table

```sh
python investigatør.py table 7580d3d305033fac91cca75ba5b0c4dc.json
```

```

[1;32m
====================================================================================================
TARGET
====================================================================================================
[0m
[1;35murl                 [0m [1;30m|[0m https://www.secureinfo.eu/html/
[1;35mhost                [0m [1;30m|[0m www.secureinfo.eu
[1;35mip                  [0m [1;30m|[0m 146.59.151.177


[1;32m
====================================================================================================
IP-INFO
====================================================================================================
[0m
[1;35mip                  [0m [1;30m|[0m 146.59.151.177
[1;35mhostname            [0m [1;30m|[0m vps-b5d0b791.vps.ovh.net
[1;35mcity                [0m [1;30m|[0m Paris
[1;35mregion              [0m [1;30m|[0m Île-de-France
[1;35mcountry             [0m [1;30m|[0m FR
[1;35mloc                 [0m [1;30m|[0m 48.8534,2.3488
[1;35morg                 [0m [1;30m|[0m AS16276 OVH SAS
[1;35mpostal              [0m [1;30m|[0m 75000
[1;35mtimezone            [0m [1;30m|[0m Europe/Paris
[1;35mreadme              [0m [1;30m|[0m https://ipinfo.io/missingauth


[1;32m
====================================================================================================
SSL
====================================================================================================
[0m
[1;35mnot-before          [0m [1;30m|[0m 2022/06/30@19:34
[1;35mnot-after           [0m [1;30m|[0m 2022/09/28@19:34
[1;35msubject             [0m [1;30m|[0m /CN=www.secureinfo.eu
[1;35maltnames             :[0m
                     [1;35m-[0m www.secureinfo.eu
[1;30m----------------------------------------------------------------------------------------------------[0m


[1;32m
====================================================================================================
HTML
====================================================================================================
[0m
[1;35mtags                 :[0m
                     [0;34ma:                                      [0m 38
                     [0;34mb:                                      [0m 7
                     [0;34mbody:                                   [0m 1
                     [0;34mbr:                                     [0m 47
                     [0;34mcenter:                                 [0m 4
                     [0;34mdiv:                                    [0m 41
                     [0;34mfooter:                                 [0m 1
                     [0;34mform:                                   [0m 2
                     [0;34mh2:                                     [0m 1
                     [0;34mh3:                                     [0m 4
                     [0;34mhead:                                   [0m 1
                     [0;34mheader:                                 [0m 1
                     [0;34mhr:                                     [0m 23
                     [0;34mhtml:                                   [0m 1
                     [0;34mi:                                      [0m 14
                     [0;34mimg:                                    [0m 11
                     [0;34minput:                                  [0m 2
                     [0;34mlink:                                   [0m 18
                     [0;34mmeta:                                   [0m 3
                     [0;34mp:                                      [0m 7
                     [0;34mspan:                                   [0m 2
                     [0;34mstyle:                                  [0m 3
                     [0;34mtitle:                                  [0m 1
                     [0;34m#Total:                                 [0m 233
[1;30m----------------------------------------------------------------------------------------------------[0m
[1;35mhref                 :[0m
                     [1;35m-[0m favicon.png
                     [1;35m-[0m css/font.css
                     [1;35m-[0m css/main.css
                     [1;35m-[0m css/hr.css
                     [1;35m-[0m css/views.css
                     [1;35m-[0m css/table.css
                     [1;35m-[0m css/search.css
                     [1;35m-[0m css/footer-distributed-with-address-and-phones.css
                     [1;35m-[0m css/font-awesome.min.css
                     [1;35m-[0m css/news.css
                     [1;35m-[0m css/resources.css
                     [1;35m-[0m css/hacking.css
                     [1;35m-[0m css/maps.css
                     [1;35m-[0m css/blog.css
                     [1;35m-[0m css/home.css
                     [1;35m-[0m css/articles.css
                     [1;35m-[0m css/mobile.css
                     [1;35m-[0m css/overflow.css
                     [1;35m-[0m https://www.secureinfo.eu/html/index.php
                     [1;35m-[0m https://www.secureinfo.eu/html/articles.php
                     [1;35m-[0m https://www.secureinfo.eu/html/news.php
                     [1;35m-[0m https://www.secureinfo.eu/html/vulns.php
                     [1;35m-[0m https://www.secureinfo.eu/html/resources.php
                     [1;35m-[0m https://www.secureinfo.eu/html/blog.php
                     [1;35m-[0m seek.php
                     [1;35m-[0m https://www.secureinfo.eu/html/articles.php?d=3
                     [1;35m-[0m article.php?id=1908
                     [1;35m-[0m article.php?id=1901
                     [1;35m-[0m article.php?id=1899
                     [1;35m-[0m article.php?id=1898
                     [1;35m-[0m https://www.secureinfo.eu/html/news.php
                     [1;35m-[0m https://www.01net.com/actualites/android-le-cheval-de-troie-bancaire-cerberus-regagne-en-intensite-1977482.html         
                     [1;35m-[0m https://www.ssi.gouv.fr/actualite/securite-et-infogerance-du-nouveau-pour-le-futur-referentiel-pams-de-lanssi/
                     [1;35m-[0m https://www.datasecuritybreach.fr/securiser-active-directory/
                     [1;35m-[0m https://www.fredzone.org/amelia-elizabeth-dyer-ou-lhistoire-de-la-terrible-ogresse-de-reading-988#utm_source=feed&utm_medium=feed&utm_campaign=feed
                     [1;35m-[0m http://www.globalsecuritymag.fr/Rampant-Kitten-a-Six-year-Iranian,20200918,102889.html
                     [1;35m-[0m https://korben.info/milkytracker-tracker-xm.html
                     [1;35m-[0m https://www.laquadrature.net/2020/09/15/usa-lettre-ouverte-contre-la-censure-de-media-anarchistes/
                     [1;35m-[0m https://www.lemonde.fr/emploi/article/2020/09/18/quand-amazon-recrutait-des-analystes-en-renseignements-pour-eviter-la-syndicalisation_6052669_1698637.html
                     [1;35m-[0m https://www.usine-digitale.fr/article/leocare-leve-2-2-millions-d-euros-pour-devenir-l-assureur-de-toute-la-famille.N1006604
                     [1;35m-[0m https://vigilance.fr/vulnerabilite/PHP-multiples-vulnerabilites-31183
                     [1;35m-[0m https://www.zataz.com/pirates-malaisiens-arretes-les-complices-chinois-dans-la-nature/
                     [1;35m-[0m https://www.secureinfo.eu/html/blog.php?year=2020
                     [1;35m-[0m https://www.secureinfo.eu/banned.php
                     [1;35m-[0m index.php
                     [1;35m-[0m seek.php
                     [1;35m-[0m blog.php
                     [1;35m-[0m concepts.php
                     [1;35m-[0m news.php
                     [1;35m-[0m mailto:contact@secureinfo.eu
                     [1;35m-[0m mailto:contact@secureinfo.eu
                     [1;35m-[0m https://www.youtube.com/channel/UCoA5WtYlz11fprxNoU8-Rsw
                     [1;35m-[0m https://twitter.com/secureinfo42
                     [1;35m-[0m https://www.root-me.org/Saelyx-1610?lang=fr#76bf5ab6ad60bc1802de9a0b5d2b2cb9
                     [1;35m-[0m https://github.com/secureinfo42
[1;30m----------------------------------------------------------------------------------------------------[0m
[1;35msrc                  :[0m
                     [1;35m-[0m img/NavTop/index_green.png
                     [1;35m-[0m img/NavTop/articles_green.png
                     [1;35m-[0m img/NavTop/news_green.png
                     [1;35m-[0m img/NavTop/vulns_green.png
                     [1;35m-[0m img/NavTop/resources_green.png
                     [1;35m-[0m img/NavTop/blog_green.png
                     [1;35m-[0m img/Home/search_grey.png
                     [1;35m-[0m pictures/sudomy.png
                     [1;35m-[0m pictures/nmap-faster.jpg
                     [1;35m-[0m pictures/keyboard_alt.jpg
                     [1;35m-[0m img/NavTop/index_grey.png
[1;30m----------------------------------------------------------------------------------------------------[0m


[1;32m
====================================================================================================
INFOS
====================================================================================================
[0m
[1;35mwhois                :[0m
                     [0;34mrefer:                                  [0m whois.arin.net
                     [0;34minetnum:                                [0m 146.0.0.0 - 146.255.255.255
                     [0;34morganisation:                           [0m Administered by ARIN
                     [0;34mstatus:                                 [0m LEGACY
                     [0;34mwhois:                                  [0m whois.arin.net
                     [0;34mchanged:                                [0m 1993-05
                     [0;34msource:                                 [0m IANA
                     [0;34mNetRange:                               [0m 146.59.0.0 - 146.59.255.255
                     [0;34mCIDR:                                   [0m 146.59.0.0/16
                     [0;34mNetName:                                [0m RIPE-ERX-146-59-0-0
                     [0;34mNetHandle:                              [0m NET-146-59-0-0-1
                     [0;34mParent:                                 [0m NET146 (NET-146-0-0-0-0)
                     [0;34mNetType:                                [0m Early Registrations, Transferred to RIPE NCC
                     [0;34mOrganization:                           [0m RIPE Network Coordination Centre (RIPE)
                     [0;34mRegDate:                                [0m 2004-02-04
                     [0;34mUpdated:                                [0m 2004-02-04
                     [0;34mRef:                                    [0m https //rdap.arin.net/registry/ip/146.59.0.0
                     [0;34mResourceLink:                           [0m whois.ripe.net
                     [0;34mOrgName:                                [0m RIPE Network Coordination Centre
                     [0;34mOrgId:                                  [0m RIPE
                     [0;34mAddress:                                [0m P.O. Box 10096
                     [0;34mCity:                                   [0m Amsterdam
                     [0;34mPostalCode:                             [0m 1001EB
                     [0;34mCountry:                                [0m NL
                     [0;34mUpdated:                                [0m 2013-07-29
                     [0;34mRef:                                    [0m https //rdap.arin.net/registry/entity/RIPE
                     [0;34mReferralServer:                         [0m whois //whois.ripe.net
                     [0;34mResourceLink:                           [0m https //apps.db.ripe.net/search/query.html
                     [0;34mOrgAbuseHandle:                         [0m ABUSE3850-ARIN
                     [0;34mOrgAbuseName:                           [0m Abuse Contact
                     [0;34mOrgAbusePhone:                          [0m +31205354444
                     [0;34mOrgAbuseEmail:                          [0m abuse@ripe.net
                     [0;34mOrgAbuseRef:                            [0m https //rdap.arin.net/registry/entity/ABUSE3850-ARIN
                     [0;34mOrgTechHandle:                          [0m RNO29-ARIN
                     [0;34mOrgTechName:                            [0m RIPE NCC Operations
                     [0;34mOrgTechPhone:                           [0m +31 20 535 4444
                     [0;34mOrgTechEmail:                           [0m hostmaster@ripe.net
                     [0;34mOrgTechRef:                             [0m https //rdap.arin.net/registry/entity/RNO29-ARIN
                     [0;34minetnum:                                [0m 146.59.150.0 - 146.59.151.255
                     [0;34mnetname:                                [0m VPS-GRA8
                     [0;34mcountry:                                [0m FR
                     [0;34morg:                                    [0m ORG-OS3-RIPE
                     [0;34mgeoloc:                                 [0m 50.98721 2.120542
                     [0;34madmin-c:                                [0m OTC2-RIPE
                     [0;34mtech-c:                                 [0m OTC2-RIPE
                     [0;34mstatus:                                 [0m LEGACY
                     [0;34mmnt-by:                                 [0m OVH-MNT
                     [0;34mcreated:                                [0m 2020-09-24T08 00 10Z
                     [0;34mlast-modified:                          [0m 2020-09-24T08 00 10Z
                     [0;34msource:                                 [0m RIPE
                     [0;34morganisation:                           [0m ORG-OS3-RIPE
                     [0;34morg-name:                               [0m OVH SAS
                     [0;34mcountry:                                [0m FR
                     [0;34morg-type:                               [0m LIR
                     [0;34maddress:                                [0m FRANCE
                     [0;34mphone:                                  [0m +33972101007
                     [0;34madmin-c:                                [0m GM84-RIPE
                     [0;34mabuse-c:                                [0m AR15333-RIPE
                     [0;34mmnt-ref:                                [0m RIPE-NCC-HM-MNT
                     [0;34mmnt-by:                                 [0m OVH-MNT
                     [0;34mcreated:                                [0m 2004-04-17T11 23 17Z
                     [0;34mlast-modified:                          [0m 2020-12-16T10 24 51Z
                     [0;34msource:                                 [0m RIPE # Filtered
                     [0;34mrole:                                   [0m OVH Technical Contact
                     [0;34maddress:                                [0m France
                     [0;34madmin-c:                                [0m OK217-RIPE
                     [0;34mtech-c:                                 [0m SL10162-RIPE
                     [0;34mnic-hdl:                                [0m OTC2-RIPE
                     [0;34mabuse-mailbox:                          [0m abuse@ovh.net
                     [0;34mmnt-by:                                 [0m OVH-MNT
                     [0;34mcreated:                                [0m 2004-01-28T17 42 29Z
                     [0;34mlast-modified:                          [0m 2014-09-05T10 47 15Z
                     [0;34msource:                                 [0m RIPE # Filtered
                     [0;34mroute:                                  [0m 146.59.0.0/16
                     [0;34morigin:                                 [0m AS16276
                     [0;34mmnt-by:                                 [0m OVH-MNT
                     [0;34mcreated:                                [0m 2020-09-03T12 57 00Z
                     [0;34mlast-modified:                          [0m 2020-09-03T12 57 00Z
                     [0;34msource:                                 [0m RIPE
[1;30m----------------------------------------------------------------------------------------------------[0m
[1;35mrev-dns              :[0m
                     [1;35m-[0m vps-b5d0b791.vps.ovh.net
                     [1;35m-[0m 177.151.59.146.in-addr.arpa
                     [1;35m-[0m 146.59.151.177
[1;30m----------------------------------------------------------------------------------------------------[0m
[1;35mgeo-ip              [0m [1;30m|[0m NO
[1;35micmp                 :[0m
                     [0;31mttl:[0m 46
                     [0;31mguessed-os:[0m Linux
                     [0;31mdistance:[0m 18
                     [0;34mttl:                                    [0m 46
                     [0;34mguessed-os:                             [0m Linux
                     [0;34mdistance:                               [0m 18
[1;30m----------------------------------------------------------------------------------------------------[0m
[1;35mthreats              :[0m
                     [0;34mrules.emergingthreats.net:              [0m False
                     [0;34mcybercrime-tracker.net:                 [0m False
                     [0;34measylist.to:                            [0m False
                     [0;34mgithub:vaseem-khan-URLcheck:            [0m False
                     [0;34mgithub:marcobrandobh_IOCs:              [0m False
                     [0;34mzonefiles.io:domains:                   [0m False
                     [0;34mzonefiles.io:ips:                       [0m False
                     [0;34murlhaus.abuse.ch:                       [0m False
[1;30m----------------------------------------------------------------------------------------------------[0m


[1;32m
====================================================================================================
APIVOID
====================================================================================================
[0m


[1;32m
====================================================================================================
ABUSE-IP-DATABASE
====================================================================================================
[0m
[1;35mip                   :[0m
                     [0;34mip:                                     [0m 146.59.151.177
                     [0;34mfound:                                  [0m not found
                     [0;34mreports:                                [0m -
                     [0;34mconfidence:                             [0m -
[1;30m----------------------------------------------------------------------------------------------------[0m


[1;32m
====================================================================================================
SECURITY-TRAILS
====================================================================================================
[0m
[1;35mhistory-dns          :[0m
                     [0;34mmessage:                                [0m Invalid authentication credentials
[1;30m----------------------------------------------------------------------------------------------------[0m

```



