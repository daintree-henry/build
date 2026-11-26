# memory_usage.py

import sys
import os
import time

time.sleep(20)
approx_mb = int(os.getenv('APPROX_MB', '300'))
bytes_per_mb = 1024 * 1024
ints_per_mb = (bytes_per_mb // 24)
large_list = [0] * (ints_per_mb * approx_mb)

print(f'Approximate memory usage: {sys.getsizeof(large_list)} bytes')

# Keep the script running for 10 minutes.
time.sleep(600)
