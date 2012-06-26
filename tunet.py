#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tianyang Li 2012

"""
TUNET authentication
"""

import sys
import getopt
import urllib2
import urllib
from getpass import getpass
from hashlib import md5

def usage():
    print >> sys.stderr, "%s" % sys.argv[0],

def logout():
    url = "http://net.tsinghua.edu.cn/cgi-bin/do_logout"
    data = ""
    req = urllib2.Request(url, data)
    resp = urllib2.urlopen(req)
    html = resp.read()
    print html
    return html

def login(username, password):
    url = "http://net.tsinghua.edu.cn/cgi-bin/do_login"
    m = md5()
    m.update(password)
    password = m.hexdigest()
    data = "username=" + username + "&password=" + password + "&drop=" + "0" + "&type=1&n=100"
    req = urllib2.Request(url, data)
    resp = urllib2.urlopen(req)
    html = resp.read()
    print html
    return html
    """
    case "user_tab_error":
        alert("认证程序未启动");
        break;
        
    case "username_error":
        alert("用户名错误");
        document.form1.uname.focus();
        break;
        
    case "user_group_error":
        alert("您的计费组信息不正确");
        break;
        
    case "non_auth_error":
        alert("您无须认证，可直接上网");
        break;
        
    case "password_error":
        alert("密码错误");
        document.form1.pass.focus();
        break;
        
    case "status_error":
        alert("用户已欠费，请尽快充值。");
        break;
        
    case "available_error":
        alert("您的帐号已停用");
        break;
        
    case "delete_error":
        alert("您的帐号已删除");
        break;
        
    case "ip_exist_error":
        alert("IP已存在，请稍后再试。");
        break;
        
    case "usernum_error":
        alert("用户数已达上限");
        break; 
        
    case "online_num_error":
        alert("该帐号的登录人数已超过限额\n如果怀疑帐号被盗用，请联系管理员。");
        break;	
        
    case "mode_error":
        alert("系统已禁止WEB方式登录，请使用客户端");
        break;
        
    case "time_policy_error":
        alert("当前时段不允许连接");
        break;
        
    case "flux_error":
        alert("您的流量已超支");
        break;
        
    case "minutes_error":
        alert("您的时长已超支");
        break;
        
    case "ip_error":
        alert("您的IP地址不合法");
        break;
        
    case "mac_error":
        alert("您的MAC地址不合法");
        break;
        
    case "sync_error":
        alert("您的资料已修改，正在等待同步，请2分钟后再试。");
        break;
        
    case "ip_alloc":
        alert("您不是这个地址的合法拥有者，IP地址已经分配给其它用户。");
        break;
        
    case "ip_invaild":
        alert("您是区内地址，无法使用。");
        break;
    """

def check():
    url = "http://net.tsinghua.edu.cn/cgi-bin/do_login"
    data = "action=check_online"
    req = urllib2.Request(url, data)
    resp = urllib2.urlopen(req)
    html = resp.read()
    print html
    return html

def main():
    username, password = None, None
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'u:p:', ['login', 'logout', 'check'])
    except getopt.GetoptError as err:
        print >> sys.stderr, str(err)
        sys.exit(1)
    set_login = False
    for opt, arg in opts:
        if opt == '-u':
            username = arg
        if opt == '-p':
            password = arg
        if opt == '--logout':
            logout()
            sys.exit(0)
        if opt == '--login':
            set_login = True
        if opt == '--check':
            check()
            sys.exit(0)
    if not set_login:
        print >> sys.stderr, usage()
        sys.exit(1)
    if not username:
        username = getpass("Username: ")
    if not password:
        password = getpass("Password: ")
    login(username, password)

if __name__ == '__main__':
    main()


