# Description
Created by Nikolay Shergin for Amirkhanov Marat.
Flask application to control ws2812b LED strip using NeoPixel library with GET API request running on Raspberry Pi.

# Install and run as root 
Prepare your raspberry
The audio output must be deactivated. For this we edit the file
```
echo 'blacklist snd_bcm2835' >> /etc/modprobe.d/snd-blacklist.conf
```
Edit the file /boot/config.txt and comment dtparam=audio=on line there
```
#dtparam=audio=on
```
Reboot the Pi
```
reboot
```  
# Install components
```
apt-get update
apt-get install -y git python-dev python3-pip
pip3 install Flask rpi_ws281x adafruit-circuitpython-neopixel
git clone https://github.com/nikolayShergin/LED.git
cd LED
```  
# Run the App
```
python3 ver1.0.cells.py
```  
  
# Customization
Change PIN, num_pixels as required.
Add new colors if needed.
Configure CELL LED ranges.
```
pixel_pin = board.D18
num_pixels = 60
```
#COLORS
See here for more colors codes:
https://www.w3schools.com/colors/colors_picker.asp

```
colors = {
  "BLACK":(0, 0, 0),
  "RED":(255, 0, 0), 
  "YELLOW": (255, 150, 0),
  "GREEN":(0, 255, 0),
  "CYAN":(0, 255, 255),
  "BLUE":(0, 0, 255),
  "PURPLE":(180, 0, 255)
}
```
#CELLS
```
cells = {
  "C1":range(0, 3),
  "C2":range(3, 20),
  "C3":range(20, 27),
  "C4":range(27, 40),
  "C5":range(40, 50),
  "C6":range(50, 60)
}
```
