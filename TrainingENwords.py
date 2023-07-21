import pathlib
import random


def load_words_from_file():
    global pathToWords
    global len_of_wordsFromFile_0
    with open(pathToWords, "r", encoding="UTF-8") as file:
        for line in file:
            # warunek spawdzający czy format pliku jest "EN - PL" a nie np "EN -PL"
            if line.find(" - ") == -1:
                print("Check the file. Is it compatible with the scheme: EN - PL")
                exit()
            # metodą split dzieli string na 2(1) i tworzy listę dwóch elementów. Znak rozdzielający to " - "
            templine = line.split(" - ", 1)
            wordsFromFile[0].append(templine[0])
            wordsFromFile[1].append(templine[1].strip())
    # długość wewnętrznej listy 0 lub 1 do metody losującej
    len_of_wordsFromFile_0 = len(wordsFromFile[0])


def draw_word():
    global len_of_wordsFromFile_0
    random_int = random.randint(0, len_of_wordsFromFile_0 - 1)
    print("ENG:", wordsFromFile[0][random_int], "\n")
    input("Press ENTER to show meaning in PL...")
    print("PL:", wordsFromFile[1][random_int], "\n\n------------------------")
    input("Press ENTER for next word in ENG...")


# --------------------------------------------------------
pathToWords = pathlib.Path("slowka.txt")
wordsFromFile = [[], []]
len_of_wordsFromFile_0 = 0

load_words_from_file()

while True:
    draw_word()

# print(wordsFromFile[0][17])
# print(wordsFromFile[1][17])
