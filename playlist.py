from playsound import playsound
from random import randint

def correct():
    number = randint(1, 5)
    playsound('sound/Response/C' + number + '.wav')

def incorrect():
    number = randint(1, 3)
    playsound('sound/Response/C' + number + '.wav')
