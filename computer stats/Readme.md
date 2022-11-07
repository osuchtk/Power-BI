# Simple Computer Statistics

## About project
I wrote this code circa June and it was my first contact with streaming datasets in PowerBI. At the time I made this srcipt I got GPU info using the GPUtil library, but in November when I came back to that code this library stopped working. Probalby it's something with the drivers to my Nvidia card. 
At this moment I had to make some workaroud to get the GPU temperature etc. I tried other libraries, but any of them worked for me. Finally when I found out that "nvidia-smi" commad
fully worked in terminal I launch this command from the script and format the result to get the data I need.
