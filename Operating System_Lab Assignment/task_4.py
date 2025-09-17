import os

def read_status(pid):
    status_file = f"/proc/{pid}/status"
    info = {}
    with open(status_file, "r") as f:
        for line in f:
            if line.startswith("Name:") or line.startswith("State:") or line.startswith("VmSize:"):
                key, value = line.split(":", 1)
                info[key.strip()] = value.strip()
    return info

def read_exe(pid):
    try:
        return os.readlink(f"/proc/{pid}/exe")
    except FileNotFoundError:
        return "Executable path not found"
    except PermissionError:
        return "Permission denied"

def read_fds(pid):
    fd_dir = f"/proc/{pid}/fd"
    try:
        return [os.readlink(os.path.join(fd_dir, fd)) for fd in os.listdir(fd_dir)]
    except FileNotFoundError:
        return ["No FD info (process might have ended)"]
    except PermissionError:
        return ["Permission denied"]

def main():
    pid = input("Enter PID: ").strip()
    if not pid.isdigit():
        print("Invalid PID")
        return

    status = read_status(pid)
    exe = read_exe(pid)
    fds = read_fds(pid)

    print("\n--- Process Info ---")
    print(f"Name: {status.get('Name', 'N/A')}")
    print(f"State: {status.get('State', 'N/A')}")
    print(f"Memory Usage: {status.get('VmSize', 'N/A')}")
    print(f"Executable Path: {exe}")
    print("\nOpen File Descriptors:")
    for fd in fds:
        print(f" - {fd}")

if __name__ == "__main__":
    main()
