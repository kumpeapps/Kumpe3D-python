if [ ! -f /home/kiosk/Kumpe3D-python/patches/installed.1.2.3 ]; then
    {
        wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub > /home/kiosk/linux_signing_key.pub
        sudo install -D -o root -g root -m 644 /home/kiosk/linux_signing_key.pub /etc/apt/keyrings/linux_signing_key.pub 2>/dev/null
        echo 46
        sudo sh -c 'echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/linux_signing_key.pub] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list'
        sudo apt-get update 2>/dev/null
        echo 47
        sudo apt-get install google-chrome-stable -y 2>/dev/null
        echo 48
    } | whiptail --gauge "Updating Kumpe3D Kiosk" 6 50 45
    touch /home/kiosk/Kumpe3D-python/patches/installed.1.2.3
fi