# Anton's kayboard
--- 
### What is this project
* This is a keyboar that uses thr 1800 compact layout (an almost 100% keyboard without most of the keys between the enter and the numpad). This keyboard uses an rp2040 chip for its 30 gpio pins that make the making of the keyboard PCB layout easier. Bellow every hotswapable key there is a LED that is wired to every other one and can be controlled with code. 
<img width="1098" height="566" alt="3d model PCB" src="https://github.com/user-attachments/assets/cd5bc56f-819a-4187-94a7-e075a72ed67e" />

--- 
### Why I made this project
* I made this keyboard because I wanted to try a bigger more complx PCB that I would be able to use everyday.
* Also I wanted to update my keyboard with one that I made.

--- 
### Images
* The schematic for the PCB
<img width="1856" height="943" alt="schematic" src="https://github.com/user-attachments/assets/b90a6952-ea01-4df5-8bfb-0faf8e1246b1" />
* The schematic for the hierarchal sheets and what is in it
<img width="2559" height="1391" alt="Shematic herarcial sheets" src="https://github.com/user-attachments/assets/fde748ed-015c-4b37-9099-da376ab33808" />
* The layout and the PCB
<img width="1648" height="606" alt="PCB" src="https://github.com/user-attachments/assets/d22e1e9a-aa21-4ba9-868e-9b4c45742f12" />
* The 3D model of the case and assembly of the keyboard
* 
<img width="1985" height="557" alt="Assembly" src="https://github.com/user-attachments/assets/3afadce5-a0af-43e0-92be-0e6b58b5aa6a" />

--- 
### BOM
| Component | Purpose | Qty | Total Cost (USD) | Distributor |
|-----------|---------|:---:|:----------------:|-------------|
| Gateron Stabilizer | Prevents larger switches from wobbling | 1 | $9.45 | Gateron |
| Decoupling Capacitors (100nF) | Reduce electrical noise before the LEDs | 2 | $3.20 | AliExpress |
| LEDs (SK6812 Mini-E) | RGB underglow beneath the switches | 1 | $3.56 | AliExpress |
| Keycaps | Keycaps | 1 | $15.78 | AliExpress |
| Rotary Encoder (EC11E) | Rotary knob for volume / scroll | 1 | $2.78 | AliExpress |
| Diodes (1N4148W) | Prevent signal backflow in the matrix | 2 | $3.60 | AliExpress |
| Resistors (4.7 kΩ and 350 Ω) | Current limiting for LEDs and I²C pull-ups | 1 | $4.10 | AliExpress |
| Foam | Sound dampening layer under the PCB | 1 | $7.77 | AliExpress |
| Coiled Cable | Connecting cable for the keyboard | 1 | $5.55 | AliExpress |
| PCB | Main circuit board | 1 | $59.00 | JLCPCB |
| Microcontroller (YD-RP2040) | Runs the keyboard firmware (KMK / CircuitPython) | 1 | $2.94 | AliExpress |
| Gateron Switches | The switches you type on | 1 | $29.00 | Gateron |
| Hotswap Sockets | Allow switches to be swapped without soldering | 1 | $6.68 | Gateron |
| **Total** | | | **$153.51** | |

--- 
### Assembly
* First you need to soulder the smaller components (the diodes and capacitors) just for your sanity because later it will get harder.
* The secpnd smallest thingyou need to soulder many of are the LEDs.
* After that you are free to soulder the hotswap sockets.
* The chip can be souldered at any time.
* The keys and kaycaps must be placed after the PCB is put into the case and secured with the top case.

--- 
### Known problems
* The code is almost entirely made by claude because I dont have the chip with me and I cant write the code.

--- 
### Credits
* Designed and built by *(Anton/ Anton-2785-bit)
* Inspired by open‑source mechanical keyboard and hackpad communities (https://forge.hackclub.com/).


