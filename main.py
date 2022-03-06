# import colorgram
#
# colors = colorgram.extract('image1.jpg', 50)
#
#
# def color_list():
#     list_rgb = []
#     for i in colors:
#         rgb = i.rgb
#         list_rgb += rgb
#     new_list = []
#     for i in range(0,len(list_rgb),3):
#         new_list.append(tuple(list_rgb[i:i+3]))
#     return new_list
#
# print(color_list())

from turtle import Turtle, Screen
import random


color_list = [(154, 80, 38), (244, 231, 236), (207, 159, 105), (181, 175, 18), (108, 165, 210), (25, 91, 160), (106, 176, 124), (194, 91, 105), (13, 37, 97), (72, 43, 23), (50, 121, 23), (187, 133, 150), (94, 192, 47), (106, 32, 54), (195, 94, 75), (25, 97, 25), (100, 120, 169), (180, 206, 170), (250, 169, 173), (24, 53, 110), (251, 171, 163), (149, 191, 244), (104, 60, 18), (81, 30, 46), (132, 79, 90), (18, 75, 105), (91, 153, 156), (45, 49, 45), (104, 52, 26), (161, 202, 213), (213, 203, 31)]

tim = Turtle()
tim.speed("fastest")
screen = Screen()

screen.colormode(255)
tim.penup()


def timmy_hirst_dots():
    pick = random.choice(color_list)
    tim.color(pick)
    tim.dot(20)


def timmy_hirst_lines():
    for i in range(1, 11):
        timmy_hirst_dots()
        tim.forward(50)


x = -225

for i in range(1,11):
    tim.setposition(-225, x)
    timmy_hirst_lines()
    x += 50

screen.exitonclick()

