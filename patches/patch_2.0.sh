if [ ! -f /home/kiosk/Kumpe3D-python/patches/installed.2.0 ]; then
    if [ ! -f /home/kiosk/terminalmode ]; then
        touch /home/kiosk/restoreguimode
        sh /home/kiosk/Kumpe3D-python/bash_scripts/disableGUI.sh
    fi
    pip install flet -y
    gawk -i inplace '!/ratpoison/' /home/kiosk/.xinitrc
    gawk -i inplace '!/xsetroot/' /home/kiosk/.xinitrc
    echo "xsetroot -solid white -cursor_name left_ptr" >> /home/kiosk/.xinitrc
    echo "exec ratpoison& flet run" >> /home/kiosk/.xinitrc
    touch /home/kiosk/Kumpe3D-python/patches/installed.2.0
fi