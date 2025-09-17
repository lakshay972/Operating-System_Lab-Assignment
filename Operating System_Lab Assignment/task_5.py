import os
import time

def cpu_task(name, duration=5):
    start = time.time()
    count = 0
    while time.time() - start < duration:
        count += 1  # CPU intensive loop
    print(f"Process {name} (PID={os.getpid()}, PPID={os.getppid()}) finished with count={count}")

def main():
    priorities = [0, 5, 10, 15]  # lower = higher priority
    print(f"Parent PID: {os.getpid()} is creating {len(priorities)} children...\n")

    for i, prio in enumerate(priorities):
        pid = os.fork()
        if pid == 0:
            try:
                os.nice(prio)  # adjust priority
            except PermissionError:
                print(f"Child {i+1}: cannot decrease nice value (need root), using default priority.")
            print(f"Child {i+1}: PID={os.getpid()}, nice={os.nice(0)} starting CPU task")
            cpu_task(f"Child {i+1}")
            os._exit(0)
        else:
            continue

    for _ in priorities:
        os.wait()

    print("\nParent: All children have finished.")

if __name__ == "__main__":
    main()
