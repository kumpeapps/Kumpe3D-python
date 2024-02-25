if [ ! -f /home/kiosk/Kumpe3D-python/patches/installed.2.1 ]; then
    if [ ! -f /home/kiosk/terminalmode ]; then
        touch /home/kiosk/restoreguimode
        sh /home/kiosk/Kumpe3D-python/bash_scripts/disableGUI.sh
    fi
    {
        sudo apt-get install wget build-essential libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev -y
        echo 53
        tar xzf Python-3.10.8.tgz
        cd Python-3.10.8 
        ./configure --enable-optimizations
        echo 55
        make altinstall
        echo 65
        pip3 install -r /home/kiosk/Kumpe3D-python/requirements.txt
    } | whiptail --gauge "Updating Kumpe3D Kiosk" 6 50 48
    touch /home/kiosk/Kumpe3D-python/patches/installed.2.1
fi