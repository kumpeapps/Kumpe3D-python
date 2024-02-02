sudo systemctl set-default graphical.target
rm /home/kiosk/terminalmode
touch /home/kiosk/guimode
rm /home/kiosk/restoreguimode
sudo reboot