import os
import sys
from PySide6.QtCore import QObject, Property, Slot, Signal
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType
from __feature__ import true_property, snake_case  # noqa: F401


PROJECT_PATH = os.path.dirname(os.path.realpath(__name__))


class MyComponent(QObject):
    some_value_changed = Signal(int)  # [3]

    def __init__(self, parent=None):
        super(MyComponent, self).__init__(parent)

        self._value = 10

    @Property(int)  # [1]
    def some_value(self):
        return self._value

    @some_value.setter  # [1]
    def some_value(self, value):
        if value == self._value:
            return
        self._value = value
        self.some_value_changed.emit(value)

    @Slot(int)  # [2]
    def some_slot(self, value):
        print(f"called slot {value}")


def register_types():
    MODULE_NAME = 'myapp'
    qmlRegisterType(MyComponent, MODULE_NAME, 1, 0, MyComponent.__name__)


class MyApp(QObject):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)

        self._engine = QQmlApplicationEngine()
        self._engine.import_path_list = [PROJECT_PATH]
        register_types()
        qml_main = os.path.join(PROJECT_PATH, "main.qml")
        self._engine.load(qml_main)


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    gui = MyApp()
    sys.exit(app.exec())
