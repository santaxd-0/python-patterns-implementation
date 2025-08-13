from abc import ABC, abstractmethod


class Window(ABC):

    def __init__(self, title: str):
        self._title = title

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def show_title(self):
        pass


class WindowsWindow(Window):

    def open(self):
        return "Windows window opened!"

    def close(self):
        return "Windows window closed!"

    def show_title(self):
        return f"Windows window title: {self._title}"


class MacOSWindow(Window):

    def open(self):
        return "macOS window opened!"

    def close(self):
        return "macOS window closed!"

    def show_title(self):
        return f"macOS window title: {self._title}"


class LinuxWindow(Window):

    def open(self):
        return "Linux window opened!"

    def close(self):
        return "Linux window closed!"

    def show_title(self):
        return f"Linux window title: {self._title}"