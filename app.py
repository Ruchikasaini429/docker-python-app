import sys
from datetime import datetime

print(f"Python Version: {sys.version}")

current_time = datetime.now()

print(f"Current Date and Time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
