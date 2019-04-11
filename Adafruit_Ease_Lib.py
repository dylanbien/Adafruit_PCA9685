#made by mangochildren
import Adafruit_PCA9685


HIGH = 4096
LOW = 0

class Adafruit_Ease_Lib():

    SERVO_LOW_TIME = 123
    SERVO_MID_TIME = 336
    SERVO_MAX_TIME = 560

    '''
    offests - if the servo limits are known to be different from the standards, provide the 
    new servo limits in this array. Defaults to noe
    '''
    def __init__(self,offsets = None):
        self.adafruit = Adafruit_PCA9685.PCA9685()
        self.num_pins = 16
        if not (offsets  == None):
            self.set_servo_limits(offsets[0],offsets[1],offsets[2])
        print('Adafruit initialized')


    def change_frequency(self, freq):
        self.adafruit.set_pwm_freq(freq)

    '''
    left -  period required for the servo to be at the minimum position/ 0 degrees
    center - period required to move to the center position/ 90 degrees
    right - period required to move to the maximum position/ 180 degrees
    '''
    def set_servo_limits(self, left, center, right):
        Adafruit_Ease_Lib.SERVO_LOW_TIME = left
        Adafruit_Ease_Lib.SERVO_MID_TIME = center
        Adafruit_Ease_Lib.SERVO_MAX_TIME = right
        print(left)
        print(center)
        print(right)

    def convert_freq_to_period(self, freq):
        return 1/freq

    def convert_period_to_freq(self, period):
        return 1/period

    '''
    FOR ALL THE FOLLOWING FUNCTIONS:
    
    *If pin is an array, the function will loop through the array of pins and perform the given task on all of them
    *If pin is a string that says 'all', the function will loop through all the pins and perform the given task on them
    *If pin is an int, the function will perform the given task on that specific pin.
    '''
    def set_high(self, pin):
        if pin == 'all':
            self.adafruit.set_all_pwm(HIGH, 0)
        elif isinstance(pin, list):
            for i in range(len(pin)):
                self.adafruit.set_pwm(i, HIGH, 0)
        else:
            self.adafruit.set_pwm(pin, HIGH, 0)

    def set_low(self, pin):
        if pin == 'all':
            self.adafruit.set_all_pwm(LOW, 0)
        elif isinstance(pin, list):
            for i in range(len(pin)):
                self.adafruit.set_pwm(i, LOW, 0)
        else:
            self.adafruit.set_pwm(pin, LOW, 0)

    '''
    percentage - On time percentage in the duty cycle. Use the change_percentage_servo() 
    function for servo movement
    '''
    def change_percentage(self, pin, percent):
        if percent == 100:
            self.set_high(pin)
            return
        elif percent == 0:
            self.set_low(pin)
            return
        percentage = int(4095 - (percent/100)*4095)
        if pin == 'all':
            self.adafruit.set_all_pwm(percentage, LOW)

        elif isinstance(pin, list):
            for i in range(len(pin)):
                self.adafruit.set_pwm(i, percentage, LOW)

        else:
            self.adafruit.set_pwm(pin, int(percentage), LOW)

    '''
    percent - percent of a 180 degree rotation the servo is meant to turn to
    '''
    def change_percentage_servo(self, pin, percent):
        self.adafruit.set_pwm_freq(50)
        if percent == 100:

            if pin == 'all':
                self.adafruit.set_all_pwm(0, Adafruit_Ease_Lib.SERVO_MAX_TIME)
            elif isinstance(pin, list):
                for i in pin:
                    self.adafruit.set_pwm(i,0, Adafruit_Ease_Lib.SERVO_MAX_TIME)
            else:
                self.adafruit.set_pwm(pin, 0, Adafruit_Ease_Lib.SERVO_MAX_TIME)
            print("moving to right")

        elif percent == 0:

            if pin == 'all':
                self.adafruit.set_all_pwm(0, Adafruit_Ease_Lib.SERVO_LOW_TIME)
            elif isinstance(pin, list):
                for i in pin:
                    self.adafruit.set_pwm(i, 0, Adafruit_Ease_Lib.SERVO_LOW_TIME)
            else:
                self.adafruit.set_pwm(pin, 0, Adafruit_Ease_Lib.SERVO_LOW_TIME)

            print("moving to center")

        elif percent == 50:

            if pin == 'all':
                self.adafruit.set_all_pwm(0, Adafruit_Ease_Lib.SERVO_MID_TIME)
            elif isinstance(pin, list):
                for i in pin:
                    self.adafruit.set_pwm(i,0, Adafruit_Ease_Lib.SERVO_MID_TIME)
            else:
                self.adafruit.set_pwm(pin, 0, Adafruit_Ease_Lib.SERVO_MID_TIME)

        elif percent < 50:

            percentage = percent
            value = int(percentage * (1/50) * (Adafruit_Ease_Lib.SERVO_MID_TIME-Adafruit_Ease_Lib.SERVO_LOW_TIME) + Adafruit_Ease_Lib.SERVO_LOW_TIME)
            print('moving to ' + str(value))
            if pin == 'all':
                self.adafruit.set_all_pwm(0, value)
            elif isinstance(pin, list):
                for i in pin:
                    self.adafruit.set_pwm(i, 0, value)
            else:
                self.adafruit.set_pwm(pin, 0, value)

        elif percent > 50:

            percentage = (percent - 50)
            value = int(percentage * (1 / 50) * (Adafruit_Ease_Lib.SERVO_MAX_TIME - Adafruit_Ease_Lib.SERVO_MID_TIME) + Adafruit_Ease_Lib.SERVO_MID_TIME)
            print('moving to ' + str(value))

            if pin == 'all':
                self.adafruit.set_all_pwm(0, value)
            elif isinstance(pin, list):
                for i in pin:
                    self.adafruit.set_pwm(i, 0, value)
            else:
                self.adafruit.set_pwm(pin, 0, value)
