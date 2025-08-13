from abc import ABC, abstractmethod


class Button(ABC):

    def __init__(self, components_style):
        self._components_style = components_style

    @abstractmethod
    def press(self):
        pass

    @abstractmethod
    def show_style(self):
        pass


class WindowsButton(Button):

    def press(self):
        return "Windows button pressed!"

    def show_style(self):
        return f"Windows button style: {self._components_style}"


class MacOSButton(Button):

    def press(self):
        return "macOS button pressed!"

    def show_style(self):
        return f"macOS button style: {self._components_style}"


class LinuxButton(Button):

    def press(self):
        return "Linux button pressed!"

    def show_style(self):
        return f"Linux button style: {self._components_style}"