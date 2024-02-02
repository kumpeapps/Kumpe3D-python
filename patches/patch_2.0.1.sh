if [ ! -f /home/kiosk/Kumpe3D-python/patches/installed.2.0.1 ]; then
    {
        sudo apt-get update 2>/dev/null
        echo 49
        sudo apt-get install feh -y 2>/dev/null
        echo 50
        echo "exec feh --bg-scale /home/kiosk/Kumpe3D-python/logo.png" > /home/kiosk/.ratpoisonrc
        echo "bind l exec killall flet" >> /home/kiosk/.ratpoisonrc
        echo "definekey top C-l exec killall flet" >> /home/kiosk/.ratpoisonrc
        echo "bind C-g exec /home/kiosk/Kumpe3D-python/bash_scripts/enableGUI.sh" >> /home/kiosk/.ratpoisonrc
        echo "bind C-s exec /home/kiosk/Kumpe3D-python/bash_scripts/runsetup.sh" >> /home/kiosk/.ratpoisonrc
    } | whiptail --gauge "Updating Kumpe3D Kiosk" 6 50 48
    touch /home/kiosk/Kumpe3D-python/patches/installed.2.0.1
fi