class Logger :
    def __init__(self):
        print("--- LOG STARTED ---")
    def __del__(self):
        print("--- LOG SAVED & CLOSED ---")