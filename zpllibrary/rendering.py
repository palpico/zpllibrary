class Engine:
    def __init__(self, elements):
        self.elements = elements

    def render(self, options):
        zpl = ''
        if options.start_end_tags:
            zpl = zpl + "^XA"

        for element in self.elements:
            zpl = zpl + (element.render(options))

        if options.start_end_tags:
            zpl = zpl + "^XZ"

        return zpl

    def to_zpl_string(self, options):
        list_of_elements = [self.elements]
        self.elements = list_of_elements
        return self.render(options)
