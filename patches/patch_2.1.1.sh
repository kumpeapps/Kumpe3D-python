if [ ! -f /home/kiosk/Kumpe3D-python/patches/installed.2.1.1 ]; then
    if [ ! -f /home/kiosk/terminalmode ]; then
        touch /home/kiosk/restoreguimode
        sh /home/kiosk/Kumpe3D-python/bash_scripts/disableGUI.sh
    fi
    sudo apt-get install libmpv-dev mpv -y
    sudo cp /home/kiosk/Kumpe3D-python/libmpv.so.1 /usr/local/lib/
    sudo ln -s /usr/local/lib/libmpv.so.1 /usr/lib/libmpv.so.1
    touch /home/kiosk/Kumpe3D-python/patches/installed.2.1.1
fi