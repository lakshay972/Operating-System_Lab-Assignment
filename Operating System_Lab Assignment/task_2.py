import os

def main():
    commands = [
        ["ls"],
        ["date"],
        ["ps"],
        ["whoami"],
        ["uname", "-a"]
    ]

    print(f"Parent PID: {os.getpid()} is creating {len(commands)} children...\n")

    for i, cmd in enumerate(commands):
        pid = os.fork()
        if pid == 0:
            print(f"Child {i+1}: PID={os.getpid()}, executing command: {' '.join(cmd)}")
            os.execvp(cmd[0], cmd)
        else:
            continue

    for _ in commands:
        os.wait()

    print("\nParent: All children have finished.")

if __name__ == "__main__":
    main()
