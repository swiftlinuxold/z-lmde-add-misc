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
else:
	dir_develop='/home/'+uname+'/develop'

# Everything up to this point is common to all Python scripts called by shared-*.sh
# =================================================================================

# THIS IS THE SCRIPT FOR ADDING LIGHTWEIGHT APPLICATIONS

print '====================================='
print 'BEGIN ADDING LIGHTWEIGHT APPLICATIONS'

os.system('apt-get install -y sylpheed') # Add Sylpheed email client
os.system('apt-get install -y xscreensaver') # Add XScreenSaver
os.system('apt-get install -y geany') # Add the Geany editor
os.system('apt-get install -y searchmonkey') # Add the SearchMonkey file search program

import shutil
# Install and configure Conky
os.system ('apt-get install -y conky')
src = dir_develop + '/ui-de/dotconkyrc/conkyrc-regular'
dest = '/home/' + uname + '/.conkyrc'
shutil.copyfile(src, dest)

print 'Install IceWM'
# Install IceWM
os.system('apt-get install -y icewm')
# os.system('apt-get install -y icewm icewm-gnome-support')

def elim_dir (dir_to_elim): 
	if (os.path.exists(dir_to_elim)):
		shutil.rmtree (dir_to_elim)

print 'Removing excess themes'
# Only default, icedesert, nice, nice2, win95, and yellowmotif remain.
# These themes are easy to read and easy on space.
# IceWM themes options are under Main menu -> Settings -> Themes
themes='/usr/share/icewm/themes/'
elim_dir (themes+'gtk2')
elim_dir (themes+'Infadel2')
elim_dir (themes+'metal2')
elim_dir (themes+'motif')
elim_dir (themes+'warp3')
elim_dir (themes+'warp4')

# Install ROX-Filer and ROXTerm
os.system ('apt-get install -y rox-filer roxterm')

# Remove background wallpapers for GNOME to save space
backgrounds='/usr/share/backgrounds/'
elim_dir (backgrounds+'linuxmint')
elim_dir (backgrounds+'linuxmint-debian')
elim_dir (backgrounds+'linuxmint-katya')
elim_dir (backgrounds+'linuxmint-katya-extra')

# Create directory for Swift Linux wallpaper
dir_wallpaper='/usr/share/backgrounds/swift'
if not (os.path.exists(dir_wallpaper)):
	os.mkdir(dir_wallpaper)

# Copy the wallpaper file to the Swift Linux wallpaper directory
src = dir_develop + '/ui-de/usr_share_backgrounds_swift/rox-regular.jpg'
dest = dir_wallpaper + '/swift.jpg'
shutil.copyfile(src, dest)

# Create the directory for the ROX desktop file
dir_pb1 = '/home/'+uname+'/.config/rox.sourceforge.net'
dir_pb2 = dir_pb1 + '/ROX-Filer'
dir_pb3 = '/home/'+uname+'/.icewm'
if not (os.path.exists(dir_pb1)):
	os.mkdir (dir_pb1)
if not (os.path.exists(dir_pb2)):
	os.mkdir (dir_pb2)

# Copy the ROX desktop file to dir_pb2
src=dir_develop+'/ui-de/ROX-Filer/pb_swift'
dest=dir_pb2+'/pb_swift'
shutil.copyfile(src, dest)

# Copy the ROX Options file to dir_pb2
src=dir_develop+'/ui-de/ROX-Filer/Options'
dest=dir_pb2+'/Options'
shutil.copyfile(src, dest)

# Activate ROX Pinboard
# os.system ('rox --pinboard=')
# os.system ('rox --pinboard=swift')

# print 'Adding/replacing IceWM files'

src = dir_develop + '/ui-de/etc_X11_icewm/theme'
dest = '/etc/X11/icewm/theme'
shutil.copyfile (src, dest)
dest = dir_pb3 + '/theme'
shutil.copyfile (src, dest)

src=dir_develop+'/ui-de/etc_X11_icewm/preferences'
dest='/etc/X11/icewm/preferences'
shutil.copyfile(src, dest)
dest = dir_pb3 + '/preferences'
shutil.copyfile (src, dest)

src=dir_develop+'/ui-de/etc_X11_icewm/startup'
dest='/etc/X11/icewm/startup'
os.system ('chmod a+rwx ' + dest)
os.system ('chown '+uname+':users '+dest)
shutil.copyfile(src, dest)
dest='/home/'+uname+'/.icewm/startup'
shutil.copyfile(src, dest)
dest = dir_pb3 + '/startup'
shutil.copyfile(src, dest)
os.system ('chmod a+rwx ' + dest)
os.system ('chown '+uname+':users '+dest)


# src=dir_develop+'/ui-de/etc_X11_icewm/keys'
# dest='/etc/X11/icewm/keys'
# shutil.copyfile(src, dest)


# src=dir_develop+'/ui-de/etc_X11_icewm/winoptions'
# dest='/etc/X11/icewm/winoptions'
# shutil.copyfile(src, dest)



# src=dir_develop+'/ui-icewm/usr_local_bin/auto-icewm-menu.sh'
# dest='/usr/local/bin/auto-icewm-menu.sh'
# shutil.copyfile(src, dest)

# src=dir_develop+'/ui-icewm/usr_local_bin/icewm-xdg-menu'
# dest='/usr/local/bin/icewm-xdg-menu'
# shutil.copyfile(src, dest)

# src=dir_develop+'/ui-icewm/home_user_doticewm/menu'
# dest='/home/'+uname+'/.icewm/menu'
# shutil.copyfile(src, dest)


# src=dir_develop+'/ui-icewm/home_user_doticewm/toolbar'
# dest='/home/'+uname+'/.icewm/toolbar'
# shutil.copyfile(src, dest)

print 'FINISHED ADDING LIGHTWEIGHT APPLICATIONS'
print '========================================'
