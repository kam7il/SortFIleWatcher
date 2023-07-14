# import datetime
import pathlib
import time


# sprawdzamy poprzez timestamp czy plik był modyfikowany
def check_modification():
    global currentTimeStampWatchingFile
    if currentTimeStampWatchingFile != pathWatchingFile.stat().st_mtime:
        print("zmodyfikowano")
        return True
    else:
        print("nie zmodyfikowano")
        return False


# wczytujemy plik do listy
def file_operation_read():
    global pathWatchingFile
    dataFromFile.clear()
    with open(pathWatchingFile, "r", encoding="utf8") as file:
        for line in file:
            if line != "\n":
                dataFromFile.append(line.lower().strip())
                # print(line.strip())


# sortowanie i nadpisanie pliku
def file_operation_sort_write():
    global currentTimeStampWatchingFile
    dataFromFile.sort()
    with open(pathWatchingFile, "w", encoding="utf8") as file:
        for line in dataFromFile:
            file.write(line + "\n")
    currentTimeStampWatchingFile = pathWatchingFile.stat().st_mtime


# -----------------------------------------------------------------------------

pathWatchingFile = pathlib.Path("slowka.txt")
dataFromFile = []
currentTimeStampWatchingFile = pathWatchingFile.stat().st_mtime

while True:
    if check_modification():
        file_operation_read()
        file_operation_sort_write()
    time.sleep(60)
