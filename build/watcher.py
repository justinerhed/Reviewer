import subprocess
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path

SCRIPT = "gui.py"  # Your GUI script

class ReloadHandler(FileSystemEventHandler):
    def __init__(self):
        self.process = None
        self.start_app()

    def start_app(self):
        if self.process:
            self.process.kill()
        print("🔄 Reloading gui.py...")
        self.process = subprocess.Popen([sys.executable, SCRIPT])

    def on_any_event(self, event):
        if event.src_path.endswith(".py") or event.src_path.endswith(".png"):
            self.start_app()

if __name__ == "__main__":
    event_handler = ReloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path=str(Path(".")), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        if event_handler.process:
            event_handler.process.kill()
    observer.join()
