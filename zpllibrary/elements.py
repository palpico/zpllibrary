from zpllibrary.models import NewLineConversion
from zpllibrary.shared import PositionedElement


class TextField(PositionedElement):
    def __init__(self, text, x, y, font, use_hexadecimal_indicator, reverse_print, new_line_conversion):
        super().__init__(x, y)
        self.text = text
        self.font = font
        self.hex_indicator = use_hexadecimal_indicator
        self.reverse = reverse_print
        self.new_line_conversion = new_line_conversion

    def render(self, options):
        text = self.font.render(options)
        text = text + self.origin.render(options)
        text = text + self.render_field_data()
        return text

    def render_field_data(self):
        text = "^FH" if self.hex_indicator else ""
        text = text + "^FR" if self.reverse else text + ""
        text = text + '^FD'

        for char in self.text:
            text = text + self.sanitise(char)

        text = text + '^FS'
        return text


class FieldBlock(TextField):
    def __init__(self, text, x, y, width, font, max_line_count=1, line_space=0, text_justification="L",
                 hanging_indent=0, use_hexadecimal_indicator=True, reverse_print=False,
                 new_line_conversion=NewLineConversion.NewLine):
        super().__init__(text, x, y, font, use_hexadecimal_indicator, reverse_print, new_line_conversion)
        self.text_justification = text_justification
        self.width = width
        self.max_line_count = max_line_count
        self.line_space = line_space
        self.hanging_indent = hanging_indent

    def render(self, options):
        text = self.font.render(options)
        text = text + self.origin.render(options)

        text = text + "^FB" + str(options.scale(self.width)) + "," + str(self.max_line_count) + "," + str(
            options.scale(self.line_space)) + "," + self.text_justification + "," + str(
            options.scale(self.hanging_indent))

        text = text + self.render_field_data()
        return text


class Font(object):
    def __init__(self, font_name="0", orientation="N", width=30, height=30):
        self.font_name = font_name
        self.orientation = orientation
        self.width = width
        self.height = height

    def render(self, options):
        return "^A" + self.font_name + self.orientation + "," + str(options.scale(self.height)) + "," + str(
            options.scale(self.width))


class QrCode(PositionedElement):
    def __init__(self, content, x, y, model=2, magnification_factor=2, error_collection="Q", mask_value=7):
        super().__init__(x, y)
        self.content = content
        self.model = model
        self.magnification_factor = magnification_factor
        self.error_collection = error_collection
        self.mask_value = mask_value

    def render(self, options):
        text = self.origin.render(options)
        text = text + "^BQN," + str(self.model) + "," + str(
            options.scale(self.magnification_factor)) + "," + self.error_collection + "," + str(self.mask_value)
        text = text + "^FD" + self.error_collection + "M," + self.content + "^FS"
        return text


class RawZpl:
    def __init__(self, raw_zpl):
        self.raw_zpl = raw_zpl

    def render(self, options):
        return self.raw_zpl


class TextBlock(TextField):
    def __init__(self, text, x, y, width, height, font, use_hexadecimal_indicator=True, reverse_print=False,
                 new_line_conversion=NewLineConversion.Space):
        super().__init__(text, x, y, font, use_hexadecimal_indicator, reverse_print, new_line_conversion)

        self.width = width
        self.height = height

    def render(self, options):
        text = self.font.render(options)
        text = text + self.origin.render(options)

        text = text + "^TB" + self.font.orientation + "," + str(options.scale(self.width)) + "," + \
               str(options.scale(self.height))

        text = text + self.render_field_data()
        return text
