#!/usr/bin/python

import sys
import requests as req

class web_scan(object):
    def run(self, args):
        if len(args) < 1:
            return
        if not isinstance(args[0],str):
            return
        if len(args) > 2:
            user=args[1]
            passwd=args[2]
            r = req.get(args[0],auth(user,passwd))
        else:
            r = req.get(args[0])
        if r.status_code != 200:
            print "Error: <status-code:" + r.status_code + ">"
        
        print r.text

ws = web_scan()
ws.run(sys.argv[1:])

