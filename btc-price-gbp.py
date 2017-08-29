#!/usr/bin/python
# coding=utf-8
#
# <bitbar.title>Bitcoin Ticker</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>laxdog</bitbar.author>
# <bitbar.author.github>laxdog</bitbar.author.github>
# <bitbar.desc>Displays current Bitcoin price in £</bitbar.desc>
#
# by laxdog

import json
from urllib import urlopen
url = urlopen('https://blockchain.info/ticker').read()
currency = 'GBP'
live_url = urlopen('https://blockchain.info/tobtc?currency={0}&value=1'.format(currency))

result = json.loads(url)
data = result[currency]
live_data = 1 / float(live_url.read())


def flow():
    if live_data == data['15m']:
        print ('⊜ £%.2f' % float(live_data))
    elif live_data > data['15m']:
        print ('▼ £%.2f' % float(live_data))
    else:
        print ('▲ £%.2f' % float(live_data))


flow()
