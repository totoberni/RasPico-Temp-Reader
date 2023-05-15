from machine import ADC, Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# initialize ADC with the pin number where it is connected
adc = machine.ADC(PIN_NUMBER)

# set up the OLED display using I2C communication
WIDTH = 128
HEIGHT = 64
i2c = I2C(0, scl=Pin(SCL_PIN_NUMBER), sda=Pin(SDA_PIN_NUMBER), freq=I2C_FREQUENCY)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

while True:
    # clear the OLED display
    oled.fill(0)

    # read the ADC voltage and convert it to Celsius
    ADC_voltage = adc.read_u16() * (VOLTAGE_CONVERSION_FACTOR)
    temperature_celcius = CALCULATE_TEMPERATURE_CELSIUS(ADC_voltage)

    # convert Celsius to Fahrenheit
    temp_fahrenheit = CALCULATE_TEMPERATURE_FAHRENHEIT(temperature_celcius)

    # print the temperature in Celsius on OLED display
    oled.text("Temperature:", 0, 10)
    oled.text(str(int(temperature_celcius)), 95, 10)
    oled.text("C", 110, 10)

    # update the OLED display with the temperature
    oled.show()

    # wait for some time before taking another reading
    time.sleep_ms(DELAY_TIME_IN_MILLISECONDS)
