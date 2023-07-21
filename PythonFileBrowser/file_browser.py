import os
import platform
import shutil

import distro
from colorama import Fore, init

def display_system_info():
    print(Fore.YELLOW + "Python version:", platform.python_version())
    system_info = platform.uname()
    print("Operating system:", system_info.system, system_info.release)

    if platform.system() == 'Linux':
        dist_info = distro.linux_distribution(full_distribution_name=False)
        dist_name = dist_info[0]
        dist_version = dist_info[1]
        print("Linux distribution:", dist_name, dist_version)

    elif platform.system() == 'Darwin':  # macOS
        mac_version = platform.mac_ver()[0]
        print("macOS version:", mac_version)

    elif platform.system() == 'Windows':
        win_version = platform.win32_ver()[0]
        print("Windows version:", win_version)

def browse_files():
    current_directory = os.getcwd()

    while True:
        print("\n" + Fore.CYAN + "Current directory:", current_directory)
        print(Fore.RESET + "Files and directories in", current_directory + ":\n")

        for item in os.listdir(current_directory):
            if os.path.isdir(os.path.join(current_directory, item)):
                print(Fore.BLUE + item)
            else:
                print(Fore.RESET + item)

        command = input(
            "\nEnter 'back', 'd' to delete, 'c' to create folder, 't' to create/edit text file, or file/directory name to enter (q to quit): "
        )

        if command == 'q':
            break

        if command == 'back':
            current_directory = os.path.dirname(current_directory)
        elif command == 'c':
            new_folder = input("Enter folder name to create: ")
            new_folder_path = os.path.join(current_directory, new_folder)
            os.makedirs(new_folder_path, exist_ok=True)
            print(Fore.GREEN + "Folder created:", new_folder_path)
        elif command == 't':
            file_name = input("Enter text file name to create/edit: ")
            file_path = os.path.join(current_directory, file_name)

            with open(file_path, 'w') as file:
                file_content = input("Enter the text content:\n")
                file.write(file_content)

            print(Fore.GREEN + "Text file created/updated:", file_path)
        elif command == 'd':
            delete_item = input("Enter file/directory name to delete: ")
            delete_path = os.path.join(current_directory, delete_item)
            if os.path.exists(delete_path):
                if os.path.isfile(delete_path):
                    os.remove(delete_path)
                    print(Fore.RED + "File deleted:", delete_path)
                else:
                    shutil.rmtree(delete_path)  # Use shutil.rmtree() for non-empty directories
                    print(Fore.RED + "Folder deleted:", delete_path)
            else:
                print(Fore.RED + "File/Folder not found.")
        elif command == 'I type hotdogs':
            print(Fore.CYAN + "Happy Hotdogs!")
        else:
            new_path = os.path.join(current_directory, command)

            if os.path.isfile(new_path):
                if new_path.endswith('.txt'):
                    with open(new_path, 'r') as file:
                        content = file.read()
                        print("\nContent of", command + ":\n")
                        print(Fore.RESET + content)
                    edit = input("Do you want to edit this file? (y/n): ").lower()
                    if edit == 'y':
                        with open(new_path, 'w') as file:
                            new_content = input("Enter the new content:\n")
                            file.write(new_content)
                        print(Fore.GREEN + "Text file updated:", new_path)
                else:
                    print(Fore.RED + command, "is not a text file.")
            elif os.path.isdir(new_path):
                current_directory = new_path
            else:
                print(Fore.RED + "Invalid file/directory name. Try again.")

if __name__ == "__main__":
    init(autoreset=True)
    display_system_info()
    browse_files()
