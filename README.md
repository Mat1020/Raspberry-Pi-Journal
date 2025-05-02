# Raspberry Pi Journal
A repository to keep all the important information of hardware/electronics that the Raspberry Pi can control. This is a repository made by myself from my notes for the Raspberry Pi. Since I've so many notes that I've kept to myself, I decided to make a GitHub repository to publish these notes. I also have included a couple of more words so you're able to understand.

This repository is compadable to every version of Raspberry Pi, but I'm not entirely sure. Since I only own a Raspberry Pi 4, I'm not sure if the tutorials would work the same to whatever Raspberry Pi you've. 

If you have any problems, please create an issue in the "Issues" section of this repository, I'll try to help you to whatever issue you face. In the future, I'd also attempt to make a video version based of this repository. But, not yet.

## Sections
These sections go (in my opinon) in a order from what **you should learn first.**

- [1. LEDs](Projects/LED/LED.md)
- [2. Buttons](Projects/Button/Button.md)
- [3. RGB LEDs](Projects/RGB%20LED/RGBLED.md)
- [4. Servos](Projects/Servo/Servo.md)

# Important Notes




# Controlling LED with Raspberry Pi GPIO
A repositorie to control any color or more than one LED with your Raspberry Pi. From this repositorie, it'll guide and teach you from everything you need to know about LEDs. From how to get started with LEDs with your Raspberry Pi in a begginer project, to how to do fancy circuits with LEDs with your Raspberry Pi, all in step-by-step.

This repositorie should be compadable to every version of Raspberry Pi.

Without any further do, let's dive in! :D

## Overview
➢ **What is an LED? What are LEDs used for?** <br>
The LED is short for Light Emitting Diode, and it's a semiconductor device that emits light when an electric current passes through it. LEDs are used for various purposes, including: lighting fixtures, displays, automotive lighting, and even medical equipment due to their energy efficiency, long lifespan, and versatility.

➢ **What does GPIO stand for?** <br>
Raspberry Pi GPIO pins stand for _General Purpose Input/Output_. They are used to connect with the outside world and physical objects, and they are located on the edge of the Raspberry Pi board.

➢ **Summary** <br>
We're going to use the Raspberry Pi GPIO pins to control the LED(s). We're going to use gpiozero module from Python to write the code, and we're going to need basic materials for the projects.

## Table of Contents
You can click on the link to go to the project you're interested in. The projects go from **easiest** to **hardest**.

- [Project #1: Make an LED Blink](#project-1-make-an-led-blink)

## Layouts
➢ **Raspberry Pi GPIO Pinout Diagram** <br>
Before connecting and setting anything yet, you need to understand what the pinout of your Raspberry Pi is. The Raspberry Pi GPIO pinout diagram shows you the **name of each pin** and  **information about the functions of each pin**.

You can find your Raspberry Pi GPIO pinout diagram by typing in your broswer search:

<pre>
________________ gpio pinout
</pre>

In the blank, type your Raspberry Pi version.

For example, this Raspberry Pi GPIO pinout diagram correspons to **Raspberry Pi 4** (I couldn't find the orginal image):
![Raspberry Pi 4 GPIO Pinout](images/raspberry_pi_4.png)

➢ **LED Layout** <br>
As you may have noticed or not, LEDs have two legs corresponding to either negative energy or positive energy. The **positive** leg is usually the one who is the **longest**, and the **negative** is the **shortest**. 

Below, there's an image showing what leg correspons to:
![LED Layout](images/led_layout.png)

# Project #1: Make an LED Blink
This project is making the LED blink (turns on and off) for 5 times with a 0.5-second sleep in between. This project is great for begginers who want to get stated into using their Raspberry Pi into awesome project ideas. 

Keep in mind that **you should play and mess with it**, meaning that **you should be changing stuff (after you are done with the project) to explore and discover more**. 

## Materials
**Components** <br>
- 1x LED
- 2x Female/Male Jumpers
- 1x 100 ohm Resistor

**Tools/Equipment** <br>
- Raspberry Pi
- Micro SD Card
- Breadboard
  
## Bulding Up the Circuit
***Note:*** You may want to do this [BEFORE Building Up the Circuit](#layouts).

➢ **Final Circuit** <br>
![Project #1 Final Circuit](images/project1/final_circuit.png)

➢ **Building** <br>
1. Connect one of the Female/Male Jumper to the GND pin.

2. Connect another Female/Male Jumper to the GPIO 17 pin.

3. Connect the GND jumper to the negative row of the breadboard (Right Side).

4. Connect the GPIO 17 jumper to the positive row of the breadboard (Right Side).

5. Grab your LED and connect it to the negative row and the 25 column (Right side).

6. Grab your resistor and connect it to the positive row and the 25 column (Right Side).

➢ **Explanation** <br>
The male/female jumpers (or wires) are connected to GND pin and GPIO 17 pin. The GND pin stands for _ground pin_, which basicly what it does it's to provide a **unstopable power scource**. In contrast, the GPIO 17 acts like a power source that can be controll (which is one of the many uses). The GND pin is connected to the negative row of the breadboard (providing negative energy) and the GPIO 17 is connected to the positive row of the breadboard (providing positive energy).

Then, we have the resistor. The resistor is crucial for this circuit because it limits the current flowing through the LED so the LED can't get damage over time. The type of resistor is 100 ohm, but the type of resistor depends on the resistance, power rating, and other factors of the circuit.

Finally, we have the LED. The LED is being powered by the 100 ohm resistor on the positive leg and by direcly the negative row of the breadboard on the negative leg.

## Writting the Code
For this project, we would be learning **3 commands** for the LED (even though we'd only using 2) to turn on/off the LED to make it blink.

We'd using [Thonny](THONNY.md) IDE for this project. Since this project is begginer, I strongly recommend using [Thonny](THONNY.md). Click on the link for more details and provided setps.

| Command | Description | Module/Library | Programming Language | 
|-----------|-----------|----------|----------|
| .on() | Turns the LED on | gpiozero | Python |
| .off() | Turns the LED off | gpiozero | Python |
| .toggle() | Switches the LED to its opposite state (on if it was off, and off if it was on) | gpiozero | Python |


You need to import the LED module:
<pre>
from gpiozero import LED
</pre>

Create a variable named "led" and attach the "LED(17)" value to it:
<pre>
led = LED(17)
</pre>

Now, you're ready! You can use one of the 3 commands we discused about with your Raspberry Pi. If needed, this is an example of turning on the LED:
<pre>
led.on()
</pre>

## Final Code
For the final code of this project, it's organized similarly for the rest of the projects. 

There would be folders on this repo that you'll have to copy to your Raspberry Pi, and you do that by making the folder to that name and then making the files and the content on those files.

➢ **Folders:** <br>
A. LED Flash
