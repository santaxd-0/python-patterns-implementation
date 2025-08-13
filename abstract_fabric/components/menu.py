from abc import ABC, abstractmethod


class Menu(ABC):

    def __init__(self, points):
        self._points = points

    @abstractmethod
    def show_all_points(self):
        pass

    @abstractmethod
    def choose_point(self):
        pass


class WindowsMenu(Menu):

    def show_all_points(self):
        return f"All points in Windows menu showed: {self._points}"

    def choose_point(self):
        return "Point was chose"


class MacOSMenu(Menu):

    def show_all_points(self):
        return f"All points in macOS menu showed {self._points}"

    def choose_point(self):
        return "Point was chose"


class LinuxMenu(Menu):

    def show_all_points(self):
        return f"All points in Linux menu showed {self._points}"

    def choose_point(self):
        return "Point was chose"