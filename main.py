#! /usr/bin/env python

# Check for root user login
import os, sys
if not os.geteuid()==0:
    sys.exit("\nOnly root can run this script\n")

# Get your username (not root)
import pwd
uname=pwd.getpwuid(1000)[0]

# The remastering process uses chroot mode.
# Check to see if this script is operating in chroot mode.
# /home/mint directory only exists in chroot mode
is_chroot = os.path.exists('/home/mint')
dir_develop=''
if (is_chroot):
	dir_develop='/usr/local/bin/develop'
	dir_user = '/home/mint'
else:
	dir_develop='/home/' + uname + '/develop'
	dir_user = '/home/' + uname

# Everything up to this point is common to all Python scripts called by shared-*.sh
# =================================================================================


# THIS IS THE SCRIPT FOR ADDING LIGHTWEIGHT APPLICATIONS

def add_pkg (packages):
    os.system ('echo INSTALLING ' + packages)
    os.system ('apt-get install -qq ' + packages)

print '=============================='
print 'BEGIN ADDING MISC APPLICATIONS'
print 'NOTE: The screen output is suppressed due to excessive volume.'

add_pkg ('sylpheed')
add_pkg ('geany')
add_pkg ('searchmonkey')
add_pkg ('pcmanfm')
add_pkg ('roxterm')
add_pkg ('mtpaint')
add_pkg ('epdfview')
add_pkg ('parole')

add_pkg ('smartmontools gsmartcontrol')

# NOTE: smart-notifier is installed only for chroot mode, because it triggers a reboot on a live system
if (is_chroot):
    add_pkg ('smart-notifier')
    
add_pkg ('mpg123')
    

print 'FINISHED ADDING MISC APPLICATIONS'
print '================================='
