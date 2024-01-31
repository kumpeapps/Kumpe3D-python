#!/bin/bash
{
    if [ ! -f .cur_version ]; then
    echo "0" > .cur_version
    fi
    echo 5
    cd /home/kiosk/Kumpe3D-python && git pull
    echo 10
    version=$(cat .version)
    cur_version=$(cat .cur_version)
    echo 20
    cd /home/kiosk/Kumpe3D-python && git update
    echo 

    if [ $cur_version < 1.2]; then
        sudo apt-get update
        touch runupdate
        echo 30
        sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio -y
        echo 40
    fi

    echo 98
    echo $version > .cur_version

} | whiptail --gauge "Updating Kumpe3D Kiosk" 6 50 0