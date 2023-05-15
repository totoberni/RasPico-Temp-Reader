# RasPico-Temp-Reader
Code to setup a temperature reader on a Raspberry Pi Pico device

# Below are the details for this project

## Difficulty: Easy

## Description:
Your task is to use the Pico and its display to make a temperature sensor. The Rasperry Pi already has a temperature sensor on board so it's a matter of configuring its use and displaying the current temperature on the OLED.

### Task 1:
Write a micropython script that detects the temperature from the onboard sensor. The sensor reads a voltage impedance between connectors to determine the temperature of the circuit. You can find more about this phenomenon here: https://electrocredible.com/raspberry-pi-pico-temperature-sensor-tutorial/. The equation is straightforward and implementing it is quite easy.

### Task 2: 
Display the temperature as it changes on the OLED screen. This too is not very difficoult and it requires just understanding how to communicate with the display.