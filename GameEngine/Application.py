from tkinter import *
from PIL import ImageTk, Image
from GameEngine.Vector import *


class Application:
    def __init__(self, title, size, fps):
        self.root = Tk()
        self.root.title(title)

        self.width, self.height = size
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.bind("<Key>", self.__handle_key_press)

        self.fps = fps

        self.__widgets = []
        self.__task_list = []
        self.__game_objects = []
        self.__action_listeners = []

        self.root.after(int((1 / self.fps) * 1000), self.new_frame)

    def render_window(self):
        for slave in self.root.slaves():
            slave.destroy()

        for widget in self.__widgets:
            widget[0].place(x=widget[1], y=widget[2])

        self.execute_task_list()

        self.root.after(int((1 / self.fps) * 1000), self.new_frame)

    def new_frame(self):
        sprites = []

        for obj in self.__game_objects:
            render_result = obj.render()

            if render_result is not None:
                sprites.append((render_result, obj.position, obj.rotation))

        frame = Frame((self.width, self.height))

        for sprite in sprites:
            frame.write_sprite(sprite)

        frame = ImageTk.PhotoImage(frame.image)

        self.__widgets = [
            [
                Label(self.root, image=frame),
                0, 0
            ]
        ]

        self.__widgets[0][0].image = frame

        self.render_window()

    def execute_task_list(self):
        for task in self.__task_list:
            task()

    def add_object(self, object):
        self.__game_objects.append(object)
        self.__task_list.append(object.update)

    def add_action_listener(self, obj):
        self.__action_listeners.append(obj)

    def __handle_key_press(self, event):
        for action_listener in self.__action_listeners:
            if action_listener.key == event.char:
                action_listener.action()

    def bind_special_key(self, key_name, f):
        self.root.bind(key_name, f)


class Frame:
    def __init__(self, size):
        self.width, self.height = size
        self.image = Image.new("RGBA", size=(self.width, self.height))
        self.image.putdata([(0, 0, 0, 255) for i in range(0, self.width * self.height)])

    def write_sprite(self, sprite_data):
        sprite, position, rotation = sprite_data

        pixels_ = self.image.getdata()
        pixels = []

        p_counter = 0
        for y in range(0, self.image.height):
            pixels.append([])
            for x in range(0, self.image.width):
                pixels[y].append(pixels_[p_counter])
                p_counter += 1

        sprite_pixels_ = sprite.getdata()
        sprite_pixels = []
        p_counter = 0
        for y in range(0, sprite.height):
            sprite_pixels.append([])
            for x in range(0, sprite.width):
                sprite_pixels[y].append(sprite_pixels_[p_counter])
                p_counter += 1

        p_counter = 0
        write_position = position
        pixel_position = Vector()
        for y in range(0, len(sprite_pixels)):
            for x in range(0, len(sprite_pixels[pixel_position.y])):
                pixels[write_position.y][write_position.x] = sprite_pixels[pixel_position.y][pixel_position.x]
                p_counter += 1
                write_position += Vector(1, 0)
                pixel_position += Vector(1, 0)

            pixel_position.x = 0
            pixel_position.y += 1

            write_position.x = position.x
            write_position.y += 1

        new_data = []
        for y in range(0, len(pixels)):
            for x in range(0, len(pixels[y])):
                new_data.append(pixels[y][x])

        self.image.putdata(new_data)
