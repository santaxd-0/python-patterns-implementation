from director import Director
from builders import OfficeComputerBuilder


def client_code():
    director = Director()
    builder = OfficeComputerBuilder()
    director.builder = builder

    director.create_computer()
    print(director.builder.get_computer())

def main():
    client_code()

if __name__ == "__main__":
    main()