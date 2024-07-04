from random import randint


class Painter:
    def __init__(self, draw):
        self.draw = draw
        self.lift_pen()
        self.change_start()

    def change_start(self, distance=200):
        self.draw.setheading(225)
        self.draw.forward(distance)
        self.draw.setheading(0)

    def lift_pen(self):
        self.draw.penup()

    def paint_dot(self, color=(255, 255, 255), size=20):
        self.draw.dot(size, color)

    def random_color(self):
        return (randint(0, 255), randint(0, 255), randint(0, 255))

    def paint_grid(self, width=400, height=400, step=10):
        x = self.draw.xcor()
        y = self.draw.ycor()
        direction = 1

        while x < width or y < height:
            self.paint_dot(color=self.random_color())

            self.draw.forward(step)

            x += direction * step

            if x >= width:
                self.paint_dot(color=self.random_color())

                self.draw.left(90)
                self.draw.forward(step)
                self.draw.left(90)
                y += step

                direction = -1

            elif x <= 0:
                self.paint_dot(color=self.random_color())

                self.draw.right(90)
                self.draw.forward(step)
                self.draw.right(90)

                direction = 1

                y += step
