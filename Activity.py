from playsound import playsound
from random import randint
import time
from time import gmtime, strftime
import sounddevice as sd
import soundfile as sf

samplerate = 44100  # Hertz
duration = 4  # seconds

def first():  # first mode for offline : greeting
    number = randint(0, 2)
    if number == 0:
        print("Robot said")
        playsound('sound/Greeting/1.mp3')
    elif number == 1:
        print("Robot said")
        playsound('sound/Greeting/2.wav')
    elif number == 2:
        print("Robot said")
        playsound('sound/Greeting/3.mp3')

def second():  # second mode : matching card
    # intro
    playsound('sound/PMmode/start1.wav')
    # tell mode
    # playsound('sound/PMmode/start2.wav')
    # please say mode
    # playsound('sound/PMmode/start3.wav')
    mode = 1  # 1 - 3 mode
    # tell group
    playsound('sound/PMmode/start4.wav')
    # please say group card
    playsound('sound/PMmode/start5.wav')
    group = 1  # 1 - 4 group card
    # sound and figure
    if mode == 1:
        # Animal
        if group == 1:
            print("mode 1 = Sound and figure group 1 = animal")
            # random number not same number
            num_array = list()
            for i in range(0, 10):
                same = True
                while same:
                    number = randint(1, 27)
                    if len(num_array) >= 1:
                        for j in range(0, len(num_array)):
                            if num_array[j] == number:
                                break
                            if j == len(num_array)-1:
                                same = False
                                break
                    elif len(num_array) < 1:
                        same = False
                # collect in array
                num_array.append(int(number))
                # tell number
                playsound('sound/PMmode/Animal/' + str(num_array[i]) + '.mp3')
        # appliance
        elif group == 2:
            print("mode 1 = Sound and figure group 2 = appliance")
            # random number not same number
            num_array = list()
            for i in range(0, 10):
                same = True
                while same:
                    number = randint(1, 26)
                    if len(num_array) >= 1:
                        for j in range(0, len(num_array)):
                            if num_array[j] == number:
                                break
                            if j == len(num_array)-1:
                                same = False
                                break
                    elif len(num_array) < 1:
                        same = False
                # collect in array
                num_array.append(int(number))
                playsound('sound/PMmode/Appliance/' + str(number) + '.mp3')
        # toy
        elif group == 3:
            print("mode 1 = Sound and figure group 3 = toy")
            # random number not same number
            num_array = list()
            for i in range(0, 10):
                same = True
                while same:
                    number = randint(1, 28)
                    if len(num_array) >= 1:
                        for j in range(0, len(num_array)):
                            if num_array[j] == number:
                                break
                            if j == len(num_array)-1:
                                same = False
                                break
                    elif len(num_array) < 1:
                        same = False
                # collect in array
                num_array.append(int(number))
                playsound('sound/PMmode/Toy/' + str(number) + '.mp3')
        # fruit
        elif group == 4:
            print("mode 1 = Sound and figure group 4 = fruit")
            # random number not same number
            num_array = list()
            for i in range(0, 10):
                same = True
                while same:
                    number = randint(1, 25)
                    if len(num_array) >= 1:
                        for j in range(0, len(num_array)):
                            if num_array[j] == number:
                                break
                            if j == len(num_array)-1:
                                same = False
                                break
                    elif len(num_array) < 1:
                        same = False
                # collect in array
                num_array.append(int(number))
                playsound('sound/PMmode/Fruit/' + str(number) + '.mp3')
    time.sleep(3)
    playsound('sound/PMmode/end.wav')

def third():  # third mode : Alarming event Remember mode
    playsound('sound/RMmode/start.wav')
    # playsound('sound/RMmode/alarm01.wav')

def fourth():  # Fourth mode : Healthy question
    playsound('sound/HQmode/start.wav')
    # Question1
    playsound('sound/HQmode/Question/1.wav')
    # collect sound
    Day = strftime("%Y-%m-%d", gmtime())
    Time = strftime("%H-%M-%S", gmtime())
    filename = 'sound/HQmode/answer/a1_' + Day + '_' + Time + '.wav'
    mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
                channels=2, blocking=True)
    sf.write(filename, mydata, samplerate)
    # Question2
    playsound('sound/HQmode/Question/2.wav')
    # collect sound
    Day = strftime("%Y-%m-%d", gmtime())
    Time = strftime("%H-%M-%S", gmtime())
    filename = 'sound/HQmode/answer/a2_' + Day + '_' + Time + '.wav'
    mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
                channels=2, blocking=True)
    sf.write(filename, mydata, samplerate)
    # Question3
    playsound('sound/HQmode/Question/3.wav')
    # collect sound
    Day = strftime("%Y-%m-%d", gmtime())
    Time = strftime("%H-%M-%S", gmtime())
    filename = 'sound/HQmode/answer/a3_' + Day + '_' + Time + '.wav'
    mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
                channels=2, blocking=True)
    sf.write(filename, mydata, samplerate)
    # Question4
    playsound('sound/HQmode/Question/4.wav')
    # collect sound
    Day = strftime("%Y-%m-%d", gmtime())
    Time = strftime("%H-%M-%S", gmtime())
    filename = 'sound/HQmode/answer/a4_' + Day + '_' + Time + '.wav'
    mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
                channels=2, blocking=True)
    sf.write(filename, mydata, samplerate)
    # Question5
    playsound('sound/HQmode/Question/5.wav')
    # collect sound
    Day = strftime("%Y-%m-%d", gmtime())
    Time = strftime("%H-%M-%S", gmtime())
    filename = 'sound/HQmode/answer/a5_' + Day + '_' + Time + '.wav'
    mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
                channels=2, blocking=True)
    sf.write(filename, mydata, samplerate)
    # Question6
    playsound('sound/HQmode/Question/6.wav')
    # collect sound
    Day = strftime("%Y-%m-%d", gmtime())
    Time = strftime("%H-%M-%S", gmtime())
    filename = 'sound/HQmode/answer/a6_' + Day + '_' + Time + '.wav'
    mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
                channels=2, blocking=True)
    sf.write(filename, mydata, samplerate)
    # End
    playsound('sound/HQmode/end.wav')

