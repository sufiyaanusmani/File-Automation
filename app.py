# Author: Sufiyaan Usmani (https://github.com/sufiyaanusmani)
# Email: usmanisufiyaan@gmail.com

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time
import os
import shutil
from pathlib import Path

directory = "C:\\Users\\Sufyan\\Downloads"
# directory = Path("D:\\testdir")

images = (".bmp", ".jpg", ".jpeg", ".gif",
          ".png", ".eps", ".ico", "jfif", "webp")
documents = (".doc", ".docx", ".odt", ".pdf", ".xls",
             ".xlsx", ".ods", ".ppt", ".pptx", ".txt")
media = (".mp3", ".mp4")
compressed = (".zip", ".rar")
codes = (".cpp", ".c", ".py", ".exe", ".js", ".html", ".css", ".php")


class Watcher:
    DIRECTORY_TO_WATCH = directory

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(
            event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created' or event.event_type == "modified":
            # Take any action here when a file is first created.
            print(f"Received created event - {event.src_path}.")
            move()


def move():
    files = os.listdir(directory)
    for file1 in files:
        oldDir = os.path.abspath(f"{directory}\\{file1}")
        if file1.endswith(images):
            newDir = Path("C:\\Users\\Sufyan\\Downloads\\Images\\" + file1)
            shutil.move(oldDir, newDir)
        elif file1.endswith(documents):
            newDir = Path("C:\\Users\\Sufyan\\Downloads\\Documents\\" + file1)
            shutil.move(oldDir, newDir)
        elif file1.endswith(media):
            newDir = Path("C:\\Users\\Sufyan\\Downloads\\Audios\\" + file1)
            shutil.move(oldDir, newDir)
        elif file1.endswith(compressed):
            newDir = Path("C:\\Users\\Sufyan\\Downloads\\Compressed\\" + file1)
            shutil.move(oldDir, newDir)
        elif file1.endswith(codes):
            newDir = Path("C:\\Users\\Sufyan\\Downloads\\Codes\\" + file1)
            shutil.move(oldDir, newDir)


if __name__ == '__main__':
    w = Watcher()
    try:
        move()
        w.run()
    except Exception as ex:
        print(ex)
