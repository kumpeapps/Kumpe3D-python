if [ ! -f /home/kiosk/Kumpe3D-python/patches/installed.1.2.1 ]; then
    {
        sudo apt-get update
        echo 42
        sudo apt-get install gawk -y
        echo 43
        gawk -i inplace '!/printer_enabled/' /home/kiosk/Kumpe3D-python/.env
    } | whiptail --gauge "Updating Kumpe3D Kiosk" 6 50 41

    if whiptail --title "Kumpe3D Kiosk Setup" --yesno "Can this kiosk print to network printers?" 8 78; then
        echo "printer_enabled=1" >> /home/kiosk/Kumpe3D-python/.env
    else
        echo "printer_enabled=0" >> /home/kiosk/Kumpe3D-python/.env
    fi
    touch /home/kiosk/Kumpe3D-python/patches/installed.1.2.1
fi