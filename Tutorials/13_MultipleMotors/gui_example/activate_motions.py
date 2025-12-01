from pyorcasdk import Actuator, MotorMode

class ORCAKinematic:
    def __init__(self):
        self.motors = []
        self.active_motion_id = None

    def connect_motors(self, serial_ports):
        """
        Opens the number of serial ports provided.
        Prints a connection message re: whether the port has connected succesfully or failed to connect.
        If no parameters are supplied in config.toml file, this runs the motor's saved motions.

        Args:
            serial_ports (array): An array of serial ports, parsed based on integers.
        """
        for index, port in enumerate(serial_ports):
            if index >= len(self.motors):
                self.motors.append(Actuator(f"ORCA{index}"))
                error = self.motors[index].open_serial_port(port)

                if error:
                    print(f"Error: {error.what()} \n")
                else:
                    print(f"Motor {index + 1} connected successfully!")
            else:
                pass

    def configure_motions(self):
        """
        This function can be used to configure motions one and two.
        If this function is not used, the motor activates its saved motions.
        """
        for motor in self.motors:
            motor.set_kinematic_motion(0, 50000, 1000, 0, 1)
            motor.set_kinematic_motion(1, 10000, 1000, 0, 1)

    def trigger_motions(self, motion_id):
        """
        Triggers the active motion based on the most recent 'Trigger' button press or console update.

        Args:
            motion_id (int): The current active motion.
        """
        self.active_motion_id = int(motion_id)

        if self.active_motion_id:
            for motor in self.motors:
                motor.set_mode(MotorMode.KinematicMode)
                motor.trigger_kinematic_motion(self.active_motion_id)

    def sleep_motor(self):
        """
        Sleeps the motors if 'Stop' is pressed or entered in the console.
        """
        for motor in self.motors:
            motor.set_mode(MotorMode.SleepMode)

    @property
    def active_motion_id(self):
        """
        Retrieves the value of the 'active_motion_id'.

        Returns:
            int: The current value of the self._active_motion_id attribute.
        """
        return self._active_motion_id

    @active_motion_id.setter
    def active_motion_id(self, value):
        """
        Sets a new value for the 'motion_id' attribute.

        Args:
            value (int): The new value to be assigned to self._active_motion_id.
        """
        self._active_motion_id = value
