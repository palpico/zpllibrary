class Origin:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def render(self, options):
        return "^FO" + str(options.scale(self.x)) + "," + str(options.scale(self.y))


class PositionedElement(object):
    def __init__(self, x, y):
        self.origin = Origin(x, y)