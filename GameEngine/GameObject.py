class GameObject:
    def __init__(self, name, position, rotation):
        self.name = name
        self.position = position
        self.rotation = rotation
        self.__components = []

    def start(self):
        pass

    def update(self):
        pass

    def add_component(self, obj):
        self.__components.append(obj)

    def render(self):
        out = None

        for component in self.__components:
            if str(component) == "sprite":
                out = component.image

        return out

    def __getitem__(self, index):
        return self.__components[index]

    def __len__(self):
        return len(self.__components)
