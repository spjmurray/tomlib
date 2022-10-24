from tomlib.util.parameter import Parameter

class FunctionArgs:
    args = []
    kwargs = []

    def add_positional_argument(self, name, path=None, type=str, choices=None, validator=None, converter=None):
        self.args.append(Parameter(name, path, type=type, choices=choices, validator=validator, converter=converter))

    def add_optional_argument(self, name, path=None, type=str, choices=None, validator=None, converter=None):
        self.kwargs.append(Parameter(name, path, type=type, choices=choices, validator=validator, converter=converter))

    def _lookup_kwarg(self, name):
        for kwarg in self.kwargs:
            if kwarg.name == name:
                return kwarg

        raise RuntimeError('kwarg lookup fail')

    def parse(self, *args, **kwargs):
        data = {}

        if len(args) != len(self.args):
            print(len(args), args)
            print(len(self.args), self.args)
            raise RuntimeError('positional args fail')

        for i, schema in enumerate(self.args):
            schema.validate(args[i])

            data[schema.path] = schema.convert(args[i])

        for name, value in kwargs.items():
            schema = self._lookup_kwarg(name)
            schema.validate(value)

            data[schema.path] = schema.convert(value)

        return data
