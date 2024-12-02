import random
import time
import multiprocessing
from datetime import datetime

def worker():
    """Worker function to wait, print the current time, and exit."""
    wait_time = random.uniform(0, 1)  # Generate a random wait time between 0 and 1 second
    time.sleep(wait_time)  # Wait for the random amount of time
    print(f"Process {multiprocessing.current_process().name} - Time: {datetime.now()}")

if __name__ == "__main__":
    # Make three different processes
    processes = []
    for i in range(3):
        process = multiprocessing.Process(target=worker, name=f"Process-{i+1}")
        processes.append(process)
        process.start()  # Start the process

    # Wait until full completion is made by all of the processes
    for process in processes:
        process.join()