from machine import ADC
import time

# initialize ADC with the pin number where it is connected
adc = machine.ADC(PIN_NUMBER)

while True:
    # read the ADC voltage and convert it to Celsius
    ADC_voltage = adc.read_u16() * (VOLTAGE_CONVERSION_FACTOR)
    temperature_celcius = CALCULATE_TEMPERATURE_CELSIUS(ADC_voltage)

    # convert Celsius to Fahrenheit
    temp_fahrenheit = CALCULATE_TEMPERATURE_FAHRENHEIT(temperature_celcius)

    # print the temperature in both Celsius and Fahrenheit units
    print("Temperature: {}°C {}°F".format(temperature_celcius, temp_fahrenheit))

    # wait for some time before taking another reading
    time.sleep_ms(DELAY_TIME_IN_MILLISECONDS)
