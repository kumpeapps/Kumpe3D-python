#!/bin/bash
#TODO: check for .env file and prompt setup if not exist
if [ ! -f .cur_version ]; then
    echo "0" > .cur_version
fi
{
    echo 0
    echo 5
    cd /home/kiosk/Kumpe3D-python && git pull 2>/dev/null
    echo 10
    version=$(cat .version)
    cur_version=$(cat .cur_version)
    echo $version >> update.log
    echo $cur_version >> update.log
} | whiptail --gauge "Updating Kumpe3D Kiosk" 6 50 1

echo $version > .cur_version

sh /home/kiosk/Kumpe3D-python/patches/patch_updates.sh
{} | whiptail --gauge "Updating Kumpe3D Kiosk" 6 50 100
clear