if [ ! -f /home/kiosk/Kumpe3D-python/patches/installed.1.2.2 ]; then
    {
        sudo apt update
        echo 44
        sudo apt-get install wkhtmltopdf -y
        echo 45
        pip3 uninstall pyppeteer -y
    } | whiptail --gauge "Updating Kumpe3D Kiosk" 6 50 43
    touch /home/kiosk/Kumpe3D-python/patches/installed.1.2.2
fi