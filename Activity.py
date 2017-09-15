from playsound import playsound
from random import randint
import time
import Serial_code as sc
import playlist

def first():  # second mode : matching card
    # intro
    playsound('sound/PMmode/start1.wav')
    # tell group
    playsound('sound/PMmode/start4.wav')
    # please say group card
    playsound('sound/PMmode/start5.wav')
    group = 1
    # sound and figure
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
            time.sleep(1)
            playsound('sound/PMmode/Animal/' + str(number) + '.mp3')
            sc.Picture(group, number)
            robotmode, reply, kick, group2, number2 = sc.RFID_card()
            if robotmode == None & reply == None & kick == None & group2 == None :
                if group2 == group & number2 == number:
                    playlist.correct()
                elif group2 != group & number2 == number:
                    playlist.incorrect()
                elif group2 != group & number2 == number:
                    playlist.incorrect()





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
            time.sleep(1)
            num_array.append(int(number))
            playsound('sound/PMmode/Appliance/' + str(number) + '.mp3')
            sc.Picture(group, number)
            time.sleep(3)

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
            sc.Picture(group, number)
            time.sleep(3)
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
            sc.Picture(group, number)
            time.sleep(3)

    elif group == 0:
        playsound('sound/Bye/5.wav')
    time.sleep(3)
    playsound('sound/PMmode/end.wav')


def second():  # Fourth mode : Healthy question
    playsound('sound/HQmode/start.wav')
    # Question1
    playsound('sound/HQmode/Question/1.wav')
    # Question2
    playsound('sound/HQmode/Question/2.wav')
    # Question3
    playsound('sound/HQmode/Question/3.wav')
    # Question4
    playsound('sound/HQmode/Question/4.wav')
    # Question5
    playsound('sound/HQmode/Question/5.wav')
    # Question6
    playsound('sound/HQmode/Question/6.wav')
    # End
    playsound('sound/HQmode/end.wav')

def third():  # Quiz mode : Quiz question "What is this?"
    # Start
    playsound('sound/QQmode/start1.wav')
    group = 1
    # Random number 1 mode 3 question
    if group == 1:
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
    elif group == 2:
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
    elif group == 3:
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
    elif group == 4:
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

def fourth():  # number question : result will be not higher than 100
    playsound('sound/NQmode/start.wav')
    for i in range(0, 5):
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

def fifth(): # Remember game : remember number robot say
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
    first()
