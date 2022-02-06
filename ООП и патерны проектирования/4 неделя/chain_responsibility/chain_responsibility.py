MY_INT, MY_FLOAT, MY_STR = "INT", "FLOAT", "STR"


class EventGet:
    def __init__(self, prop):
        self.kind = {int:MY_INT, float:MY_FLOAT, str:MY_STR}[prop];
        self.prop = None;


class EventSet:
    def __init__(self, prop):
        self.kind = {int:MY_INT, float:MY_FLOAT, str:MY_STR}[type(prop)];
        self.prop = prop;


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            return self.__successor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == MY_INT:
            if event.prop is None:
                return obj.integer_field
            else:
                obj.integer_field = event.prop;
        else:
            return super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == MY_STR:
            if event.prop is None:
                return obj.string_field
            else:
                obj.string_field = event.prop;
        else:
            return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == MY_FLOAT:
            if event.prop is None:
                return obj.float_field
            else:
                obj.float_field = event.prop;
        else:
            return super().handle(obj, event)