# kid's toy: Jukebox controlled by rfid cards

![reader](photos/125KHz-Black-USB-Proximity-Sensor-Smart-rfid-id-Card-Reader-EM4100-EM4200-EM4305-T5577-or-compatible.jpg)
![applicationsuggestion](photos/applicationsuggestion.jpg)
![reader_in_furniture](photos/reader_in_furniture.jpg)
![cards](photos/5YOA-10pcs-5YOA-1-8mm-EM4100-Tk4100-125khz-Access-Control-Card-Keyfob-RFID-Tag-Tags-Sticker.jpg)

## Materials used:
- raspberry pi 2 (similar should work)
- SD card with raspbian
- USB RFID reader acting as an USB keyboard, (aliexpress "125KHz Black USB Proximity Sensor Smart rfid id Card Reader EM4100 EM4200 EM4305 T5577 or compatible")
- a set of compatible rfid cards (aliexpress "10pcs 5YOA 1.8mm EM4100 125khz Keyfob RFID Tag)
- double sided tape to mount the reader behind the glass front of our TV furniture
- piece of laminated paper with icon of music notes on it (see the artwork/ folder)

## Operation
When the RFID reader outputs a card code, the player checks if a filename starting with the code (and a dash) exists.  If so it starts playing it.

there are two special cards:
- "key" unlock/lock the player
- "stop" stop playing the current song
To identify these special cards to the player, create files by those names and rename them to prefix them with the text generated by the rfid reader for those cards.

## Installation

The default login agetty process on the first video console is replaced with the player (note you can still login with keyboard if you switch to another video console eg. with ctrl-alt-f2):

1. place `play.py`, `play.service` in `/home/pi` (or a different location if you update play.service)
2. run the following commands:

       apt-get install sox libsox-fmt-mp3 alsamixer
       sudo install -m 644 play.service /etc/systemd/system/play.service
       sudo systemctl daemon-reload
       sudo systemctl mask getty@tty1.service
       sudo systemctl enable play.service
       sudo systemctl start play.service

3. use `raspi-config` to enable playback to jack
4. use `alsamixer` to set an acceptable volume
5. make sure to shut down correctly to have alsa save the volume levels, use `sudo reboot` to check if playback works as expected.
