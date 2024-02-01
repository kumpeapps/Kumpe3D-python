if [ ! -f /home/kiosk/Kumpe3D-python/patches/installed.2.0 ]; then
    if whiptail --title "Kumpe3D Kiosk Setup" --yesno "Kumpe3D Kiosk has been updated to 2.0 which adds login feature. Would you like to remove default userid?" 8 78; then
        gawk -i inplace '!/USERID/' /home/kiosk/Kumpe3D-python/.env
        echo "USERID=none" >> /home/kiosk/Kumpe3D-python/.env
    fi
    touch /home/kiosk/Kumpe3D-python/patches/installed.2.0
fi