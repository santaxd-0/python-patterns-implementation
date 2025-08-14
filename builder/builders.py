from abc import ABC, abstractmethod

from computer import Computer

class Builder(ABC):
    @abstractmethod
    def install_processor(self): pass

    @abstractmethod
    def install_motherboard(self): pass

    @abstractmethod
    def install_ram(self): pass

    @abstractmethod
    def install_video_card(self): pass

    @abstractmethod
    def install_storage_device(self): pass

    @abstractmethod
    def install_power_supply(self): pass

    @abstractmethod
    def install_case(self): pass

    @abstractmethod
    def get_computer(self): pass


class OfficeComputerBuilder(Builder):

    def __init__(self):
        self._computer = Computer()

    def install_processor(self) -> Computer:
        self._computer.processor = {
            "model": "Intel",
            "frequency": "low",
            "number_of_cors": "4"
        }
        return self._computer

    def install_motherboard(self) -> Computer:
        self._computer.motherboard = {
            "socket": "Some socket",
            "chipset": "Some chipset"
        }
        return self._computer

    def install_ram(self) -> Computer:
        self._computer.ram = {
            "memory capacity": "4GB",
            "type": "DDR3",
        }
        return self._computer

    def install_video_card(self) -> Computer:
        self._computer.video_card = {
            "model": "RTX1070",
            "memory": "3GB"
        }
        return self._computer

    def install_storage_device(self) -> Computer:
        self._computer.storage_device = {
            "type": "HDD",
            "capacity": "512GB"
        }
        return self._computer

    def install_power_supply(self) -> Computer:
        self._computer.power_supply = {
            "power": "500Wt"
        }
        return self._computer

    def install_case(self) -> Computer:
        self._computer.case = {
            "size": "M",
            "color": "Black"
        }
        return self._computer

    def get_computer(self):
        return self._computer.get_info()


class GamingComputerBuilder(Builder):
    def __init__(self):
        self._computer = Computer()

    def install_processor(self) -> Computer:
        self._computer.processor = {
            "model": "AMD",
            "frequency": "high",
            "number_of_cors": "16"
        }
        return self._computer

    def install_motherboard(self) -> Computer:
        self._computer.motherboard = {
            "socket": "Some socket",
            "chipset": "Some chipset"
        }
        return self._computer

    def install_ram(self) -> Computer:
        self._computer.ram = {
            "memory capacity": "32GB",
            "type": "DDR4",
        }
        return self._computer

    def install_video_card(self) -> Computer:
        self._computer.video_card = {
            "model": "RTX5070",
            "memory": "8GB"
        }
        return self._computer

    def install_storage_device(self) -> Computer:
        self._computer.storage_device = {
            "type": "SSD",
            "capacity": "2TB"
        }
        return self._computer

    def install_power_supply(self) -> Computer:
        self._computer.power_supply = {
            "power": "700Wt"
        }
        return self._computer

    def install_case(self) -> Computer:
        self._computer.case = {
            "size": "M",
            "color": "Blue"
        }
        return self._computer

    def get_computer(self):
        return self._computer.get_info()

class WorkStationBuilder(Builder):
    def __init__(self):
        self._computer = Computer()

    def install_processor(self) -> Computer:
        self._computer.processor = {
            "model": "Intel",
            "frequency": "high",
            "number_of_cors": "32"
        }
        return self._computer

    def install_motherboard(self) -> Computer:
        self._computer.motherboard = {
            "socket": "Some socket",
            "chipset": "Some chipset"
        }
        return self._computer

    def install_ram(self) -> Computer:
        self._computer.ram = {
            "memory capacity": "64GB",
            "type": "DDR5",
        }
        return self._computer

    def install_video_card(self) -> Computer:
        self._computer.video_card = {
            "model": "RTX5070",
            "memory": "16GB"
        }
        return self._computer

    def install_storage_device(self) -> Computer:
        self._computer.storage_device = {
            "type": "SSD",
            "capacity": "4TB"
        }
        return self._computer

    def install_power_supply(self) -> Computer:
        self._computer.power_supply = {
            "power": "700Wt"
        }
        return self._computer

    def install_case(self) -> Computer:
        self._computer.case = {
            "size": "L",
            "color": "Black"
        }
        return self._computer

    def get_computer(self):
        return self._computer.get_info()