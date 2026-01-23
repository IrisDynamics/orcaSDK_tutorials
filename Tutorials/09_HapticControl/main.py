from pyorcasdk import Actuator, MotorMode, OscillatorType, HapticEffect

motor = Actuator( "MyMotorName" )

serial_port = int(input("Please input the serial port of your connected motor. "))

motor.open_serial_port(serial_port)

motor.clear_errors() # ORCA motors raise an error when communication stops during haptics mode

motor.enable_stream()

motor.set_mode(MotorMode.HapticMode)

motor.update_haptic_stream_effects(HapticEffect.Osc0 | HapticEffect.Spring0)

motor.set_spring_effect( #Update spring parameters
    0,      #Spring ID (0, 1, or 2)
    200,    #Spring strength
    40000   #Center position
)

motor.set_osc_effect(
    0,      #Oscillator ID (0 or 1)
    20,     #Oscillator max force (newtons)
    10,     #Frequency (decihertz)
    0,      #Duty cycle (not used in sine wave)
    OscillatorType.Sine
)

while True:
    motor.run()

    print("Current Sensed Force: " + str(motor.get_stream_data().force), end="        \r")