#!/usr/bin/env python
# -*- coding: utf-8 -*-

# wechat
WECHAT_CORPID = ''      # 企业ID
WECHAT_SECRET = ''    # 通讯录secrete
WECHAT_DEPART_ID = 2  # 部门id
WECHAT_FETCH_CHILD = 1  # 是否递归获取子部门(1-递归获取，0-只获取本部门)


# ldap
LDAP_HOST = '192.168.9.248' 
LDAP_PORT = 389
LDAP_BINDDN = 'cn=admin,dc=example,dc=org' 
LDAP_BINDPW = 'admin'
LDAP_BASE = 'dc=example,dc=org'
LDAP_USER_OU = 'ou=user'  # 用户所在的ou，需要提前创建
LDAP_GROUP_OU = 'ou=group' # 部门所在的ou，需要提前创建

# mail
SMTP_HOST = 'smtp.exmail.qq.com'
SMTP_PORT = 465
SMTP_USER = ''
SMTP_PASSWD = ''

MESSAGE = """
<p>LDAP账号可用于登入 Gitlab、jumpserver、openvpn、jira 、wiki、showdoc、yearning等平台</p>
<p>gitlab : <a href="http://gitblit.***.cn">http://gitblit.***.cn</a><P>
<p>jumpserver : <a href="http://jump.***.cn">http://jump.***.cn</a><P>
<p>jira : <a href="http://jira.***.cn">http://jira.***.cn</a><P>
<p>wiki : <a href="http://wiki.***.cn">http://wiki.***.cn</a><P>
<p>showdoc : <a href="http://showdoc.***.cn">http://showdoc.***.cn</a><P>
<p>账号：%s</p>
<p>密码：%s@123!</p>
<p>您可以访问后面的链接修改默认密码：<a href="http://ldap.***.cn">重置密码链接</a></p>
<p></p>
<p><b> 系统自动发送，勿回复！</b></p>
"""
