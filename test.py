from GameEngine.Application import *
from GameEngine.GameObject import *
from GameEngine.Vector import *
from GameEngine.Components.Sprite import *
from GameEngine.ActionListener import *


class Player:
    def __init__(self):
        self.game_object = GameObject("player", Vector(50, 50), Vector(0, 0))
        self.game_object.add_component(Sprite(image=Image.new("RGBA", size=(50, 50), color=(0, 255, 0, 255))))

        self.game_object.update = self.update
        self.speed = Vector(1, 0)

    def update(self):
        self.game_object.position += self.speed


class Game:
    def __init__(self):
        self.player = Player()

        self.app = Application("Hello world", (500, 500), 1)
        self.app.add_object(self.player.game_object)

        self.app.add_action_listener(ActionListener('a', self.a_key_action))

    def mainloop(self):
        self.app.root.mainloop()

    def a_key_action(self):
        self.player.speed *= Vector(2, 2)


if __name__ == "__main__":
    game = Game()
    game.mainloop()
