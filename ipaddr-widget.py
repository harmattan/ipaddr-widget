# -*- coding: utf-8 -*-
#
# Harmattan IP Address "Widget" (http://thp.io/2011/ipaddr-widget/)
# -----------------------------------------------------------------
# Based on my calendar icon experiment (calenderr.sh), here is someting that
# could provide the community with a way of adding "widgets" to the app screen.
#
# How it works: When clicked, it will automatically update its application icon
# with the current IP(s) from /sbin/ifconfig and the launcher will reload it.
#
# Oh and by the way: The icon update can happen anytime. Next, I want someone
# to come up with an "overlay" icon for their apps to indicate new items (e.g.
# the mail application could have an overlay with the amount of new mails, ...)
#
# Copyright (c) 2011 Thomas Perl <thp.io/about>; License: GPLv3+
#

import Image, ImageDraw
import subprocess
import re
import os

ICON_TEMPLATE = '/usr/share/ipaddr-widget/template.png'
ICON_WIDGET = '/home/user/.config/widgets/ipaddr.png'

TARGET_FOLDER = os.path.dirname(ICON_WIDGET)
if not os.path.isdir(TARGET_FOLDER):
    os.makedirs(TARGET_FOLDER)

im = Image.open(ICON_TEMPLATE)
width, height = im.size

ifconfig = subprocess.Popen('/sbin/ifconfig', stdout=subprocess.PIPE)
stdout, stderr = ifconfig.communicate()

ips = re.findall('addr:([^ ]+)', stdout)
ips = filter(lambda ip: not ip.startswith('127.'), ips) or ['Offline']

draw = ImageDraw.Draw(im)
for idx, ip in enumerate(ips):
    sx, sy = draw.textsize(ip)
    draw.text((width/2 - sx/2, height/2 - (len(ips)*sy)/2 + idx*sy),
            ip, fill=(255, 255, 255))
del draw

im.save(ICON_WIDGET, 'PNG')

