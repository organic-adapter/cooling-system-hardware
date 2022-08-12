# Installation and Setup
You need to follow the Hardware and Python/CircuitPython libraries steps described in the article 
https://www.freva.com/dht11-temperature-and-humidity-sensor-on-raspberry-pi/

# Execution
This code does not use the "Write the Code" script. Instead you can run

```python CoolingSystem.py```

# Configuration
You can modify the cooling-config.json properties to adjust the thresholds that trigger the 
cooling adjustments.

Right now it's checking to see if the sensor telemetry is between specific ranges. This may
change to a Wet Bulb Thermometer calculation.
