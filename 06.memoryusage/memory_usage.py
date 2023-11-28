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

# 스크립트를 10분간 실행 상태로 유지합니다.
time.sleep(600)
