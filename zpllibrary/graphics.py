from zpllibrary.shared import PositionedElement

class GraphicElement(PositionedElement):
    def __init__(self, x, y, line_colour="B", border_thickness=1):
        super().__init__(x, y)
        self.line_colour = line_colour
        self.border_thickness = border_thickness


class GraphicBox(GraphicElement):
    def __init__(self, x, y, width, height, line_colour="B", border_thickness=1, corner_rounding=0):
        super().__init__(x, y, line_colour, border_thickness)
        self.width = width
        self.height = height
        self.corner_rounding = corner_rounding

    def render(self, options):
        text = self.origin.render(options)
        text = text + "^GB"
        text = text + options.scale_to_string(self.width) + ","
        text = text + options.scale_to_string(self.height) + ","
        text = text + options.scale_to_string(self.border_thickness) + ","
        text = text + self.line_colour + ","
        text = text + options.scale_to_string(self.corner_rounding)
        text = text + "^FS"
        return text

class GraphicCircle(GraphicElement):
    def __init__(self, x, y, diameter, line_colour="B", border_thickness=1):
        super().__init__(x, y, line_colour, border_thickness)
        self.diameter = diameter

    def render(self, options):
        text = self.origin.render(options)
        text = text + "^GC"
        text = text + options.scale_to_string(self.diameter) + ","
        text = text + options.scale_to_string(self.border_thickness) + ","
        text = text + self.line_colour
        text = text + "^FS"
        return text

class GraphicDiagonalLine(GraphicBox):
    def __init__(self, x, y, width, height, leaning_diagonal_right=False, line_colour="B", border_thickness=1):
        super().__init__(x, y, width, height, line_colour, border_thickness, 0)
        self.leaning_diagonal_right = leaning_diagonal_right

    def render(self, options):
        text = self.origin.render(options)
        text = text + "^GD"
        text = text + options.scale_to_string(self.width) + ","
        text = text + options.scale_to_string(self.height) + ","
        text = text + options.scale_to_string(self.border_thickness) + ","
        text = text + self.line_colour + ","
        text = text + "R" if self.leaning_diagonal_right else text + "L"
        text = text + "^FS"
        return text


class GraphicEllipse(GraphicBox):
    def __init__(self, x, y, width, height, line_colour="B", border_thickness=1):
        super().__init__(x, y, width, height, line_colour, border_thickness, 0)

    def render(self, options):
        text = self.origin.render(options)
        text = text + "^GE"
        text = text + options.scale_to_string(self.width) + ","
        text = text + options.scale_to_string(self.height) + ","
        text = text + options.scale_to_string(self.border_thickness) + ","
        text = text + self.line_colour
        text = text + "^FS"
        return text


class GraphicHorizontalLine(GraphicBox):
    def __init__(self, x, y, width, line_colour="B", line_thickness=1):
        super().__init__(x, y, width, 0, line_colour, line_thickness, 0)

    def render(self, options):
        return super().render(options)


class GraphicSymbol(PositionedElement):
    def __init__(self, character, x, y, width, height, orientation="N"):
        super().__init__(x, y)
        self.character = character
        self.width = width
        self.height = height
        self.orientation = orientation

    def render(self, options):
        text = self.origin.render(options)
        text = text + "^GS" + ","
        text = text + self.orientation + ","
        text = text + options.scale_to_string(self.height) + ","
        text = text + options.scale_to_string(self.width)
        text = text + "^FD"
        text = text + self.character.value
        text = text + "^FS"
        return text

class GraphicVerticalLine(GraphicBox):
    def __init__(self, x, y, height, line_colour="B", line_thickness=1):
        super().__init__(x, y, 0, height, line_colour, line_thickness, 0)

    def render(self, options):
        return super().render(options)