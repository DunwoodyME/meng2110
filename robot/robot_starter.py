#!/usr/bin/env python
"""
robot_starter.py
    Starter code for Lego robot vehicle
    Daniel Thomas
    Nov 21, 2017

Documentation for the BrickPi3 can be obtained by the following
command in your Pi terminal:
>>> pydoc brickpi3.BrickPi3

"""

import brickpi3 as bp
import time

# Set up BrickPi object and initialize sensors:
igor = bp.BrickPi3()
igor.set_sensor_type(igor.PORT_1, igor.SENSOR_TYPE.EV3_ULTRASONIC_CM)
igor.set_sensor_type(igor.PORT_3, igor.SENSOR_TYPE.EV3_GYRO_ABS_DPS)


try:
    # Set a target speed in degrees per second (DPS)
    igor.set_motor_dps(igor.PORT_A + igor.PORT_D, 60)
    time.sleep(1.0)

    # Move the motor to a given angular position
    igor.set_motor_dps(igor.PORT_D, 0)          # Stop motor D
    current_position = igor.get_motor_encoder(igor.PORT_A)
    igor.offset_motor_encoder(igor.PORT_A, current_position) # Reset encoder A
    igor.set_motor_limits(igor.PORT_A, 100, 60) # (port, power_limit, DPS_limit)
    igor.set_motor_position(igor.PORT_A, 180)   # Set target position in degrees
    while True:     # Wait while motor moves to given position
        current_position = igor.get_motor_encoder(igor.PORT_A)
        print('  Current motor A position: {0} deg'.format(current_position))
        if current_position >= 177: break
        time.sleep(0.02)
    igor.set_motor_dps(igor.PORT_A, 0)          # Stop motor A

    # Print voltages: Battery should be 7.2 - 10.0 V
    print('\n  Battery voltage: {0:6.3f} V'.format(igor.get_voltage_battery()))
    print("  9v voltage:     %6.3f V"   % igor.get_voltage_9v())
    print("  5v voltage:     %6.3f V"   % igor.get_voltage_5v())
    print("  3.3v voltage:   %6.3f V\n" % igor.get_voltage_3v3())

    # Print out the ultrasonic & gyro sensor outputs:
    while True:
        try:
            distance = igor.get_sensor(igor.PORT_1)
            print('\n  Ultrasonic sensor reading: {0:.2f} cm'.format(distance))
            gyro = igor.get_sensor(igor.PORT_3) # [deg, deg/sec]
            print('  Gyro sensor reading: {0} deg'.format(gyro[0]))
        except bp.SensorError as error:
            print(error)
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
finally:
    igor.reset_all()  # Unconfigure the sensors and disable the motors
