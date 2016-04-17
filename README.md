# AquariumController

Requires ROOT6 : http://root.cern.ch 

To install dependencies : 
sudo apt-get install git dpkg-dev make g++ gcc binutils libx11-dev libxpm-dev libxft-dev libxext-dev python-dev gfortran

Get ROOT : 
cd ~/
git clone http://root.cern.ch/git/root.git
cd root
git checkout -b v6-06-02 v6-06-02

then, on Raspian wheezy : 

./configure --with-x11-libdir=/usr/lib/arm-linux-gnueabihf/ --with-xpm-libdir=/usr/lib/arm-linux-gnueabihf/ --with-xft-libdir=/usr/lib/arm-linux-gnueabihf/ --with-xext-libdir=/usr/lib/arm-linux-gnueabihf/ --enable-http --enable-python

to use root, 

source /home/pi/root/bin/thisroot.sh

Requires a working local mySQL database with a table with the fields filled by deamon.py

In this case, AQUARIUMdb is the database and tempdat is the table I created, containing : Date,Time,Comments,Temperature,pH,Relay1,Relay2


Aquarium Controller based on raspberry pi 3 B+ with : 
- DS18B20 : https://www.adafruit.com/product/381
- EZO pH Circuit : http://www.atlas-scientific.com/product_pages/circuits/ezo_ph.html 
- EZO Single Circuit USB Carrier board : http://www.atlas-scientific.com/product_pages/components/single_usb_carrier.html

In the future : 
  - SaintSmart 2 Channel relay for Light control and CO2 Solenoid control  : http://www.sainsmart.com/arduino-pro-mini.html
  
  
  Folder structure : 
  
  - ConditionDeamon
    ---> Read condition from pH sensor and temperature sensor and reccord thing in a local mySQL database 
    - pypH.py : Function to read pH
    - pyTemperature.py : Function to read Temperature 
    - deamon.py : Function to execute by cron job every time a reading need to be done and written to db
    - deamon.sh : bash script to run the deamon
  - plotter 
    ---> Instanciate web server and refresh plot by reading from mySQL database , should be started once at boot 
    - plotter.py : function that read the db and update the ROOT Tgraph objects 
    - plotterdeamon.py : instanciate the server and run the update of plots every 60s
    - launchplotter.sh : launch deamon maintaining the webserver
    
    
    

 
