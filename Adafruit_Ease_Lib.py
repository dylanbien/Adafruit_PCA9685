import Adafruit_PCA9685


HIGH = 4096
LOW = 0


class Adafruit_Ease_Lib(Adafruit_PCA9685)
def __init__(self,*args,**kwargs):
    self.adafruit = Adafruit_PCA9685.PCA9685(address = kwargs.get('address',40))
    self.num_pins = 16
    print('Adafruit initialized')

def set_high(self, pin):
    if pin == 'all':
        set_all_pwm(HIGH,LOW)
    elif isinstance(pin, list):
        for i in range(pin):
            self.adafruit.set_pwm(i, HIGH, LOW) 
        
      
      
