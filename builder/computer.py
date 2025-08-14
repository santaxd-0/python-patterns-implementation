from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Computer:
    processor: Dict[str, str] = field(default_factory=dict)
    motherboard: Dict[str, str] = field(default_factory=dict)
    ram: Dict[str, str] = field(default_factory=dict)
    video_card: Dict[str, str] = field(default_factory=dict)
    storage_device: Dict[str, str] = field(default_factory=dict)
    power_supply: Dict[str, str] = field(default_factory=dict)
    case: Dict[str, str] = field(default_factory=dict)


    def get_info(self) -> str:
        info = (f"----Computer info----\n"
                f"Processor: {self.processor['model']}\n"
                f"Motherboard: {self.motherboard['socket']}\n"
                f"RAM: {self.ram['memory capacity']}, {self.ram['type']}\n"
                f"Video card: {self.video_card['model']}, {self.video_card['memory']}\n"
                f"Storage device: type - {self.storage_device["type"]}, capacity - {self.storage_device["capacity"]}\n"
                f"Power supply: {self.power_supply["power"]}\n"
                f"Case: size - {self.case["size"]}, color - {self.case["color"]}")
        return info
