#!/bin/bash
{
    if [ ! -f /home/kiosk/Kumpe3D-python/patches/installed.1.2 ]; then
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
        touch /home/kiosk/Kumpe3D-python/patches/installed.1.2
    fi
} | whiptail --gauge "Updating Kumpe3D Kiosk" 6 50 20