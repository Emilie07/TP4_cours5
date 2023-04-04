#Emilie Mancera

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.AFRICAN_VIOLET, arcade.color.AMARANTH_PINK, arcade.color.ARYLIDE_YELLOW, arcade.color.BLEU_DE_FRANCE]

class Balle:
    def __init__(self, position_x, position_y, change_x, change_y, rayon, color):
        self.x = position_x
        self.y = position_y
        self.vx = change_x
        self.vy = change_y
        self.rayon = rayon
        self.color = color

    def on_update(self, delta_time: float):
        self.x += self.vx
        self.y += self.vy
        if self.x < self.rayon:
            self.x *= -1
        if self.x > SCREEN_WIDTH - self.rayon:
            self.x *= -1
        if self.y < self.rayon:
            self.y *= -1
        if self.y > SCREEN_HEIGHT - self.rayon:
            self.y *= -1

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)

class rectangle:
    def __init__(self, position_x, position_y, change_x, change_y, width, height, color, angle):
        self.x = position_x
        self.y = position_y
        self.vx = change_x
        self.vy = change_y
        self.width = width
        self.height = height
        self.color = color
        self.angle = 0

    def on_update(self, delta_time: float):
        arcade.start_render()


    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)
        super().__init__(width, height)
        self.liste.balles = []
        self.liste.rectangles = []

    def on_draw(self):
        arcade.start_render()
        for balles in self.liste.balle:
            balles.draw
        for rectangles in self.liste.rectangle:
            rectangles.draw

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            rayon = random.randint(10, 30)
            color = random.choice(COLORS)
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            balles = Balle(rayon, color, x, y)
            self.liste.balles.append(balles)
        if button == arcade.MOUSE_BUTTON_RIGHT:
            rectangles = Rectangle(x, y, width, height, color, angle)
            self.liste.rectangle.append(rectangle)

def main():
    my_game = MyGame()
    arcade.run()

main()