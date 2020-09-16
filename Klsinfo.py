class KlsInfo:
    def __init__(self, raw3a, raw3b):
        self.__init__()
        self.new_raw3a(raw3a)
        self.new_raw3b(raw3b)

    def __init__(self):
        self.throttle = 0
        self.brake_pedal = 0
        self.switch_brake = 0
        self.switch_forward = 0
        self.switch_foot = 0
        self.switch_reverse = 0
        self.switch_hall_A = 0
        self.switch_hall_B = 0
        self.switch_hall_C = 0
        self.voltage_battery = 0
        self.temperature_motor = 0
        self.temperature_controller = 0
        self.direction_setting = 0
        self.direction_actual = 0
        self.motor_speed = 0
        self.phase_current = 0
        self._separator = ","

    def new_raw3a(self, raw):
        if len(raw) == 19:
            if raw[0] == 0x3A and \
               raw[18] == self.get_checksum(raw):
                self.throttle = raw[2]
                self.brake_pedal = raw[3]
                self.switch_brake = raw[4]
                self.switch_forward = raw[5]
                self.switch_foot = raw[6]
                self.switch_reverse = raw[7]
                self.switch_hall_A = raw[8]
                self.switch_hall_B = raw[9]
                self.switch_hall_C = raw[10]
                self.voltage_battery = raw[11]
                self.temperature_motor = raw[12]
                self.temperature_controller = raw[13]
                self.direction_setting = raw[14]
                self.direction_actual = raw[15]
                return True
        return False

    def new_raw3b(self, raw):
        if len(raw) == 19:
            if raw[0] == 0x3B and \
               raw[18] == self.get_checksum(raw):
                self.motor_speed = int(raw[5] + (raw[4] * 255))
                self.phase_current = int(raw[7] + (raw[6] * 255))
                return True
        return False

    def get_line(self):
        return str(self.throttle) + self._separator +  \
            str(self.brake_pedal) + self._separator +  \
            str(self.switch_brake) + self._separator +  \
            str(self.switch_forward) + self._separator +  \
            str(self.switch_foot) + self._separator +  \
            str(self.switch_reverse) + self._separator +  \
            str(self.switch_hall_A) + self._separator +  \
            str(self.switch_hall_B) + self._separator +  \
            str(self.switch_hall_C) + self._separator +  \
            str(self.voltage_battery) + self._separator +  \
            str(self.temperature_motor) + self._separator +  \
            str(self.temperature_controller) + self._separator +  \
            str(self.direction_setting) + self._separator +  \
            str(self.direction_actual) + self._separator + \
            str(self.motor_speed) + self._separator + \
            str(self.phase_current)

    def get_header(self):
        return "throttle" + self._separator +  \
            "throttle" + self._separator +  \
            "brake_pedal" + self._separator +  \
            "switch_brake" + self._separator +  \
            "switch_forward" + self._separator +  \
            "switch_foot" + self._separator +  \
            "switch_reverse" + self._separator +  \
            "switch_hall_A" + self._separator +  \
            "switch_hall_B" + self._separator +  \
            "switch_hall_C" + self._separator +  \
            "voltage_battery" + self._separator +  \
            "temperature_motor" + self._separator +  \
            "temperature_controller" + self._separator +  \
            "direction_setting" + self._separator +  \
            "direction_actual" + self._separator + \
            "motor_speed" + self._separator + \
            "phase_current"

    @staticmethod
    def get_checksum(raw):
        checksum = 0
        for i in range(len(raw) - 1):
            checksum += raw[i]
            if checksum > 0xFF:
                checksum -= 0xFF
        return checksum
