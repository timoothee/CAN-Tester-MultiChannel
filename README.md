# CAN-Tester GUI application

Python program that present a gui app used for easy interaction in a linux environment.
The main objective, in addition to being a useful interactive application, is to achieve 4 main functionalities.

- Be able to configure can settings.
- Toggle between canup and candown.
- Write messages or import a list of messages to send.
- CAN BUS area



**Apart from these functionalities, we managed to add extra ones that helps the user.**
- Developer settings (used only by the developer)
- Edit message button
- Error area (in case we have syntax messages errors or wrong settings)

# Hardware parts
- Raspberry Pi 4
- Charger
- uSDcard
- HDMI Cable
- CAN-FD extension board [link](https://www.seeedstudio.com/2-Channel-CAN-BUS-FD-Shield-for-Raspberry-Pi-p-4072.html)

# Set UP
Step 1: Download Raspberry PI Imager [link](https://www.raspberrypi.com/software/)

Step 2: In the Linux terminal write:
```
sudo apt-get update
```
```
sudo apt-get upgrade
```
Step 3: Remote access:
```
sudo raspi-config 
```
![Screenshot 2023-03-27 at 04 41 55](https://user-images.githubusercontent.com/115079881/227820929-e64c5a04-561b-4853-9da8-b7078e417be3.png)

![Screenshot 2023-03-27 at 04 42 47](https://user-images.githubusercontent.com/115079881/227821017-244e9e4a-1712-4588-87bf-128046b04ec5.png)

Step 4: Reboot:
```
sudo reboot
```
# Install needed components:
- Git
```
sudo apt-get install git
```
# Install CAN-HAT
Step 1: Clone this repo:
```
git clone https://github.com/Seeed-Studio/seeed-linux-dtoverlays
cd seeed-linux-dtoverlays
```
Step 2: Open config.txt file: In the console type this comand to open the config file
```
sudo nano /boot/config.txt
```
Step 3: Enable the HAT:
There are 3 types of this HAT

- with controller MCP2517FD, no RTC available
- with controller MCP2518FD, no RTC available
- with controller MCP2518FD with RTC available

The last one is easily distinguishable because it has a slot for a battery in order to keep the RTC clock running, if your board has RTC you need to add the following line at the end of the config.txt file:
```
dtoverlay=seeed-can-fd-hat-v2
```
If your board does not have the RTC module you need to add the following line at the bottom of the config.text file:
```
dtoverlay=seeed-can-fd-hat-v1
```
Step 4: Save your config file You can save the file with any of the shortucts available, the most common is to press Ctrl + X to attemp to close the file, the console will prompt you to save before closing the file, press Y and then enter.

Step 5: Reboot:
```
sudo reboot
```
Then install the can library
```
sudo apt install can-utils
```
