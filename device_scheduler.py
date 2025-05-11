import asyncio
from collections import deque
import os
import random
import datetime
import logging
import sys

# ---------- Setup logging ----------
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "device_log.txt")

# Check and create log directory and file if not present
os.makedirs(LOG_DIR, exist_ok=True)
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'w') as f:
        f.write("=== Device Access Log ===\n")

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)  # Also print to console
    ]
)

# ---------- Device + Scheduler Simulation ----------
devices = deque(["Device A", "Device B", "Device C"])

async def access_shared_resource(device):
    logging.info(f"{device} is accessing the shared resource.")
    await asyncio.sleep(random.uniform(0.5, 1.5))  # Simulate work
    logging.info(f"{device} finished.")

async def round_robin_scheduler():
    
    try:
        for i in range(6):  # (Keep it simple) each device gets 2 turns for a total of 6 cycles
            
            logging.info(f"\n--- Cycle {i + 1} ---")
            
            current_device = devices[0]
            
            await access_shared_resource(current_device)
            
            devices.rotate(-1)  # Rotate priority
            
            logging.info(f"Queue after rotation: {list(devices)}")
    
    except Exception as e:
        logging.error(f"Scheduler error: {e}")
    
    finally:
        logging.info("Scheduler completed. Graceful shutdown.\n")

# ---------- Run ----------
if __name__ == "__main__":
    asyncio.run(round_robin_scheduler())
