from enum import Enum


class NewLineConversion(Enum):
    Space = 1,
    Empty = 2,
    NewLine = 3


class Options:
    def __init__(self, include_start_end_tags=True, source_print_dpi=203, target_print_dpi=203):
        self.start_end_tags = include_start_end_tags
        self.source_print_dpi = source_print_dpi
        self.target_print_dpi = target_print_dpi
        self.scale_factor = self.target_print_dpi / self.source_print_dpi

    def scale(self, input):
        return input * self.scale_factor

    def scale_to_string(self, input):
        return str(self.scale(input))


class SpecialCharacter(Enum):
    registered_tradeMark = "A"
    copyright = "B"
    trade_mark = "C"
    underwriters_laboratories_approval = "D"
    canadian_standards_association_approval = "E"
