import turtle
import random

# import colorgram
#
# colors_from_picture = colorgram.extract("dots.jpg", 56)
# colors = []
# for color in colors_from_picture:
#     rgb = color.rgb
#     rgb_num = (rgb.r, rgb.g, rgb.b)
#     colors.append(rgb_num)


# Extract only once, because it's not necessary to do it everytime, and then I deleted few values from list,
# because these was background colors
colors = [(141, 176, 206), (25, 32, 48), (28, 105, 156),
          (208, 161, 112), (238, 222, 234), (230, 211, 94), (131, 31, 64), (5, 162, 195), (182, 45, 84), (217, 60, 85),
          (226, 80, 44), (195, 129, 168), (54, 167, 116), (29, 61, 115), (108, 181, 91), (109, 99, 88), (2, 102, 119),
          (193, 187, 47), (241, 204, 1), (19, 22, 21), (52, 149, 109), (171, 211, 173), (226, 170, 186),
          (150, 207, 222), (234, 169, 160), (184, 186, 210), (115, 38, 37), (82, 34, 76), (122, 118, 154), (28, 28, 28)]

rows = 10
columns = 5

turtle.colormode(255)
artist = turtle.Turtle()
artist.speed("fastest")
artist.penup()
artist.hideturtle()
artist.setposition(-250, -250)
for row in range(rows):
    for column in range(columns):
        artist.color(random.choice(colors))
        artist.dot(20)
        artist.forward(50)
    artist.setposition(-250, artist.ycor() + 50)

screen = turtle.Screen()
screen.exitonclick()
