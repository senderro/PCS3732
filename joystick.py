import threading
import time

from gpiozero import Button
from ADCDevice import *

Z_PIN = 7


class Joystick:

    def __init__(self, controller):

        self.controller = controller

        self.button = Button(Z_PIN)

        self.adc = ADCDevice(0x48)

        if self.adc.detectI2C(0x48):
            self.adc = ADS7830(0x48)
        else:
            raise RuntimeError("ADS7830 não encontrado")

        self.running = True

        self.thread = threading.Thread(target=self.loop)
        self.thread.daemon = True
        self.thread.start()

    def loop(self):

        while self.running:

            x = self.adc.analogRead(5)
            y = self.adc.analogRead(6)
            z = not self.button.value

            self.controller.joystick_changed(x, y, z)

            time.sleep(0.01)

    def close(self):

        self.running = False

        self.thread.join()

        self.button.close()
        self.adc.close()
