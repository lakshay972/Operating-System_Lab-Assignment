cat > zombie.py << 'EOF'
import os
import time

pid = os.fork()
if pid == 0:
    print(f"Child (Zombie demo): PID={os.getpid()}, Parent={os.getppid()}")
    os._exit(0)
else:
    print(f"Parent (Zombie demo): PID={os.getpid()} created child {pid}")
    time.sleep(20)
    print("Parent exiting...")
EOF
