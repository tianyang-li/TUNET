#!/usr/bin/env python

# Tianyang Li 2012

"""
TUNET authentication
"""

import sys
import getopt
import urllib2
import urllib
from getpass import getpass

def usage():
    print >> sys.stderr, "%s" % sys.argv[0],

def logout():
    url = "http://net.tsinghua.edu.cn/cgi-bin/do_logout"
    data = ""
    req = urllib2.Request(url,data)
    resp = urllib2.urlopen(req)
    html = resp.read()
    print html

def login(username, password):

def main():
    username, password = None, None
    try:
        opts, args = getopt.getopt(sys.argv[1:])
    except getopt.GetoptError as err:
        print >> sys.stderr, str(err)
        sys.exit(1)
    if username == None:
        username = getpass("Username: ")
    if password == None:
        password = getpass("Password: ")

if __name__ == '__main__':
    main()


