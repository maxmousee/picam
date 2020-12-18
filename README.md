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

## How to install the camera software

In order to take photos, you will need to install the camera software.

To download the Application, run "git clone https://github.com/maxmousee/picam.git" on your Terminal.

You can create a shortcut to the Application on Raspberry Pi OS.

To do that, click on the Raspberry Pi OS menu, then Preferences and Main Menu Editor

Then click "New Item"

Create a name, you can use "Camera" and for the command use "python3 path where snap-on-btn-press.py is"...

For example, "python3 /home/pi/picam/snap-on-btn-press.py" is probably the default location.

In case your camera application is crashing due to not enough memory, increase the GPU memory to 256Mb using this guide:

https://www.raspberrypi.org/documentation/configuration/config-txt/memory.md

This should not be needed for the Raspberry PI 4, but for older models it is.

You can also change it in your Raspberry Pi OS settings if you are not comfortable with the Terminal.

## How to install the touchscreen module

If everything goes well, and the camera application runs, you can now assemble the touchscreen module and install the driver.

To do that, shut down your Raspberry Pi, disconnect the power supply and install the HyperPixel 4.0 drivers.

There's a very good guide on how to do that here https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-hyperpixel-4

## Time to build everything

After every part is working, you can now put everything into the case and here it will probably be very different from what I did.

You can do what I did and use a plastic camera, remove the insides and zip tie the Raspberry Pi, lens and touch module to it.

Alternatively you can buy a specific Raspberry Pi camera case or 3D print your own case.

After you fit everything into the case, it's ready to use. Plug a USB cable into the Pi and into a powerbank and start taking pictures.

## Where are the photos I've taken?

Your photos will be saved to your Pictures folder as JPGs... /home/pi/Pictures

From there, you can upload them to Google Photos, OneDrive using the web browse :) 