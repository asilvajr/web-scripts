#!/usr/bin/python

import sys
import bs4
import requests as req

class web_scan(object):
    def run(self, args):
        if len(args) < 1:
            return
        if not isinstance(args[0],str):
            return
        if len(args) > 3:
            user=args[2]
            passwd=args[3]
            r = req.get(args[0],auth(user,passwd))
        else:
            r = req.get(args[0])
        if r.status_code != 200:
            print "Error: <status-code:" + r.status_code + ">"
        soup = bs4.BeautifulSoup(r.text) 
        if len(args) > 1:
            results = self.search_html(soup, args[1])
        else:
            results = self.search_html(soup)
        
        for res in results:
            print res
 
    def search_html(self, soup, scan_type="links"):
        if scan_type=="links":
            links = soup.select('a[href]')
            return [a.attrs.get('href') for a in links if a.attrs]
        if scan_type=="external-links":
            links = soup.select('a[href^=http]')
            return [a.attrs.get('href') for a in links if a.attrs] 
        if scan_type=="internal-links":
            links = soup.select('a[href^=/]')
            return [a.attrs.get('href') for a in links if a.attrs] 

ws = web_scan()
ws.run(sys.argv[1:])

