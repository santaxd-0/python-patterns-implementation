from builders import Builder

class Director:
    def __init__(self) -> None:
        self.builder = None

    def create_computer(self):
        self.builder.install_processor()
        self.builder.install_motherboard()
        self.builder.install_ram()
        self.builder.install_video_card()
        self.builder.install_power_supply()
        self.builder.install_storage_device()
        self.builder.install_case()