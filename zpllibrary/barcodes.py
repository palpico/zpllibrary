from zpllibrary.shared import PositionedElement


class Barcode(PositionedElement):
    def __init__(self, content, x, y, height, orientation, print_interpretation_line,
                 print_interpretation_line_above_code):
        super().__init__(x, y)
        self.content = content
        self.height = height
        self.orientation = orientation
        self.print_interpretation_line = print_interpretation_line
        self.print_interpretation_line_above_code = print_interpretation_line_above_code


class Barcode39(Barcode):
    def __init__(self, content, x, y, height=100, orientation="N", print_interpretation_line=True,
                 print_interpretation_line_above_code=False, mod_43_check_digit=False):
        super().__init__(content, x, y, height, orientation, print_interpretation_line,
                         print_interpretation_line_above_code)

        self.mod_43_check_digit = mod_43_check_digit

    def render(self, options):
        text = self.origin.render(options)
        text = text + "^B3" + self.orientation + ","
        text = text + "Y" if self.mod_43_check_digit else text + "N"
        text = text + ","
        text = text + str(options.scale(self.height)) + ","
        text = text + "Y" if self.print_interpretation_line else text + "N"
        text = text + ","
        text = text + "Y" if self.print_interpretation_line_above_code else text + "N"
        text = text + "^FD" + self.content + "^FS"
        return text

class Barcode128(Barcode):
    def __init__(self, content, x, y, height=100, orientation="N", print_interpretation_line=True,
                 print_interpretation_line_above_code=False):
        super().__init__(content, x, y, height, orientation, print_interpretation_line,
                         print_interpretation_line_above_code)

    def render(self, options):
        text = self.origin.render(options)
        text = text + "^BC" + self.orientation + ","
        text = text + str(options.scale(self.height)) + ","
        text = text + "Y" if self.print_interpretation_line else text + "N"
        text = text + ","
        text = text + "Y" if self.print_interpretation_line_above_code else text + "N"
        text = text + "^FD" + self.content + "^FS"
        return text

class BarcodeAnsi(Barcode):
    def __init__(self, content, x, y, height, start_char, stop_char, orientation="N", print_interpretation_line=True,
                 print_interpretation_line_above_code=False, check_digit=False):
        super().__init__(content, x, y, height, orientation, print_interpretation_line,
                         print_interpretation_line_above_code)
        self.start_char = start_char
        self.stop_char = stop_char
        self.check_digit = check_digit

    def render(self, options):
        text = self.origin.render(options)
        text = text + "^BK" + self.orientation + ","
        text = text + "Y" if self.check_digit else text + "N"
        text = text + ","
        text = text + str(options.scale(self.height)) + ","
        text = text + "Y" if self.print_interpretation_line else text + "N"
        text = text + ","
        text = text + "Y" if self.print_interpretation_line_above_code else text + "N"
        text = text + "^FD" + self.content + "^FS"

        return text


