from Adafruit_Ease_Lib import Adafruit_Ease_Lib as al
import Events
#USE THIS FILE IN A COMMAND PROMPT

class MyEvents(Events):
     __events__ = ('on_this', 'on_that')

pin = input('enter the pin of the servo')

adafruit = al()
adafruit.change_percentage_servo(int(pin))
response = input('Is it centered?(Y/N)')
if response == 'N':
