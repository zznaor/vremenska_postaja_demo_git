### ova .py skripta sadrzi klase za senzore i aktuatore

import random
from gpiozero import Device, LED
from gpiozero.pins.mock import MockFactory

Device.pin_factory = MockFactory()

class Senzor:
    def __init__(self,naziv,pin):
        self.naziv = naziv
        self.pin = pin

    def ocitaj(self):
        raise NotImplementedError('Podklasa mora definirati ocitaj()')

    def __str__(self):
        return f'{self.naziv} - {self.pin}'

class TemperaturniSenzor(Senzor):
    def ocitaj(self):
        return round(random.uniform(18.0,30.0),1)

class SenzorPokreta(Senzor):
    def ocitaj(self):
        return random.choice([True,False])

class Aktuator:
    def __init__(self,naziv,pin):
        self.naziv = naziv
        self.led = LED(pin)

    def ukljuci(self):
        self.led.on()

    def iskljuci(self):
        self.led.off()

    def je_li_ukljucen(self):
        return self.led.is_lit

    def zatvori(self):
        self.led.close()


