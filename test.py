from GameEngine.Application import *
from GameEngine.GameObject import *
from GameEngine.Vector import *
from GameEngine.Components.Sprite import *
from GameEngine.ActionListener import *
import sys


class Player:
    def __init__(self):
        self.game_object = GameObject("player", Vector(50, 50), Vector(0, 0))
        self.game_object.add_component(Sprite(image=Image.new("RGBA", size=(50, 50), color=(0, 255, 0, 255))))

        self.game_object.update = self.update
        self.speed = Vector(10, 0)

    def update(self):
        self.game_object.position += self.speed


class Game:
    def __init__(self):
        self.player = Player()

        self.app = Application("Hello world", (500, 500), 60)
        self.app.add_object(self.player.game_object)

        self.app.bind_special_key("<Right>", self.right_arrow)
        self.app.bind_special_key("<Left>", self.left_arrow)
        self.app.bind_special_key("<Up>", self.up_arrow)
        self.app.bind_special_key("<Down>", self.down_arrow)
        self.app.bind_special_key("<Escape>", self.exit)

    def mainloop(self):
        self.app.root.mainloop()

    def right_arrow(self, event):
        self.player.speed = Vector(10, 0)

    def left_arrow(self, event):
        self.player.speed = Vector(-10, 0)

    def up_arrow(self, event):
        self.player.speed = Vector(0, -10)

    def down_arrow(self, event):
        self.player.speed = Vector(0, 10)

    def exit(self, event):
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.mainloop()
