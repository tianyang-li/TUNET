#!/usr/bin/env python

# Tianyang Li 2012

"""
TUNET authentication
"""

import sys
import getopt
import urllib2
import urllib

def logout():
    url = "http://net.tsinghua.edu.cn/cgi-bin/do_logout"
    data = ""
    req = urllib2.Request(url,data)
    resp = urllib2.urlopen(req)
    html = resp.read()
    print html

def login(username, password):

def main(args):

if __name__ == '__main__':
    main(sys.argv[1:])


