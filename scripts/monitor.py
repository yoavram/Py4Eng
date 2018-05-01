import time
from watchdog.observers import Observer
import watchdog.events


class MyEventHandler(watchdog.events.FileSystemEventHandler):
    def on_created(self, event):
        filename = event.src_path
        print("Hello,", filename)

    def on_deleted(self, event):
        filename = event.src_path
        print("Goodbye,", filename)

if __name__ == '__main__':
    path = '.'
    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break
    observer.stop()
    observer.join()
