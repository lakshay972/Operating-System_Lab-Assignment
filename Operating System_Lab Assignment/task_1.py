import os

def main():
    N = 5
    print(f"Parent PID: {os.getpid()} is creating {N} children...\n")

    for i in range(N):
        pid = os.fork()
        if pid == 0:
            print(f"Child {i+1}: PID={os.getpid()}, Parent PID={os.getppid()}, Message=Hello from child {i+1}")
            os._exit(0)
        else:
            continue

    for _ in range(N):
        os.wait()

    print("\nParent: All children have finished.")

if __name__ == "__main__":
    main()
