# 5.11. Project: Conditional Launch

# 5.11.1. Spacecraft Data
engine_indicator_light = "green"
space_suits_on = False
shuttle_cabin_ready = True
crew_status = space_suits_on and shuttle_cabin_ready
computer_status_code = 400

# 5.11.2. Part A: PREDICT
print('The code will print: "Engines off"')
print('The two blocks of code produce different results b/c "and" and "or" are different')
print()

# 5.11.3. Part B: Cabin Safety Checks
spacecraft_speed = float(input("Enter the spacecraft's speed: "))
if crew_status == True:
    print('Crew Ready')
else:
    print('Crew Not Ready')

if computer_status_code == 200:
    print('Please standby. Computer is rebooting.')
elif computer_status_code == 400:
    print('Success! Computer online.')
else:
    print('ALERT: Computer offline!')

if spacecraft_speed > 17500:
    print('ALERT: Escape velocity reached!')
elif spacecraft_speed < 8000:
    print('ALERT: Cannot maintain orbit!')
else:
    print('Stable speed')

# 5.11.4. Part C: Fuel Safety Checks
fuel_level = 10001
engine_temperature = 2500

if fuel_level < 1000  or engine_temperature > 3500 or engine_indicator_light == 'red blinking':
    print('ENGINE FAILURE IMMINENT!')
elif fuel_level <= 5000  or engine_temperature > 2500:
    print('ALERT: Check fuel level and engine temperature.')
elif fuel_level > 20000 and engine_temperature <= 2500:
    print('Full tank. Engines good.')
elif fuel_level > 10000  and engine_temperature <= 2500:
    print('Fuel level above 50%.  Engines good.')
elif fuel_level > 5000  and engine_temperature <= 2500:
    print('Fuel level above 25%. Engines good.')
else:
    print('Fuel and engine status pending...')

# 5.11.4.1. Test Your Fuel Status Code

print()
# 5.11.5. A Final Bit of Fun!
command_override = False
'''
if command_override == False:
    print('Command override: OFF')
    if fuel_level > 20000 and engine_temperature <= 2500:
        print('Cleared to launch!')
    else:
        print('Launch scrubbed!')
else:
    print('Command override is ON')
    print('Cleared to launch!')
'''

if fuel_level > 20000 and engine_indicator_light != 'red blinking' or command_override == True:
    print('Cleared to launch!')
else:
    print('Launch scrubbed!')