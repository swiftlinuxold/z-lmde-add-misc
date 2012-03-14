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

print '=============================='
print 'BEGIN ADDING MISC APPLICATIONS'

os.system('apt-get install -y sylpheed') # Add Sylpheed email client
os.system('apt-get install -y geany') # Add the Geany editor
os.system('apt-get install -y searchmonkey') # Add the SearchMonkey file search program
os.system('apt-get install -y pcmanfm') # Add the PCManFM file manager
os.system ('apt-get install -y roxterm') # Add ROXTerm
os.system('apt-get install -y xscreensaver') # Add XScreenSaver
os.system('apt-get install -y mtpaint') # Add MTPaint
os.system('apt-get install -y epdfview') # Add lightweight PDF Viewer

# Install Ceni
os.system('apt-get install -y libcurses-perl libcurses-ui-perl') # Dependencies of ceni
os.system('apt-get install -y libexpect-perl libio-pty-perl') # Dependencies of ceni
os.system('apt-get install -y libio-stty-perl libterm-readkey-perl') # Dependencies of ceni
os.system('wget http://www.mirrorservice.org/sites/sidux.com/sidux/debian/pool/main/c/ceni/ceni_2.23_all.deb')
os.system('dpkg -i ceni_2.23_all.deb')
os.system('rm ceni_2.23_all.deb')
os.system('apt-get install -f')

os.system('apt-get install -y smartmontools gsmartcontrol')

# NOTE: smart-notifier is installed only for chroot mode, because it triggers a reboot on a live system
if (is_chroot):
    os.system('apt-get install -y smart-notifier')
    
os.system('apt-get install -y mpg123') # Plays MP3s from command line, needed for special editions
    

print 'FINISHED ADDING MISC APPLICATIONS'
print '================================='
