#!/bin/bash
{
    echo 1
    sudo apt-get install wget -y 2>/dev/null
    echo 2
    sudo apt-get install ssh -y 2>/dev/null
    echo 3
    sudo apt-get install git -y 2>/dev/null
    echo 4
    sudo apt-get install pip -y 2>/dev/null
    echo 5
    sudo apt-get install -y python3-dev libasound2-dev 2>/dev/null
    echo 7
    sudo apt-get install python3-tk -y 2>/dev/null
    echo 8
    sudo apt-get install ratpoison -y 2>/dev/null
    echo 9
    sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio -y 2>/dev/null
    echo 25
    wget https://debian.kumpedns.us/setupRepo.sh 2>/dev/null
    echo 26
    sudo apt-get purge aisleriot cheese evolution five-or-more four-in-a-row gnome-2048 gnome-calendar gnome-chess gnome-clocks gnome-color-manager gnome-contacts gnome-disk-utility gnome-documents gnome-klotski gnome-logs gnome-mahjongg gnome-maps gnome-mines gnome-music gnome-nibbles gnome-robots gnome-sound-recorder gnome-shell-extension-prefs gnome-sudoku gnome-taquin gnome-tetravex gnome-todo gnome-tweaks gnome-weather hitori iagno im-config libreoffice-calc libreoffice-draw libreoffice-impress libreoffice-writer lightsoff malcontent nautilus quadrapassel rhythmbox seahorse shotwell simple-scan software-properties-gtk swell-foop synaptic tali transmission-gtk -y 2>/dev/null
    echo 35
    sudo apt-get purge baobab eog evince file-roller firefox-esr gedit gnome-calculator gnome-characters gnome-font-viewer gnome-screenshot gnome-software gnome-system-monitor libreoffice-common totem yelp -y 2>/dev/null
    echo 45
    sudo apt-get purge aisleriot baobab cheese eog evince evolution file-roller firefox-esr five-or-more four-in-a-row gedit gnome-2048 gnome-calculator gnome-calendar gnome-characters gnome-chess gnome-clocks gnome-color-manager gnome-contacts gnome-disk-utility gnome-documents gnome-font-viewer gnome-klotski gnome-logs gnome-mahjongg gnome-maps gnome-mines gnome-music gnome-nibbles gnome-robots gnome-screenshot gnome-software gnome-sound-recorder gnome-shell-extension-prefs gnome-sudoku gnome-system-monitor gnome-taquin gnome-tetravex gnome-todo gnome-tweaks gnome-weather hitori iagno im-config libreoffice-calc libreoffice-common libreoffice-draw libreoffice-impress libreoffice-writer lightsoff malcontent nautilus quadrapassel rhythmbox seahorse shotwell simple-scan software-properties-gtk swell-foop synaptic tali totem transmission-gtk yelp -y 2>/dev/null
    echo 55
    sh setupRepo.sh 2>/dev/null
    echo 60
    sudo apt-get install kumpe-home-sshdsetup -y 2>/dev/null
    echo 62
    sudo apt-get install sed -y 2>/dev/null
    echo 63
    adduser --disabled-password --gecos "" kiosk 2>/dev/null
    echo 65
    echo "#!/bin/sh" > /home/kiosk/.xinitrc
    echo 66
    echo "cd ~/Kumpe3D-python" >> /home/kiosk/.xinitrc
    echo 67
    echo "exec ratpoison& flet run" >> /home/kiosk/.xinitrc
    echo "sh /home/kiosk/Kumpe3d-python/debian_update.sh" >> /home/kiosk/.profile
    echo "exec startx" >> /home/kiosk/.profile
    echo 70
    passwd -d kiosk 2>/dev/null
    echo 71
    echo "kiosk     ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/kiosk
    cd /home/kiosk 2>/dev/null
    echo 73
    runuser -u kiosk -- git clone https://github.com/kumpeapps/Kumpe3D-python.git 2>/dev/null
    echo 74
    token=$(whiptail --inputbox "Enter Infisical Token" 8 39 Blue --title "Kumpe3D Kiosk Initial Setup" 3>&1 1>&2 2>&3)
    exitstatus=$?
    if [ $exitstatus = 0 ]; then
        echo "SERVICE_TOKEN=" $token > /home/kiosk/Kumpe3D-python/.env
    else
        echo "SERVICE_TOKEN=" > /home/kiosk/Kumpe3D-python/.env
    fi
    environment=$(whiptail --inputbox "Should this be Production(prod) or Development(dev)" 8 39 Blue --title "Kumpe3D Kiosk Initial Setup" 3>&1 1>&2 2>&3)
    exitstatus=$?
    if [ $exitstatus = 0 ]; then
        echo "APP_ENV=" $environment >> /home/kiosk/Kumpe3D-python/.env
    else
        echo "APP_ENV=" >> /home/kiosk/Kumpe3D-python/.env
    fi
    userid=$(whiptail --inputbox "Default User ID (cancel for none)" 8 39 Blue --title "Kumpe3D Kiosk Initial Setup" 3>&1 1>&2 2>&3)
    exitstatus=$?
    if [ $exitstatus = 0 ]; then
        echo "USERID=" $userid >> /home/kiosk/Kumpe3D-python/.env
    else
        echo "USERID=none" >> /home/kiosk/Kumpe3D-python/.env
    fi
    print_room=$(whiptail --inputbox "Is this kiosk in a print room?" 8 39 Blue --title "Kumpe3D Kiosk Initial Setup" 3>&1 1>&2 2>&3)
    exitstatus=$?
    if [ $exitstatus = 0 ]; then
        echo "print_room=" $print_room >> /home/kiosk/Kumpe3D-python/.env
    else
        echo "print_room=0" >> /home/kiosk/Kumpe3D-python/.env
    fi
    orders_desk=$(whiptail --inputbox "Is this kiosk an orders desk?" 8 39 Blue --title "Kumpe3D Kiosk Initial Setup" 3>&1 1>&2 2>&3)
    exitstatus=$?
    if [ $exitstatus = 0 ]; then
        echo "orders_desk=" $orders_desk >> /home/kiosk/Kumpe3D-python/.env
    else
        echo "orders_desk=0" >> /home/kiosk/Kumpe3D-python/.env
    fi
    printer_enabled=$(whiptail --inputbox "Can this kiosk print to network?" 8 39 Blue --title "Kumpe3D Kiosk Initial Setup" 3>&1 1>&2 2>&3)
    exitstatus=$?
    if [ $exitstatus = 0 ]; then
        echo "printer_enabled=" $printer_enabled >> /home/kiosk/Kumpe3D-python/.env
    else
        echo "printer_enabled=0" >> /home/kiosk/Kumpe3D-python/.env
    fi
    mifare_enabled=$(whiptail --inputbox "Does this kiosk have a Schlage credential reader?" 8 39 Blue --title "Kumpe3D Kiosk Initial Setup" 3>&1 1>&2 2>&3)
    exitstatus=$?
    if [ $exitstatus = 0 ]; then
        echo "mifare_enabled=" $mifare_enabled >> /home/kiosk/Kumpe3D-python/.env
    else
        echo "mifare_enabled=0" >> /home/kiosk/Kumpe3D-python/.env
    fi
    echo 90
    sudo chown kiosk:kiosk /home/kiosk/.xinitrc
    sudo chown kiosk:kiosk /home/kiosk/.profile
    sudo chown kiosk:kiosk /home/kiosk/Kumpe3D-python/.env
    
    echo "(Exit status was $exitstatus)"
    sudo chown kiosk:kiosk /home/kiosk/.xinitrc 2>/dev/null
    echo 95
    runuser -u justinkumpe -- echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDc3HhBIEDUqeiqvN8J4kP+1Px9J1cNin2wWRzIUmo4IG+cdFnHoYPepcisfG5LOtrxAQnRZ20U8Pb4SNz9pyN84UXXWxgyMMITwkOEvGMl+HfGvPLrQPz9quWZpqusN1rhxxYQ6YZOaU2rrN09zf3hoVdzi0vKla4mDnUuLTWGLDmqBhzRbTd4UUv1stSe4f3t9IZCW6vRq2hZS1qXJ+TUwHrLS2EVRzo9ReUfj1fErCk1o0ZbN7+PUOnPS7RXQMD8TMjE0R4ZdHDHLIa6Rl073xSPqpmA1RPXUJo9lhWtMMggBX1yfVnWrrDJ09f9wmmI/jq1kO16oo6ZoQSEk+ogvzEWciFBKf/YfoWCvLyxCPODpT1xIGo5kgugcrQn7ftmc5K1qbNt0qO32JAJbr0pp+npl+GG64ebnim3IBMwk0Pz7oIfQpRtD+D7KoFE5JWNrWEF93RdE7+UeFMekh5UD+UEUAalkIjOQA+ioSHJcE3Vjtr19dqljvCfYja4PP8=" > /home/justinkumpe/.ssh/authorized_keys
    echo 100
    runuser -u kiosk -- touch /home/kiosk/terminalmode
    runuser -u kiosk -- touch /home/kiosk/restoreguimode
} | whiptail --gauge "Kumpe3D Kiosk Initial Setup" 6 50 0
runuser -u kiosk -- sh /home/kiosk/Kumpe3D-python/patches/patch_updates.sh