def fifth():  # Quiz mode : Quiz question "What is this?"
    # Start
    playsound('sound/QQmode/start1.wav')
    # Ask for select Group card
    playsound('sound/QQmode/start2.wav')
    # Select Group card
    playsound('sound/QQmode/start3.wav')
    # Group card
    Group = 1  # 1-4
    # Random number 1 mode 3 question
    if Group == 1:
        print("Question in Animal group")
    # random number not same number
        num_array = list()
        for i in range(0, 3):
            same = True
            while same:
                number = randint(1, 10)
                if len(num_array) >= 1:
                    for j in range(0, len(num_array)):
                        if num_array[j] == number:
                            break
                        if j == len(num_array)-1:
                            same = False
                            break
                elif len(num_array) < 1:
                    same = False
            # collect in array
            num_array.append(int(number))
            playsound('sound/QQmode/quiz/Animal/' + str(num_array[i]) + '.wav')
    elif Group == 2:
        print("Question in Appliance group")
    # random number not same number
        num_array = list()
        for i in range(0, 3):
            same = True
            while same:
                number = randint(1, 10)
                if len(num_array) >= 1:
                    for j in range(0, len(num_array)):
                        if num_array[j] == number:
                            break
                        elif j == len(num_array)-1:
                            same = False
                            break
                elif len(num_array) < 1:
                    same = False
            # collect in array
            num_array.append(int(number))
            playsound('sound/QQmode/quiz/Appliance/' + str(num_array[i]) + '.wav')
    elif Group == 3:
        print("Question in Toy group")
    # random number not same number
        num_array = list()
        for i in range(0, 3):
            same = True
            while same:
                number = randint(1, 10)
                if len(num_array) >= 1:
                    for j in range(0, len(num_array)):
                        if num_array[j] == number:
                            break
                        elif j == len(num_array)-1:
                            same = False
                            break
                elif len(num_array) < 1:
                    same = False
            # collect in array
            num_array.append(int(number))
            playsound('sound/QQmode/quiz/Toy/' + str(num_array[i]) + '.wav')
    elif Group == 4:
        print("Question in Fruit group")
    # random number not same number
        num_array = list()
        for i in range(0, 3):
            same = True
            while same:
                number = randint(1, 10)
                if len(num_array) >= 1:
                    for j in range(0, len(num_array)):
                        if num_array[j] == number:
                            break
                        elif j == len(num_array):
                            same = False
                            break
                elif len(num_array) < 1:
                    same = False
            # collect in array
            num_array.append(int(number))
            playsound('sound/QQmode/quiz/Fruit/' + str(num_array[i]) + '.wav')
    playsound('sound/QQmode/end.wav')

def sixth():  # shutdown mode : robot will say goodbye : offline mode
    number = randint(0, 2)
    if number == 0:
        print("Robot said")
        playsound('sound/Bye/1.wav')
    elif number == 1:
        print("Robot said")
        playsound('sound/Bye/2.wav')
    elif number == 2:
        print("Robot said")
        playsound('sound/Bye/3.wav')
    elif number == 3:
        print("Robot said")
        playsound('sound/Bye/4.wav')
    elif number == 4:
        print("Robot said")
        playsound('sound/Bye/5.wav')

def seventh():  # number question : result will be not higher than 100
    playsound('sound/NQmode/start.wav')
    number1 = randint(0, 99)
    playsound('sound/NQmode/number/' + str(number1) + '.wav')
    playsound('sound/NQmode/mark/add.wav')
    number2 = randint(0, 99)
    while number2 + number1 >= 100:
        number2 = randint(0, 99)
    playsound('sound/NQmode/number/' + str(number2) + '.wav')
    playsound('sound/NQmode/mark/Equal.wav')
    time.sleep(5)
    playsound('sound/NQmode/end.wav')

def eighth(): # Remember game : remember number robot say
    playsound('sound/RQmode/start.wav')
    num_array = list()
    for i in range(0, 10):
        n = randint(0, 9)
        num_array.append(int(n))
        for i in range(0, len(num_array)):
            playsound('sound/RQmode/number/' + str(num_array[i]) + '.wav')
        if i >= 1:
            time.sleep(5+i)
            correct = True
            if not correct:
                break
        elif i < 1:
            time.sleep(5+i)
    playsound('sound/RQmode/end.wav')

if __name__ == '__main__':
    fifth()
