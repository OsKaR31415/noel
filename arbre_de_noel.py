#!/usr/bin/python3
from colors import Color
from math import cos, sin, pi
import random
from random import random
from shutil import get_terminal_size
from sys import maxsize, stdout


def noise(point):
    return abs(hash(str(point)) / maxsize)


# the maths here are not obvious, because he basis of the tree is also
# responsive... but it is not really important since 3 works up tu huge heights
# (where the tree does not look like anything at all)
H = int(10*get_terminal_size().lines/11 - 3)

# create a colorizer (helps to color text in the terminal)
color = Color()


# size of the border (to display more snow)
border = (get_terminal_size().columns - H)//2

# initialize the text to print with new lines (so previouss text gets )
result = "\n"*3

# first put the star at the top of the tree !
result += color('yellow', "☆").center(H+1+2*border+7) + "\n"

for y in range(1, H):
    for x in range(-H//2 - border, H//2 + border):
        # leaves of the left side
        # y = 2x
        if x == y//2:
            result += color(28, "╲")
        # leaves of the right side
        # droite y = -2x
        elif x == -y//2:
            result += color(28, "╱")
        # outside of the tree
        # before / after the leaves
        elif x < -y//2 or x > y//2:
            # some snow !
            if 0.02 > random():
                result += color(81, "⋅")
            elif 0.02 > random():
                result += color(81, ".")
            elif 0.01 > random():
                result += color(51, "❄")
            else:
                result += " "
        # garlands : cosinus functions
        # first garland: at the top, high frequency
        elif y == int((H/2)-(H/30)*cos(x*0.8)):
            result += color(153, "※")
        # second garland : at the bottom, high frequency
        elif y == int((6*H/7)-(H/20)*cos(1+x/2.3)):
            result += color(153, "※")
        # here the bulb
        # the probability gets bigger with y
        elif 0.02 > random() * H/y:
            result += color(28, "ƠÔ"[random() > .5])
        elif 0.01 > random() * H/y:
            result += color(88, "ƠÔ"[random() > .5])
        else:
            result += " "
    result += "\n"
# bottom spikes, hard to always perfectly center them
result += color(28, ' '*(border) + "╱╲"*((1+H)//2))

# base of the tree
result += (H//8) * ('\n' + color(94, ("|"*(H//5)).center(H+2*border)))


print(result)


# very golfed and simplifed version :
# print((lambda H:'^'.center(H+2)+'\n'+'\n'.join([''.join(['\\'if x==y//2 else('/' if x==-y//2 else(' 'if(x>y//2)or(x<-y//2)else'           *O~'[__import__('random').randint(0,13)]))for x in range(-H//2,H//2)])for y in range(2,H)]+['^'*H]+['| |'.center(H+2)]*(1+H//10)+['']))(int(input(">"))))
