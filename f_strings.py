import inspect
import string


def f(f_string):
    frame = inspect.stack()[1][0]
    return Formatter(frame.f_globals, frame.f_locals).format(f_string)


class Formatter(string.Formatter):
    def __init__(self, globals_, locals_):
        self.globals = globals_
        self.locals = locals_

    def _vformat(self, *args, **kwargs):
        _vformat = super(Formatter, self)._vformat
        if 'auto_arg_index' in inspect.getargspec(_vformat)[0]:
            kwargs['auto_arg_index'] = False
        return _vformat(*args, **kwargs)

    def get_field(self, field_name, args, kwargs):
        if not field_name.strip():
            raise ValueError('empty expression not allowed')
        return eval('(' + field_name + ')', self.globals, self.locals), None
