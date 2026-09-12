---
title: "Keyboard"
author: "antondimitrov2785"
description: "Its a keyboard using the 1800 compact layout"
created_at: "2026-09-11"
---

# 2026-09-11: Making the case

**Total time spent: 1.0 hours**

I didnt make it complicated. tye top plate will just slide in befort any of the keys are placed and then they will secure the plate down ![image](https://cdn.hackclub.com/019edcaa-5fd0-77eb-a0db-7ddd4bee9a8d/image.png)

# 2026-09-11: Adding GND and 3D models

**Total time spent: 2.5 hours**

In this time I had to add like 150 vias all around the PCB because I had screwed up with one of the steps that were made to make the process easier. Other than that it is all good. ![image](https://cdn.hackclub.com/019edc84-5fd6-7e7e-b745-227b8fa04a16/image.png)
After that I had to find a way to add the 3D models. I had forgotten how t o do that but I managed to do it and now everything but the keycaps is there (I think there is no need of them on the switches and they will make the process a bt harder).![image](https://cdn.hackclub.com/019edc86-e486-78ed-bfe1-b976adff152d/Screenshot%202026-06-18%20235551.png)

# 2026-09-11: conected the LEDs to the 5v rails

**Total time spent: 1.5 hours**

It wasnt ahrd. My the only thing that I didnt account for was the many vias that I needed to place. I had specificly wanted to make it easy to wire then the GND, but it looks like it wouldnt happen
![image](https://cdn.hackclub.com/019eccff-63c0-71fa-8a4a-2ef0fdcbe24d/image.png)

# 2026-09-11: Adding stabilizers and 5v rail

**Total time spent: 2.5 hours**

I needed the 5v rail for all of the LEDs. That is why it is much ticker than the other lines. The stabilizers were straight forward. 
![image](https://cdn.hackclub.com/019ec723-b38d-7cd6-b4f6-d9a30dc87bd0/image.png)

# 2026-09-11: Connecting some resistors and lines

**Total time spent: 0.5 hours**

I had forgotten to add some of the resistors that are connected to the USB and chip. I moved the crystal which I will wire some other day. 
![image](https://cdn.hackclub.com/019eae15-5b01-7d6d-8d89-878376252d97/image.png)

# 2026-09-11: making the columns bus

**Total time spent: 1.5 hours**

I needed to connect every column to the chip. And I didnt want to make it too hard later on with the GND layers. 
![image](https://cdn.hackclub.com/019ea8cc-81b4-7771-a47b-1130fd0e8899/Screenshot%202026-05-28%20222322.png)

# 2026-09-11: Making the chip assembly

**Total time spent: 1.0 hours**

I needed to add the chip modules and all of the caps and everything that is related to it. Now I haave to connect every column and row.
![image](https://cdn.hackclub.com/019e9bf8-e8e9-71fa-9775-bc35f1661a8b/Screenshot%202026-05-22%20215843.png)

# 2026-09-11: Adding LED and caps

**Total time spent: 3.0 hours**

I needed to add every led and capacitor. FOr each other row I had to flip the LED and the cap so that it would be easier to wire it later. that alone will save me 2 hours in the future. ![image](https://cdn.hackclub.com/019e998a-10ae-7211-b697-bc088b8f9753/Screenshot%202026-05-22%20201857.png)

# 2026-09-11: Arranging the Switches

**Total time spent: 4.0 hours**

I added the footrpints and I needed to start to arrangе all of the switches and LEDs. 
![image](https://cdn.hackclub.com/019e8e8e-fb2e-73d3-ac2e-bbc4a9e535c3/image.png)
After the hours I spent arranging the switches and diodes I have it for now. I spent more time than I needed because I wanted all of them to be at the same place relative to the centre of the switch to make it easier to wire and soulder later.  
![image](https://cdn.hackclub.com/019e8e8f-8090-7792-9e3b-0b1a654412f7/Screenshot%202026-05-22%20185700.png)

# 2026-09-11: Assigning footprints

**Total time spent: 1.0 hours**

I wanted to handsoulder everything do I made the caps size 0805 to make it easier and the diodes are sot-123. The switches will be on hotswap module. 
![image](https://cdn.hackclub.com/019e885d-78aa-7e8f-a5a1-d614a549e5a2/image.png)

# 2026-09-11: Adding LEDs and caps

**Total time spent: 1.0 hours**

Almost each LED needs an capacitor to smooth out the current for each LED. This is required because there are 96 LED on one single 5v line. 
![image](https://cdn.hackclub.com/019e847d-479c-794e-936b-72834f63ce1c/image.png)

# 2026-09-11: Adding the switches

**Total time spent: 2.0 hours**

I decided to place each key into its own sheet so it would be easier to assign the footprints later. The last thing I need to add to the schematic is the LED with their caps and then Im going to start on the layout and PCB. 
![image](https://cdn.hackclub.com/019e7f89-9f55-7e6f-a019-b69ca2608d99/Screenshot%202026-05-31%20223056.png)

# 2026-09-11: The chip side is done

**Total time spent: 2.0 hours**

This part wasnt the easiest nor of the hardest. I just had to search what pin to connect where. And now I have to make the LEDs and the switches. 
![image](https://cdn.hackclub.com/019e7533-1bdd-7f83-b061-68f89a5208e5/Screenshot%202026-05-21%20211149.png)

# 2026-09-11: Getting schematic symbols

**Total time spent: 1.0 hours**

This is the symbols that will be for the chip and the things around it. The keys and diodes will follow up next. 
![image](https://cdn.hackclub.com/019e6fff-042f-742e-ba92-83a710ef9af0/Screenshot%202026-05-21%20211219.png)

# 2026-09-11: Chip

**Total time spent: 1.0 hours**

For this keyboard I have decided to not use a devboard. I will integrate the chip with all of the components it needs into the keyboard to make the keyboard a bit smaller and easier to work with. ![image](https://cdn.hackclub.com/019e4c5b-828a-791e-850e-ce487e8e3f5a/Screenshot%202026-05-21%20195727.png)

# 2026-09-11: Layout

**Total time spent: 1.5 hours**

I will use a 1800 compact layout. I have chosen this one because I dont need the keys that are cut short from the full sized keyboard and if I happen to need them they will be just on a lower layer of the symbols.  ![image](https://cdn.hackclub.com/019e4b7a-b3d6-7051-9f68-826844f4dc0f/Screenshot%202026-02-15%20222532.png)

