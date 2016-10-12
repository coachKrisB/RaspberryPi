from sense_hat import SenseHat

def Display_Temp():
    sense = SenseHat()
    print("Temp:{}".format(sense.temperature))
    curTemp = sense.temperature *9/5 + 32
    sense.show_message("Temp:{}".format(curTemp))    


sense = SenseHat()
sense.low_light = True
#sense.show_message("Hello world!")

sense = SenseHat()



X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White
B = [0, 0, 255] #Blue
G = [0, 255, 0] #Green
N = [0, 0, 0] #No Color

question_mark = [
B, O, O, X, X, O, O, B,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
G, O, O, X, O, O, O, G
]

up_arrow = [
B, O, N, G, G, O, O, B,
O, O, N, G, G, O, O, O,
O, N, G, G, G, G, O, O,
N, G, G, G, G, G, G, O,
O, O, N, G, G, O, O, O,
O, O, N, G, G, O, O, O,
O, O, N, G, G, O, O, O,
G, O, N, G, G, O, O, G
]


sense.set_pixels(up_arrow)
lastTemp = 0
directionUp = True

from time import sleep

while True:
    print("Top of While")
    sense.set_pixels(question_mark)

    Display_Temp()
    print("Rel-Hum:{}".format(sense.get_humidity()))

    curTemp = sense.temp

    print("lastTemp:{},{}:curTemp".format(curTemp,lastTemp))
    print(lastTemp<curTemp)
    if (lastTemp < curTemp):
        directionUp = False
        print("Going Down")
    else:
        directionUp = True
        print("Going Up")

    lastTemp = curTemp
    
    if directionUp:
        sense.set_rotation(0)
        sense.set_pixels(up_arrow)
    else:
        sense.set_rotation(180)
        sense.set_pixels(up_arrow)
        
    print("Bottom of While")        
    sleep(5)


