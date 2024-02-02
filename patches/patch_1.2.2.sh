if [ ! -f /home/kiosk/Kumpe3D-python/patches/rollback.1.2.2 ]; then
    {
        sudo apt-get update
        echo 44
        sudo apt-get remove wkhtmltopdf -y 2>/dev/null
        echo 45
        pip3 uninstall pyppeteer -y 2>/dev/null
        pip3 uninstall pdfkit -y 2>/dev/null
    } | whiptail --gauge "Updating Kumpe3D Kiosk" 6 50 43
    touch /home/kiosk/Kumpe3D-python/patches/rollback.1.2.2
fi