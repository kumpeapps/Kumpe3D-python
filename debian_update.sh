#!/bin/bash
vercomp(){
   local a b IFS=. -; set -f 2>/dev/null
#   printf a %08d $1; printf b %08d $3
   test $a "$2" $b 2>/dev/null
}

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
    echo 20
    echo 

    if vercomp $cur_version < "1.2"; then
        echo "updated to 1.2" >> update.log
        sudo apt-get update 2>/dev/null
        echo 21
        sudo apt-get install libgstreamer1.0-dev -y 2>/dev/null
        echo 22
        sudo apt-get install libgstreamer-plugins-base1.0-dev -y 2>/dev/null
        echo 23
        sudo apt-get install libgstreamer-plugins-bad1.0-dev -y 2>/dev/null
        echo 24
        sudo apt-get install gstreamer1.0-plugins-base -y 2>/dev/null
        echo 25
        sudo apt-get install gstreamer1.0-plugins-good -y 2>/dev/null
        echo 26
        sudo apt-get install gstreamer1.0-plugins-bad -y 2>/dev/null
        echo 27
        sudo apt-get install gstreamer1.0-plugins-ugly -y 2>/dev/null
        echo 28
        sudo apt-get install gstreamer1.0-libav -y 2>/dev/null
        echo 29
        sudo apt-get install gstreamer1.0-tools -y 2>/dev/null
        echo 30
        sudo apt-get install gstreamer1.0-x -y 2>/dev/null
        echo 31
        sudo apt-get install gstreamer1.0-alsa -y 2>/dev/null
        echo 31
        sudo apt-get install gstreamer1.0-gl -y 2>/dev/null
        echo 33
        sudo apt-get install gstreamer1.0-gtk3 -y 2>/dev/null
        echo 34
        sudo apt-get install gstreamer1.0-qt5 -y 2>/dev/null
        echo 35
        sudo apt-get install gstreamer1.0-pulseaudio -y 2>/dev/null
        echo 40
    fi

    if vercomp $cur_version < "1.2.1"; then
        echo "updated to 1.2" >> update.log
        if whiptail --title "Kumpe3D Kiosk Setup" --yesno "Can this kiosk print to network printers?" 8 78; then
            echo "printer_enabled=1" >> /home/kiosk/Kumpe3D-python/.env
        else
            echo "printer_enabled=0" >> /home/kiosk/Kumpe3D-python/.env
        fi
    fi

    echo 98
    echo $version > .cur_version

} | whiptail --gauge "Updating Kumpe3D Kiosk" 6 50 0