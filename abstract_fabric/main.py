from system_style import (WindowsComponents,
                          ConcreteComponents,
                          LinuxComponents,
                          MacOSComponents)

system_list = {
    "windows": WindowsComponents(),
    "linux": LinuxComponents(),
    "macos": MacOSComponents()
}

def client_code(components: ConcreteComponents) -> None:
    os_window = components.create_window()
    print(os_window.open())
    print(os_window.show_title())
    print(os_window.close())

    os_button = components.create_button()
    print(os_button.press())
    print(os_button.show_style())

    os_menu = components.create_menu()
    print(os_menu.show_all_points())
    print(os_menu.choose_point())

def main():
    operation_system = input("Enter OS that you use: ").lower()

    if operation_system not in system_list:
        print("Your system is not supported!")
        return

    os_fabric = system_list[operation_system]
    client_code(os_fabric)


if __name__ == '__main__':
    main()