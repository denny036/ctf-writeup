**Title**: hideme  
**Tags**: pico CTF 2023 - Forensics - steganography  
**Author**: GEOFFREY NJOGU

**Description**: "Every file gets a flag.
The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye here."

In this challenge, we provided an image file named 'flag.png'. Based on the category and description provided in this challenge, we can extract the metadata of the file. To further investigate the file, we used Binwalk, an open-source tool used for analyzing and extracting information from files. By using Binwalk to perform an extraction of embedded files from 'flag.png', we obtained a directory called 'secret' that contains a new file named 'flag.png'. Opening the file revealed the flag: **picoCTF{Hiddinng_An_imag3_within_@n_ima9e_d55982e8}.**
