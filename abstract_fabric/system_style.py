from abc import ABC, abstractmethod

from components.button import *
from components.window import *
from components.menu import *


class ConcreteComponents(ABC):
    __components_style: dict[str, str]
    __title: str
    __points: list[int]

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_menu(self) -> Menu:
        pass

    @abstractmethod
    def create_window(self) -> Window:
        pass

class WindowsComponents(ConcreteComponents):
    __components_style = {
        "elements_accent": "flat elements",
        "color_accents": "blue",
        "font": "Segoe UI"
    }
    __title = "This is a windows!"
    __points = ["Create task", "End Task", "Show Info"]

    def create_button(self) -> WindowsButton:
        button = WindowsButton(self.__components_style)
        return button

    def create_window(self) -> WindowsWindow:
        window = WindowsWindow(self.__title)
        return window

    def create_menu(self) -> WindowsMenu:
        menu = WindowsMenu(self.__points)
        return menu


class MacOSComponents(ConcreteComponents):
    __components_style = {
        "elements_accent": "rounded elements",
        "color_accents": "grey",
        "font": "San Francisco"
    }
    __title = "This is a macOS!"
    __points = ["Create task", "End Task", "Show Info"]

    def create_button(self) -> MacOSButton:
        button = MacOSButton(self.__components_style)
        return button

    def create_window(self) -> MacOSWindow:
        window = MacOSWindow(self.__title)
        return window

    def create_menu(self) -> MacOSMenu:
        menu = MacOSMenu(self.__points)
        return menu


class LinuxComponents(ConcreteComponents):
    __components_style = {
        "elements_accent": "simple elements",
        "color_accents": "dark",
        "font": "Ubuntu"
    }
    __title = "This is a Linux!"
    __points = ["Create task", "End Task", "Show Info"]

    def create_button(self) -> LinuxButton:
        button = LinuxButton(self.__components_style)
        return button

    def create_window(self) -> LinuxWindow:
        window = LinuxWindow(self.__title)
        return window

    def create_menu(self) -> LinuxMenu:
        menu = LinuxMenu(self.__points)
        return menu