class Stationery:
    def __init__(self, title="Something that can draw"):
        self.title = title

    def draw(self):
        print(f"Just start drawing! {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Start write with {self.title} pen!")


class Pencil(Stationery):
    def draw(self):
        print(f"Start decorate with {self.title} pencil!")


class Marker(Stationery):
    def draw(self):
        print(f"Start highlight with {self.title} marker!")


stat = Stationery()
stat.draw()
pen = Pen("Big")
pen.draw()
pencil = Pencil("Faber-Castell")
pencil.draw()
marker = Marker("Erich Krause")
marker.draw()