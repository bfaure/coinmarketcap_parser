
# script to pull the most recent price data for Gridcoin from
# the following url: https://coinmarketcap.com/currencies/gridcoin/
# it will then compute the value of my holdings where I own
# a total of 400 Gridcoin.
cur_holdings=400

import urllib2


resp = urllib2.urlopen('https://coinmarketcap.com/currencies/gridcoin/')
html = resp.read()


tag="<span class=\"text-large2\" data-currency-value>"
data_idx=html.find(tag)

if data_idx!=-1:
	cur_price=html[data_idx+len(tag):data_idx+len(tag)+8]
	cur_price=float(cur_price)

	print "\n==============================\n"
	print "Portfolio Value: $%0.2f"%(cur_price*cur_holdings)
	print "(Assuming holdings of %d GRC)"%cur_holdings
	print "(Data parsed from coinmarketcap.com)"
	print "\n==============================\n"

else:
	print "Tag not found, printing stuff we got..."
	print html
