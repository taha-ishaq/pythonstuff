import winreg
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if not is_admin():
        print("[!] Restarting script with admin privileges...")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()

def delete_startup_registry(app_name="MyApp"):
    try:
        run_as_admin()
        
        key = winreg.HKEY_CURRENT_USER
        subkey = r"Software\Microsoft\Windows\CurrentVersion\Run"
        
        with winreg.OpenKey(key, subkey, 0, winreg.KEY_SET_VALUE) as registry_key:
            winreg.DeleteValue(registry_key, app_name)
            print(f"[-] Successfully removed {app_name} from startup registry.")
            return True
    except FileNotFoundError:
        print(f"[!] Registry entry {app_name} not found.")
    except Exception as e:
        print(f"[!] Error deleting startup registry: {e}")
    return False

if __name__ == "__main__":
    delete_startup_registry()
