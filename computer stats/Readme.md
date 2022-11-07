# Simple Computer Statistics

## About project
I wrote this code circa June 2022 and it was my first contact with streaming datasets in PowerBI. At the time I made this srcipt I got GPU info using the GPUtil library, but in November when I came back to that code this library stopped working. Probably it's something with the drivers to my Nvidia card. 
At this moment I had to make some workaroud to get the GPU temperature etc. I tried other libraries, but any of them worked for me even though "nvidia-smi" commad fully worked in CMD. Finally, I made workaround where I launch this command from the script and format the result to get the data I need.

Gathered data are send using PowerBI API and then they are visualised in few simple charts.

![obraz](https://user-images.githubusercontent.com/56642926/200317162-5b1fa1fa-5f6b-46c4-b4c9-926d9eed0577.png)
