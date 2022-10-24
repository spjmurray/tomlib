class Parameter:
    name = None
    _path = None
    type = None
    choices = None
    validator = None
    converter = None

    def __init__(self, name, path=None, type=str, choices=None, validator=None, converter=None):
        self.name = name
        self._path = path
        self.type = type
        self.choices = choices
        self.validator = validator
        self.converter = converter

    def validate(self, value):
        if self.type != type(value):
            raise RuntimeError('arg type fail')

        if self.type == str and self.choices:
            if value not in self.choices:
                raise RuntimeError('arg enumeration fail')

        if self.validator:
            if not self.validator(value):
                raise RuntimeError('arg validation fail')

    def convert(self, value):
        if not self.converter:
            return value
        return self.converter(value)

    @property
    def path(self):
        if self._path:
            return self._path
        return self.name
