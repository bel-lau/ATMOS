Program to take pictures and print pixel data using the Lepton FLIR camera.

This program is a modified version of the sample raspberrypi_capture program from the original LeptonModule repository. This program will be used on a Raspberry Pi with a Lepton camera hooked up to it, which will be sent up in the quadcopter payload of a rocket to take images of the ground every 10 seconds during the duration of the copter's descent.

Changes made:
* Added section for printing the array of pixel data for each picture
* Images are now created as .jpeg files, rather than .pgm files
* Added loop to take multiple pictures in one run
