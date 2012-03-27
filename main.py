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

#os.system('apt-get install -y sylpheed') # Add Sylpheed email client
add_pkg ('sylpheed')
#os.system('apt-get install -y geany') # Add the Geany editor
add_pkg ('geany')
#os.system('apt-get install -y searchmonkey') # Add the SearchMonkey file search program
add_pkg ('searchmonkey')
#os.system('apt-get install -y pcmanfm') # Add the PCManFM file manager
add_pkg ('pcmanfm')
#os.system ('apt-get install -y roxterm') # Add ROXTerm
add_pkg ('roxterm')
#os.system('apt-get install -y mtpaint') # Add MTPaint
add_pkg ('mtpaint')
#os.system('apt-get install -y epdfview') # Add lightweight PDF Viewer
add_pkg ('epdfview')

#os.system('apt-get install -y smartmontools gsmartcontrol')
add_pkg ('smartmontools gsmartcontrol')

# NOTE: smart-notifier is installed only for chroot mode, because it triggers a reboot on a live system
if (is_chroot):
    #os.system('apt-get install -y smart-notifier')
    add_pkg ('smart-notifier')
    
#os.system('apt-get install -y mpg123') # Plays MP3s from command line, needed for special editions
add_pkg ('mpg123')
    

print 'FINISHED ADDING MISC APPLICATIONS'
print '================================='
