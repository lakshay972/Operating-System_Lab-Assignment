cat > orphan.py << 'EOF'
import os
import time

pid = os.fork()
if pid == 0:
    time.sleep(10)
    print(f"Child (Orphan demo): PID={os.getpid()}, New Parent={os.getppid()}")
else:
    print(f"Parent (Orphan demo): PID={os.getpid()} created child {pid} and will exit now")
    os._exit(0)
EOF
