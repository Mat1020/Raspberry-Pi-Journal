# What is an RGB LED?
RGB LED stands for Red, Green, and Blue. It's a type of light-emitting diode (LED) that can produce over 16 million colors by combining these three primary science colors.

## Tutorial 1: Control the RGB LED (in Python)

1 ) Materials:

- 4x Female/Male Jumpers
- 6x Resistors 100 ohms
- 1x RGB LED
- Breadboard
- Raspberry Pi
- Micro SD Card

2 ) Building the Circuit:

**Step 1:** <br>
Connect the RGB LED red leg on 25 column of the breadboard (Right Side)

**Step 2:** <br>
Connect the RGB LED ground leg on 28 column of the breadboard (Right Side)

**Step 3:** <br>
Connect the RGB LED blue leg on 30 column of the breadboard (Right Side)

**Step 4:** <br>
Connect the RGB LED green leg on 33 cloumn of the breadboard (Right Side)

***Note:*** <br>
Each color needs a different balance of vol. <br>
Red needs 100 ohn <br>
Green needs 200 ohn <br>
Blue needs 300 ohn <br>

**Step 5:** <br>
Connect one resistor between 25 column on the (Right Side) and the (Left Side) 25 column of the breadboard

**Step 6:** <br>
Connect one resistor between 33 column on the (Right Side) and the (Left Side) 40 column of the breadboard

**Step 7:** <br>
Connect one resistor between 40 cloumn on the (Left Side) and 50 column on the (Left Side) of the breadboard

**Step 8:** <br>
Connect one resistor between 30 column on (Right Side) and 30 column on the (Left Side) of the breadboard

**Step 9:** <br>
Connect one resistor between 30 column on the (Left Side) and 22 column on the (Left Side) of the breadboard

**Step 10:** <br>
Connect one resistor between 22 column on the (Left Side) and 11 column on the (Left Side) of the breadboard

***Note:*** <br>
Raspberry Pi GPIO Pins
	
**Step 11:** <br>
Connect one male/female jumper to the GND pin

**Step 12:** <br>
Connect the GND jumper to 28 column of the breadboard (Right Side)

**Step 13:** <br>
Connect one male/female jumper to the GPIO 17 pin

**Step 14:** <br>
Connect the GPIP 17 jumper to the 11 column of the breadboard (Left Side)

**Step 15:** <br>
Connect one male/female jumper to the GPIO 27 pin

**Step 16:** <br>
Connect the GPIO 27 to the 50 column of the breadboard (Left Side)

**Step 17:** <br>
Connect the last male/female jumper to the GPIO 22 pin

**Step 18:** <br>
Connect the GPIO 22 jumper to 25 column of the breadboard (Left Side)

3 ) Set up the Code:

You need to import the LED module:
<pre>
from gpiozero import LED
</pre>

Create a variable named "red" and attach "LED(22)" to it:
<pre>
red = LED(22)
</pre>

Create a variable named "green" and attach "LED(17)" to it:
<pre>
green = LED(17)
</pre>

Create a variable named "blue" and attach "LED(27)" to it:
<pre>
blue = LED(27)
</pre>

To turn on/off an specified color, we can type the name of the variable with either ".on()" method or ".off()" method
<pre>
blue.on()  # Example: I typed the name of the variable with one of the gpiozero methods
</pre>

4 ) My Programs Examples:

A. control_rgb.py
