if [ ! -f /home/kiosk/Kumpe3D-python/patches/installed.2.1 ]; then
    if [ ! -f /home/kiosk/terminalmode ]; then
        touch /home/kiosk/restoreguimode
        sh /home/kiosk/Kumpe3D-python/bash_scripts/disableGUI.sh
    fi
    pip install flet_easy -y
    touch /home/kiosk/Kumpe3D-python/patches/installed.2.1
fi