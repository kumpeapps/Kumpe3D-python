#!/bin/bash

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

#20-40
bash /home/kiosk/Kumpe3D-python/patches/patch_1.2.sh

#41-43
bash /home/kiosk/Kumpe3D-python/patches/patch_1.2.1.sh

echo $version > .cur_version