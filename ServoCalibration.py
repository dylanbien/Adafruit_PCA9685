from Adafruit_Ease_Lib import Adafruit_Ease_Lib as al
from time import sleep

#USE THIS FILE IN A COMMAND LINE


pin = input('enter the pin of the servo: ')

adafruit = al()
adafruit.change_percentage_servo(int(pin), 50)
response = input('Is it centered?(y/n): ')
pwm_val = 0
k = adafruit.SERVO_MID_TIME
while response == 'n':
    pwm_val = int(input('Enter how much you want to change it by: '))
    k += pwm_val
    print(k)
    sleep(2)
    #adafruit.change_percentage_servo(int(pin), 50)
    adafruit.adafruit.set_pwm(int(pin), 0, k)
    response = input('Is it centered?(y/n): ')

adafruit.SERVO_LOW_TIME += pwm_val
adafruit.SERVO_MAX_TIME += pwm_val

print('HERE ARE YOUR NEW PWM VALUES [LEFT,MID,CENTER]: '+ str(adafruit.SERVO_LOW_TIME) + ' , ' + str(adafruit.SERVO_MID_TIME) +' , '+str(adafruit.SERVO_MAX_TIME))
