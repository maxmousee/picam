# PiCam
How to build a point-and-shoot camera using a Raspberry Pi

## Requirements

Some knowledge of how computers and cameras work and patience

## Parts

1 - Raspberry Pi 3B+ or 4

1 - Powerbank

1 - USB cable appropriate for your Raspberry Pi - Raspberry Pi 4 uses USB-C, older models use micro USB

1 - HQ Camera module for Raspberry Pi

1 - HyperPixel 4.0 - Hi-Res Touch Display for Raspberry Pi

1 - C-Mount lens

1 - MicroSD card

1 - Computer with an SD card reader to install Raspberry OS to the micro SD card

1 - Case to mount it

1 - Display with HDMI port and a HDMI cable

# How to build it

I suggest testing everything without the case and without the display because it's easier to fix any issues

## Installing Raspberry Pi OS

First, put the SD card in your computer and install Raspberry OS into it

There's a good and simple tutorial on how to do it on Raspberry Pi's website https://www.raspberrypi.org/documentation/installation/installing-images/


    Download the latest version of Raspberry Pi Imager and install it.
        If you want to use Raspberry Pi Imager on the Raspberry Pi itself, you can install it from a terminal using sudo apt install rpi-imager.
    Connect an SD card reader with the SD card inside.
    Open Raspberry Pi Imager and choose the required OS from the list presented.
    Choose the SD card you wish to write your image to.
    Review your selections and click 'WRITE' to begin writing data to the SD card.

Note: if using the Raspberry Pi Imager on Windows 10 with Controlled Folder Access enabled, you will need to explicitly allow the Raspberry Pi Imager permission to write the SD card. If this is not done, Raspberry Pi Imager will fail with a "failed to write" error.
Using other tools

## Basic assembly

Put the SD card with Raspberry Pi OS into the raspberry Pi slot

Plug the HDMI cable to a monitor, plug a mouse and a keyboard into the Raspberry Pi
and plug power into the raspberry Pi, either by using the powerbank or a USB charger (your smartphone probably has one)

After Raspberry Pi OS is running, connect it to the Wi-Fi (or ethernet) and update it

If you don't know how to install or configure it, there are a lot of easy tutorials on YouTube, I recommend this one https://www.youtube.com/watch?v=y45hsd2AOpw

## Camera assembly and software

Turn off your Raspberry Pi and disconnect it from the power supply, plug in your camera module to the appropriate port in your Raspberry Pi and then screw on the lens into the camera module

###Attention: the camera module flat cable is FRAGILE, be very careful and gentle when connecting or disconnecting it

//TODO how to install camera software, increase GPU memory and create the shortcut
//TODO how to install touchscreen module
//TODO how to assembly