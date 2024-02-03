if [ ! -f /home/kiosk/Kumpe3D-python/patches/installed.init ]; then
    if [ ! -f /home/kiosk/terminalmode ]; then
        touch /home/kiosk/restoreguimode
        sh /home/kiosk/Kumpe3D-python/bash_scripts/disableGUI.sh
    fi
    sudo apt-get remove *gnome* gdm* -y
    sudo apt-get install lxde-core -y
    touch /home/kiosk/Kumpe3D-python/patches/installed.init
fi