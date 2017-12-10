import time


class Timer:
    def __init__(self):
        self.start = 0.0

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print("elapsed", end - self.start, "s")
