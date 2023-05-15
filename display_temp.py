from machine import ADC, Pin, I2C 
from ssd1306 import SSD1306_I2C
import time
adc = machine.ADC(4)
WIDTH =128 
HEIGHT= 64
i2c=I2C(0,scl=Pin(1),sda=Pin(0),freq=200000)
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c) 
while True:
    oled.fill(0)
    ADC_voltage = adc.read_u16() * (3.3 / (65535))
    temperature_celcius = 27 - (ADC_voltage - 0.706)/0.001721
    temp_fahrenheit=32+(1.8*temperature_celcius)
    oled.text("Temperature:",0,10)
    oled.text(str(int(temperature_celcius)), 95, 10)
    oled.text("C",110,10)
    oled.show()
    time.sleep_ms(500)