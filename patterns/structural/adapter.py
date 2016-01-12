class FahrenheitSensor(object):
    def __init__(self):
        self.fahrenheit_temp = 100

    def get_fahrenheit_temp(self):
        return self.fahrenheit_temp


class AdaptedSensor_1(object):
    def __init__(self, fahrenheit_sensor):
        self.fahrenheit_sensor = fahrenheit_sensor

    def get_temp(self):
        t = float(self.fahrenheit_sensor.get_fahrenheit_temp())
        return (t - 32.0)  * 5.0 / 9.0


class AdaptedSensor_2(FahrenheitSensor):
    def __init__(self):
        super(AdaptedSensor_2, self).__init__()

    def get_temp(self):
        t = self.get_fahrenheit_temp()
        return (t - 32.0)  * 5.0 / 9.0


if __name__ == '__main__':
    fahrenheit_sensor = FahrenheitSensor()
    print fahrenheit_sensor.get_fahrenheit_temp()
    sensor_1 = AdaptedSensor_1(fahrenheit_sensor)
    print sensor_1.get_temp()

    sensor_2 = AdaptedSensor_2()
    print sensor_2.get_temp()
