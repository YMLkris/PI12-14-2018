from sense_emu import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

#set variables here

white = [255,255,255]
blue = [0,0,255]

# Set variables
sense.clear()
black = [0,0,0]
snake = [ [2,4], [3,4], [4,4] ]
berry =[]
direction = "right"
score = 0
dead = False

def make_berry():
    x = randint(0,7)
    y = randint(0,7)
    new = [x,y]
    berry.append(new)
    for segment in berry:
        sense.set_pixel(segment[0], segment[1], blue)
    
    
def draw_snake():
    for segment in snake:
        sense.set_pixel(segment[0], segment[1], white)


def move():

    global score
    global dead
    remove = True

    # Find the last and first items in the snake list
    last = snake[-1]
    first = snake[0]
    next = list(last)

    # Find the next pixel in the direction the snake is moving

    if direction == "right":

        if last[0] + 1 == 8:
            next[0] = 0
        else:
            next[0] = last[0] + 1

    if direction == "left":

        if last[0] - 1 == -1:
            next[0] = 7
        else:
            next[0] = last[0] - 1

    if direction == "down":
        if last[1] + 1 == 8:
            next[1] = 0
        else:
            next[1] = last[1] + 1

    if direction == "up":
        if last[1] - 1 == -1:
            next[1] = 7
        else:
            next[1] = last[1] - 1

    #Add this new pixel to the end of the list

    if next in snake:
        dead = True
        print("Game Over, you bit yourself!")

    snake.append(next)

    sense.set_pixel(next[0], next[1], white)

    if score % 5 == 0 and score != 0:
        remove = False
        score +=1
    else:
        remove = True
        
    if remove == True:
        sense.set_pixel(first[0], first[1], black)
        snake.remove(first)
        
    if next in berry:
        berry.remove(next)
        score += 1
        print(score)
   

def joystick_moved(event):
    global direction
    direction = event.direction
    
while dead == False:

    sense.stick.direction_any = joystick_moved
    move()
    draw_snake()
    sleep(.5)
    if len(berry) < 3 and randint(1, 5) > 4:
        make_berry()
    

sense.show_message("Game over man!")

