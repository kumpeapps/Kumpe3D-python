    #!/bin/bash
    token=$(whiptail --inputbox "Enter Infisical Token" 8 39 Blue --title "Kumpe3D-Python Setup" 3>&1 1>&2 2>&3)
    exitstatus=$?
    if [ $exitstatus = 0 ]; then
        gawk -i inplace '!/SERVICE_TOKEN/' /home/kiosk/Kumpe3D-python/.env
        echo "SERVICE_TOKEN=" $token > /home/kiosk/Kumpe3D-python/.env
    fi
    environment=$(whiptail --inputbox "Should this be Production(prod) or Development(dev)" 8 39 Blue --title "Kumpe3D-Python Setup" 3>&1 1>&2 2>&3)
    exitstatus=$?
    if [ $exitstatus = 0 ]; then
        gawk -i inplace '!/APP_ENV/' /home/kiosk/Kumpe3D-python/.env
        echo "APP_ENV=" $environment >> /home/kiosk/Kumpe3D-python/.env
    fi
    userid=$(whiptail --inputbox "Default User ID (cancel for none)" 8 39 Blue --title "Kumpe3D-Python Setup" 3>&1 1>&2 2>&3)
    exitstatus=$?
    if [ $exitstatus = 0 ]; then
        gawk -i inplace '!/USERID/' /home/kiosk/Kumpe3D-python/.env
        echo "USERID=" $userid >> /home/kiosk/Kumpe3D-python/.env
    fi
    print_room=$(whiptail --inputbox "Is this kiosk in a print room?" 8 39 Blue --title "Kumpe3D-Python Setup" 3>&1 1>&2 2>&3)
    exitstatus=$?
    if [ $exitstatus = 0 ]; then
        gawk -i inplace '!/print_room/' /home/kiosk/Kumpe3D-python/.env
        echo "print_room=" $print_room >> /home/kiosk/Kumpe3D-python/.env
    fi
    orders_desk=$(whiptail --inputbox "Is this kiosk an orders desk?" 8 39 Blue --title "Kumpe3D-Python Setup" 3>&1 1>&2 2>&3)
    exitstatus=$?
    if [ $exitstatus = 0 ]; then
        gawk -i inplace '!/orders_desk/' /home/kiosk/Kumpe3D-python/.env
        echo "orders_desk=" $orders_desk >> /home/kiosk/Kumpe3D-python/.env
    fi
    printer_enabled=$(whiptail --inputbox "Can this kiosk print to network?" 8 39 Blue --title "Kumpe3D-Python Setup" 3>&1 1>&2 2>&3)
    exitstatus=$?
    if [ $exitstatus = 0 ]; then
        gawk -i inplace '!/printer_enabled/' /home/kiosk/Kumpe3D-python/.env
        echo "printer_enabled=" $printer_enabled >> /home/kiosk/Kumpe3D-python/.env
    fi
    mifare_enabled=$(whiptail --inputbox "Does this kiosk have a Schlage credential reader?" 8 39 Blue --title "Kumpe3D-Python Setup" 3>&1 1>&2 2>&3)
    exitstatus=$?
    if [ $exitstatus = 0 ]; then
        gawk -i inplace '!/mifare_enabled/' /home/kiosk/Kumpe3D-python/.env
        echo "mifare_enabled=" $mifare_enabled >> /home/kiosk/Kumpe3D-python/.env
    fi